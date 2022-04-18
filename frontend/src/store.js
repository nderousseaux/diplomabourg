import { reactive } from "vue"

const store = {
  state: reactive({
    jeu: [],
    gameId: '',
    playerId: '',
    token: ''
  }),
  setGameId(id) {
    this.state.gameId = id
  },
  setPlayerId(id) {
    this.state.playerId = id
  },
  setToken(token) {
    this.state.token = token
  },
  setJeu(jeu) {
    this.state.jeu = jeu
  }
}

export default store
