<template>
	<div>
		<img id="logo" alt="Logo Diplomabourg" title="Logo Diplomabourg"
			src="../assets/img/logo.png"/>
		<div>
			<div id="lobby">
				<div id="joueurs">
					<div>
						<img alt="Drapeau français" title="Drapeau français"
						src="../assets/img/flags/france.png"/>
						<button @click='ready()'>Prêt</button>
					</div>
					<div>
						<img alt="Drapeau allemand" title="Drapeau allemand"
						src="../assets/img/flags/germany.png"/>
						<button class="inactif">Prêt</button>
					</div>
					<div>
						<img alt="Attente du joueur" title="Attente du joueur"
						src="../assets/img/flags/loading.png"/>
					</div>
					<div>
						<img alt="Attente du joueur" title="Attente du joueur"
						src="../assets/img/flags/loading.png"/>
					</div>
					<div>
						<img alt="Attente du joueur" title="Attente du joueur"
						src="../assets/img/flags/loading.png"/>
					</div>
					<div>
						<img alt="Attente du joueur" title="Attente du joueur"
						src="../assets/img/flags/loading.png"/>
					</div>
					<div>
						<img alt="Attente du joueur" title="Attente du joueur"
						src="../assets/img/flags/loading.png"/>
					</div>
				</div>
				<div id="actions">
					<button>Créer une partie</button>
					<button>Commencer la partie</button>
				</div>
			</div>
			<div id="chat">
				<h1>Chat</h1>
				<div>Messages ici</div>
				<form name="message" action="">
					<input type="text" name="msg" id="msg" placeholder="Entrez votre message"/>
				</form>
			</div>
		</div>
	</div>
</template>

<script>
//import api from '../api.js'
// get game_id ??
// get username ??

export default {
	methods: {
		ready() {
//			api.put('/games/' + game_id + '/players/' + username, {ready: true})
		}
	}
}
</script>

<style scoped>
	/* Div principale */
	#app > div{
		background: url("../assets/img/map.jpeg");
		display: flex;
		flex-direction: column;
		width: 100vw;
		height: 100vh;
		align-items: center;
	}
	#logo{
		width: 430px;
		height: 163px;
		margin: 20px 0;
	}
	#app > div > div{
		display: flex;
		flex-direction: row;
		width: 100vw;
	}
	#lobby{
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		align-items: center;
		width: 80vw;
		height: calc(100vh - 203px)
	}

	/* Chat */
	#chat{
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		background-color: rgba(42, 58, 73, 0.7);
		width: calc(20vw - 10px);
		height: calc(100% - 10px);
		margin: 0 10px 10px 0;
		border-radius: 10px;
	}
	#chat > h1{
		line-height: 64px;
		margin: 0;
		border-style: solid;
		border-width: 0 0 4px;
		border-image: radial-gradient(#ae0132,#1c0043) 1;
		color: #ffffff;
		text-align: center;
	}
	#chat > div{
		color: wheat;
	}
	#chat > form > input[type=text]{
		background-color: rgb(42, 58, 73);
		color: #ffffff;
		width: calc(100% - 20px);
		padding: 0 10px;
		font-size: 24px;
		outline: none;
		border-style: none;
	}

	/* Pays du joueur */
	#joueurs{
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		justify-content: space-evenly;
		width: 80%;
		height: 50vh;
		background-color: rgba(42, 58, 73, 0.7);
		border-radius: 10px;
	}
	#joueurs > div{
		display: flex;
		flex-direction: column;
		width: 23%;
		height: calc(50% - 40px);
		margin: 20px 0;
		align-items: center;
	}
	#joueurs > div > img{
		width: 98px;
		height: 64px;
	}

	/* Bouton */
	button,
	input[type=submit]{
		margin: 20px 0;
		padding: 4px 32px;
		background-color: #800124;
		background-image: linear-gradient(#002843, rgba(255, 255, 255, 0));
		transition: 0.7s;
		color: #ffffff;
		font-size: 28px;
		border-radius: 20px;
		border-style: none;
		cursor: pointer;
		box-shadow: 0px 0px 15px 5px #002843;
	}
	button:hover,
	input[type=submit]:hover{
		background-color: #4682b4;
	}
	button:active,
	input[type=submit]:active{
		background-color: #376890;
	}
	#actions{
		display: flex;
		width: 100%;
		justify-content: space-evenly;
	}
	.inactif{
		background-color: #000000;
		background-image: linear-gradient(#808080, rgba(255, 255, 255, 0));
		cursor: not-allowed;
	}
	.inactif:hover{
		background-color: #000000;
	}
	.inactif:active{
		background-color: #000000;
	}

/* Version mobile */
@media screen and (max-width:769px){
	/* Div principale */
	#logo{
		width: 324px;
		height: 123px;
	}
}
</style>
