import { createRouter, createWebHistory, createWebHashHistory } from "vue-router"

import HomePage from "../components/HomePage.vue"
import LobbyPage from "../components/LobbyPage.vue"
import GameMap from "../components/GameMap"

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
    meta: {
      title: "Diplomabourg"
    }
  },
  {
    path: "/lobby/:id",
    name: "Lobby",
    component: LobbyPage,
    meta: {
      title: "Diplomabourg - Lobby"
    }
  },
  {
    path: "/jeu/:id",
    name: "Jeu",
    component: GameMap,
    meta: {
      title: "Diplomabourg - Jeu"
    }
  }
];

const router = createRouter({
  history: process.env.IS_ELECTRON ? createWebHashHistory() : createWebHistory(),
  routes,
});

router.afterEach((to, from) => {
  console.log(from, to);
  document.title = to.meta.title;
})

export default router;
