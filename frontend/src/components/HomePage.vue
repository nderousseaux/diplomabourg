<template>
	<div>
		<img id="logo" alt="Logo Diplomabourg" title="Logo Diplomabourg" src="../assets/img/logo.png"/>
		<div id="pays">
			<img alt="Drapeau français" title="Drapeau français" src="../assets/img/flags/france.png"/>
			<p>France</p>
		</div>
		<button id="bouton">Créer une partie</button>
	</div>
	<dialog id="lancer">
		<h1>Paramètres de la partie</h1>
		<form id="choix" method="dialog">
			<div>
				<label for="nom">Nom de la partie</label>
				<input type="text" id="nom" name="nom"/>
			</div>
			<div>
				<label for="nbrJ">Nombre de joueurs</label>
				<input type="number" onkeydown="return false" id="nbrJ" name="nbrJ" min="2" max="7" value="7"/>
			</div>
			<div>
				<label for="mdp">Mot de passe</label>
				<input type="password" id="mdp" name="mdp"/>
			</div>
			<p>Tous les champs ne sont pas complétés</p>
			<div>
				<button>Annuler</button>
				<input type="submit" value="Créer"/>
			</div>
		</form>
	</dialog>
</template>

<script>
export default {
	mounted() {
		// Pour paramétrer la partie
		let paramBtn = document.getElementById("bouton")
		let lancerDiag = document.getElementById("lancer")
		let erreur = document.querySelector("form > p")

		// Ouvrir le formulaire
		paramBtn.addEventListener("click", function onOpen() {
			if (typeof lancerDiag.showModal === "function") {
				erreur.style.display = "none"
				lancerDiag.showModal()
			}
		})

		document.querySelector("input[type=submit]").addEventListener("click", event => {
			event.preventDefault()
			var form = event.target.form

			// Si le formulaire n'est pas complet
			if (
				form["nom"].value === '' ||
				form["mdp"].value === ''
				) {
					console.log("Erreur")
					erreur.style.display = "block"
				}

			// Sinon on peut envoyer au back
			else {
				erreur.style.display = "none"
				console.log("Nom de la partie :", form["nom"].value,
							"\nNombre de joueurs :", form["nbrJ"].value,
							"\nMot de passe :", form["mdp"].value)
			}
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
		width: 100vw;
		height: 100vh;
		align-items: center;
	}
	#logo{
		width: 30vw;
		margin: 5vh 0;
	}

	/* Pays du joueur */
	#pays{
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	#pays > img{
		height: 128px;
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
	button,
	input[type=submit]{
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
	button:hover,
	input[type=submit]:hover{
		background-color: #4682b4;
	}
	button:active,
	input[type=submit]:active{
		background-color: #376890;
	}

	/* Boîte de dialogue pour paramétrer la partie */
	#lancer{
		background-color: #2a3a49;
		border-radius: 10px;
		border-style: none;
		box-shadow: 0px 0px 15px 5px #002843;
		min-width: 35vw;
	}
	#lancer > h1{
		color: #ffffff;
		font-size: 40px;
		margin: 10px 0 30px;
		text-align: center;
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
		align-items: center;
		width: 80%;
	}
	#lancer > form > p{
		display: none;
		font-size: 20px;
		color: lightcoral;
		margin-bottom: 0;
	}
	#lancer > form > div > label{
		color: #ffffff;
		font-size: 25px;
		width: 49%;
		text-align: left;
	}
	input[type=number],
	input[type=password],
	input[type=text]{
		width: calc(50% - 10px);
		font-size: 25px;
		outline: none;
		margin: 2px 0;
		padding: 0 5px;
		border-style: none;
		background-color: #3b5167;
		color: #ffffff;
		height: 30px;
	}
	input[type=number]{
		text-align: right;
		caret-color: transparent;
		user-select: none;
		cursor: default;
	}
	#lancer > form > div > button,
	#lancer > form > div > input[type=submit]{
		padding: 4px 22px;
		border: none;
		line-height: 40px;
		margin: 30px 0 10px;
		outline: inherit;
		flex-basis: 40%;
	}

/* Version mobile */
@media screen and (max-width:769px){
	/* Div principale */
	#logo{
		width: 90vw;
	}

	/* Boîte de dialogue pour paramétrer la partie */
	#lancer > h1{
		font-size: 30px;
	}
	#lancer > form > div{
		flex-direction: column;
		width: 90%;
		align-items: center;
	}
	#lancer > form > div > label{
		font-size: 25px;
		width: 100%;
		text-align: center;
	}
	#lancer > form > div > input{
		width: 100%;
		margin-bottom: 10px;
	}
	#lancer > form > div:last-child{
		flex-direction: row;
	}
	#lancer > form > div > button{
		font-size: 25px;
	}
}
</style>