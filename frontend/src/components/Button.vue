<template>
	<div>
	</div>
</template>

<script>

export default {
	name: 'Button',
	props: [],
	computed: {
	},
	methods: {
		
	},
	data() {
		return {
			init : ["Création de salon", "Réjoindre un salon", "Règles du jeu"],
			config : ["Langues", "Temos de discussion", "Nombre de joueurs"],
			config_init : ["Par défaut", "Confirmation"],
			saloon : [],
			color: ["btn-red", "btn-green", "btn-blue"]
		}
	},
	mounted(){
	}
}
</script>

<style scoped>
	.btn33{
		margin: 10px 0px;
		width: 33.33%;
		height: 60px;
		color: #ffffff;
	}
	
	.btn80{
		margin: 10px 0px;
		width: 80%;
		height: 60px;
		color: #ffffff;
	}

	.btn-red{
		background-color: #ff0000;        
	}

	.btn-green{
		background-color: #00ff00;
	}

	.btn-blue{
		background-color: #0000ff;
	}

</style>
