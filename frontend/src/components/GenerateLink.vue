<template>
  <button @click='showLink()'>Générer le lien</button>
  <p v-if='link'>{{link}}</p>
</template>


<script>
import api from 'api.js'

export default {
  data() {
    return {
      link: ''
    }
  },
  methods: {
    showLink() {
      this.link = api.baseURL + '/games/' + {{gameId}}
    }
  }
}
</script>
