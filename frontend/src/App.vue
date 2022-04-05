<template>
	<GameMaps></GameMaps>
</template>

<script>
import GameMaps from './views/GameMaps.vue'

export default {
	name: 'App',
	components: {
		GameMaps
	}
}
</script>

<style lang="css">
@import './assets/css/main.css';
#app {
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
}
</style>
