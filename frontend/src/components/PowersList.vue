<template lang="html">

  <p v-if='powers'>{{powers}}</p>

</template>



<script>

import api from 'api.js'

const pow = api.get('/maps')
this.powers = pow.data.powers

export default {
  data() {
    return {
      powers: ''
    }
  },
  name: 'PowersList'
}
</script>
