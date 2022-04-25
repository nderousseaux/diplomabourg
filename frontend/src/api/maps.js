import { axios } from "@/api";

let url = "/maps";

const maps = {
  getAll() {
    return axios.get(url);
  },
};

export default maps;
