<template>
  <button @click='validate()'>Valider les ordres</button>
</template>

<script>
import api from 'api.js'

export default {
  data() {
    return {
      gameId: ''
      playerId: ''
    }
  }
  methods: {
    validate() {
      api.put('/games/' + {{gameId}} + '/players/' + {{playerId}}, {"ready":true})
    }
  }
}
</script>
