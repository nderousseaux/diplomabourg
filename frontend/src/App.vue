<template>
	<!-- <HomePage/> -->
	<LobbyPage/>
	<!-- <GameMap/> -->
</template>

<script>
// import HomePage from './components/HomePage.vue'
import LobbyPage from './components/LobbyPage.vue'
// import GameMap from './components/GameMap.vue'

export default
{
	name: "App",
	components:
	{
		// HomePage
		LobbyPage
		// GameMap
	}
}
</script>

<style>
@import "assets/css/main.css";
</style>
