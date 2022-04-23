import {createApp} from "vue"
import App from "./App.vue"

import router from './router'

createApp(App)
  .use(router)
  //.use(VueSocketio, "http://localhost:6543/")
  .mount('#app')