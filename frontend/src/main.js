import { createApp} from 'vue'
import App from './App.vue'

import router from './router'

import api from "./api";

// config.productionTip = false;


api.init("/backend");


/*
new Vue({
  render: h => h(App),
  router
}).use(router).$mount('#app')
*/

createApp(App).use(router).mount('#app')