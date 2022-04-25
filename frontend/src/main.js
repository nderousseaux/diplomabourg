import {createApp} from "vue";
import App from "./App.vue";
import router from './router';
import api from "./api/index.js";

api.init("/backend");

createApp(App).use(router).mount('#app');
//.use(VueSocketio, "http://localhost:6543/")
