import { createRouter ,createWebHistory  } from "vue-router"

import HomePage from "../components/HomePage.vue"
import LobbyPage from "../components/LobbyPage.vue"
import GameMap from "../components/GameMap.vue"

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
    meta: {
      title: 'home'
    }
  },
  {
    path: "/lobby",
    name: "Lobby",
    component: LobbyPage,
    meta: {
      title: 'Lobby'
    }
  },
  {
    path: "/jeu",
    name: "Jeu",
    component: GameMap,
    meta: {
      title: 'Jeu'
    }
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.afterEach((to, from) => {
  console.log(from, to);
  document.title = to.meta.title;
})

export default router;
