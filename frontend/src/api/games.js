import { axios } from '@/api';

let base_url = "/games";
let url_playeur = "/players?password="

const games = {
    create_game(username,name,password, map_id)
    {
        let data = {
            player: {username},
            game: {name,password,map_id}
        }
        return axios.post(base_url,data);
    },
    get_game(game_id, config)
    {
        var new_url = base_url + "/" + game_id;
        return axios.get(new_url, config);
    },
    join_game(username, game_id, pwd)
    {
        var new_url = base_url + "/" + game_id + url_playeur + pwd;
        return axios.post(new_url, {username: `${username}`});
    }
};

export default games;
