<template>
	<header>
		<nav>
			<router-link class="HomeButton" to="/">Home</router-link>
			<router-link class="MapsButton" to="/Maps">Carte</router-link>
		</nav>
	</header>
</template>

<script>

export default {
	name: 'Header',
	methods: {
		getPathname(){
			return location.pathname;
		},
		hideRouter(){
			const header = document.querySelector("header")
			header.innerHTML = ``
		}
	},
	mounted(){
		if(this.getPathname() === `/Maps`)
			this.hideRouter()
	}
}
</script>

<style scoped>
	header{
		display: flex;
		flex-direction: row;
	}

	nav{
		margin: 5px 0px;
		width: 100%;
		height: auto;
		display: flex;
		flex-direction: inherit;
	}

	a{
		margin: 0px 20px;
		padding: 10px 15px;
		background-color: #006EFF;
		border: 1px solid #FFF;
		color: #FFF;
		text-decoration: none;
		text-transform: uppercase;
		font-weight: bold;
	}

	a:hover{
		margin: 0px 20px;
		padding: 10px 15px;
		color: #006EFF;
		background-color: #fff;
		border: 1px solid #006EFF;
	}
	
	a:active{
		color: #006EFF;
		background-color: #FFF;
		border: 1px dashed #006EFF;
	}
</style>
