<template>
  <button @click='ready()'>Prêt</button>
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
  }
}
</script>
