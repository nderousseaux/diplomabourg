import {createRouter, createWebHashHistory} from "vue-router"

import HomePage from "../components/HomePage.vue"
import LobbyPage from "../components/LobbyPage.vue"
import GameMap from "../components/GameMap"

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
    meta: {
      title: 'Diplomabourg'
    }
  },
  {
    path: "/games/:id",
    name: "Lobby",
    component: LobbyPage,
    meta: {
      title: 'Diplomabourg - Lobby'
    }
  },
  {
    path: "/jeu",
    name: "Jeu",
    component: GameMap,
    meta: {
      title: 'Diplomabourg - Jeu'
    }
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.afterEach((to, from) => {
  console.log(from, to);
  document.title = to.meta.title;
})

export default router;