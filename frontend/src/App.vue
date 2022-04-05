<template>
	<HomePage/>
</template>

<script>
import HomePage from './components/HomePage.vue'

export default {
	name: 'App',
	components: {
		HomePage
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
