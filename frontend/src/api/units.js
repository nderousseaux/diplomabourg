import { axios } from "@/api";

let url = "/units";

const units = {
  get_all() {
    return axios.get(url, {
      headers: { Authorization: `Bearer ${axios.token}` }
  });
  },
};

export default units;
