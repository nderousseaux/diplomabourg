<template>
  <button @click='ready()'>Prêt</button>
  <button @click='begin()'>Commencer la partie</button>
</template>

<script>
import api from 'api.js'

export default {
  data() {
    return {
      gameId: ''
      player: ''
    }
  }
  methods: {
    ready() {
      api.put('/games/' + this.gameId + '/players/' + this.player, {"ready":true})
    }
    begin() {
      api.post('/games' + this.gameId, {"state":"play"})
    }
  }
}
</script>
