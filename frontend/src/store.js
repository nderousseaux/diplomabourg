import { reactive } from "vue"

const store = {
  state: reactive({
    gameId: '',
    playerId: ''
  }),
  setGameId(id) {
    this.state.gameId = id
  },
  setPlayerId(id) {
    this.state.playerId = id
  }
}

export default store
