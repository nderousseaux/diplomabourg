import { axios } from "@/api";

let url = "/units";

const units = {
  get_all(config) {
    return axios.get(url, config);
  },
};

export default units;
