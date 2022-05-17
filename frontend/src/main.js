import { createApp} from 'vue'

import App from './App.vue'
import router from './router'
import api from "./api";

if (process.env.NODE_ENV.trim() === 'production'){
    api.init("http://185.155.93.105:10005")
}
else{
    api.init("http://localhost:6543")
}

createApp(App).use(router).mount('#app');
