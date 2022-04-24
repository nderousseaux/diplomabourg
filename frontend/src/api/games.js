import { axios } from '@/api';

let url = "/games";

const games = {
    create_game(username,name,pwd, map_id)
    {
        let data = {
            player: {username},
            game: {name,pwd,map_id}
        }
        console.log(axios)
        console.log(axios.post(url, data))
        return axios.post(url,data);
    },
};

export default games;