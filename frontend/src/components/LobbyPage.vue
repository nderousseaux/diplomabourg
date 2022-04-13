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
						<button>Prêt</button>
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
					<button>Générer le liens</button>
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
export default{
	mounted(){
	}
}
</script>

<style scoped>
	/* Div principale */
	#app > div{
		display: flex;
		flex-direction: column;
		width: 100vw;
		height: 100vh;
		align-items: center;
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
		width: calc(20vw - 10px);
		height: calc(100% - 10px);
		margin: 0 10px 10px 0;
		border-radius: 10px;
	}
	#chat > h1{
		line-height: 64px;
		margin: 0;
		text-align: center;
	}
	#chat > div{
		color: wheat;
	}
	#chat > form > input[type=text]{
		background-color: rgb(112, 128, 143);
		width: calc(100% - 20px);
		padding: 0 10px;
		font-size: 24px;
		border-radius: 0 0 10px 10px;
		outline: none;
		border-style: none;
	}

	/* Pays des joueurs */
	#joueurs{
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		justify-content: space-evenly;
		width: 80%;
		height: max-content;
		border-radius: 10px;
		overflow-x: auto;
	}
	#joueurs > div{
		display: flex;
		flex-direction: column;
		width: 23%;
		min-width: max-content;
		height: calc(64px + 64px);
		margin: 20px 0;
		align-items: center;
	}
	#joueurs > div > button{
		margin-bottom: 0;
	}
	#joueurs > div > img{
		width: 98px;
		height: 64px;
	}

	/* Bouton */
	#actions{
		display: flex;
		flex-wrap: wrap;
		width: 80%;
		justify-content: space-evenly;
	}
	#actions > button{
		width: 35%;
		min-width: fit-content;
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

/* Version tablette */
@media screen and (max-width:1370px){
	/* Div principale */
	#app > div > div{
		flex-direction: column-reverse;
		align-items: center;
		justify-content: space-evenly;
	}
	#lobby{
		width: 80vw;
		height: unset;
	}

	/* Chat */
	#chat{
		width: 80vw;
		height: 30vh;
		margin: 0 0 10px 0;
	}
	
	/* Pays des joueurs */
	#joueurs{
		width: 100%;
	}

	/* Bouton */
	#actions{
		width: 100%;
		margin-top: 5vh;
	}
}

/* Version mobile */
@media screen and (max-width:769px){
	/* Div principale */
	#lobby{
		height: calc(80vh - 203px)
	}

	/* Bouton */
	#actions{
		margin-top: unset;
	}
	#actions > button{
		width: 100%;
		font-size: 25px;
	}
	#actions > button:first-child{
		margin-bottom: 0;
	}
}
</style>