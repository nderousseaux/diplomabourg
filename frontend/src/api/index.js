import Vue from "vue";
import Axios from "axios";
import VueAxios from "vue-axios";

import maps from "./maps";
import games from "./games";
import players from "./players";
import units from "./units";
import orders from "./orders";

let axios = Axios.create();

Vue.use(VueAxios, axios);

const api = {
  init(server) {
    axios.defaults.baseURL = server;
    return axios;
  },
  maps,
  games,
  players,
  units,
  orders
};

export { axios };
export default api;