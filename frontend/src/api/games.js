import { axios } from "@/api";

let url = "/games";

const games = {
  create(username, name, password, map_id) {
    let data = {
      player: {username},
      game: {name,password, map_id}
    }
    return axios.post(url, data);
  },
};

export default games;
