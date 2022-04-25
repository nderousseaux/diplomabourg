import { axios } from "@/api";

let url = "/maps";

const maps = {
  getAll() {
    return axios.get(url);
  },
  get_map(map_id) {
    return(url + "/",map_id);
  }
};

export default maps;
