import { createApp} from 'vue'

import App from './App.vue'
import router from './router'
import api from "./api";

// api.init("/dev_url");
api.init("http://localhost:10005")

createApp(App).use(router).mount('#app');
