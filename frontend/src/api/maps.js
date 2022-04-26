import { axios } from "@/api";

let url = "/maps";

const maps = {
  getAll() {
    return axios.get(url);
  },
  getMap(map_id) {
    return axios.get(url + "/" + map_id);
  }
};

export default maps;
