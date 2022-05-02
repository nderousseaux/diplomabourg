import { axios } from "@/api";

let base_url = "/games";
let url = "/players";

const games = {
  update(id_game, id_player, username, power_id, is_ready, config) {
    let data = {
      username,
      power_id,
      is_ready
    }
    return axios.put(base_url + '/' + id_game + url + '/' + id_player, data, config);
  },
  get_users(game_id){
    var new_url = base_url + "/" + game_id + url;
    return axios.get(new_url)
  }
};

export default games;
