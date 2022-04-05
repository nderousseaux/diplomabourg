<template>
	<div>
		<img id="logo" alt="Logo Diplomabourg" title="Logo Diplomabourg" src="../assets/img/logo.png"/>
		<div id="pays">
			<img alt="Drapeau Français" title="Drapeau Français" src="../assets/img/flags/france.png"/>
			<p>France</p>
		</div>
		<button id="bouton">Créer une partie</button>
	</div>
	<dialog id="lancer">
		<h1>Paramètres de création de la partie</h1>
		<form id="choix" method="dialog">
			<div>
				<label for="nom">Nom de la partie :</label>
				<input type="text" id="nom" name="nom"/>
			</div>
			<div>
				<label for="nbrJ">Nombre de joueurs :</label>
				<input type="number" id="nbrJ" name="nbrJ" min="2" max="7" value="7"/>
			</div>
			<div>
				<label for="mdp">Mot de passe :</label>
				<input type="password" id="mdp" name="mdp"/>
			</div>
			<div>
				<button value="annuler">Annuler</button>
				<button value="confirmer">Créer</button>
			</div>
		</form>
	</dialog>
</template>

<script>
export default {
	mounted() {
		// Pour lancer la partie
		let paramBtn = document.getElementById("bouton");
		let lancerDiag = document.getElementById("lancer");


		paramBtn.addEventListener("click", function onOpen() {
			if (typeof lancerDiag.showModal === "function") {
				lancerDiag.showModal();
			}
		})

		// Action effectuée lors de l'appuie sur l'un des boutons
		lancerDiag.addEventListener("close", function onClose() {
			console.log(lancerDiag.returnValue)
		})
	}
}
</script>

<style scoped>
	/* Div principale */
	#app > div{
		background: url("../assets/img/map.jpeg");
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		height: 100vh;
		align-items: center;
	}
	#logo{
		height: 30vh;
		margin: 5vh 0;
	}

	/* Pays du joueur */
	#pays > img{
		height: 20vh;
	}
	#pays > p{
		font-size: 80px;
		margin: 0;
		font-weight: bold;
		background-image: linear-gradient(.25turn, #002843, #800124);
		-webkit-background-clip: text;
		-moz-background-clip: text;
		-webkit-text-fill-color: transparent; 
		-moz-text-fill-color: transparent;
	}

	/* Bouton */
	button{
		margin: 5vh 0;
		padding: 4px 44px;
		background-color: #800124;
		background-image: linear-gradient(#002843, rgba(255, 255, 255, 0));
		transition: 0.7s;
		color: #ffffff;
		font-size: 36px;
		border-radius: 20px;
		border-style: none;
		cursor: pointer;
		box-shadow: 0px 0px 15px 5px #002843;
	}
	button:hover{
		background-color: #4682b4;
	}
	button:active{
		background-color: #376890;
	}

	/* Boîte de dialogue pour paramétrer la partie */
	#lancer{
		background-color: #2a3a49;
		border-radius: 10px;
		border-style: none;
		box-shadow: 0px 0px 15px 5px #002843;
	}
	#lancer > h1{
		color: #ffffff;
		font-size: 40px;
		margin: 10px 0 30px;
	}
	#lancer > form{
		display: flex;
		flex-direction: column;
		margin: 0;
		align-items: center;
	}
	#lancer > form > div{
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		width: 80%;
	}
	#lancer > form > div > label{
		color: #ffffff;
		font-size: 25px;
	}
	#lancer > form> div > input{
		width: 50%;
		font-size: 25px;
		outline: none;
		margin: 2px 0;
		padding: 0 5px;
		border-style: none;
		background-color: #3b5167;
		color: #ffffff;
	}
	#lancer > form > div > button{
		padding: 4px 22px;
		border: none;
		line-height: 40px;
		margin: 30px 0 10px;
		outline: inherit;
		flex-basis: 40%;
	}
</style>