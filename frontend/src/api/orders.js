import { axios } from "@/api";

let base_url = "/games/"
let url = "/orders";

const orders = {
  create(id_game, type_order, dst_region_id, unit_id, config) {
    let data = {
      type_order,
      dst_region_id,
      unit_id
    }
    return axios.post(base_url + id_game + url, data, config);
  },
};

export default orders;