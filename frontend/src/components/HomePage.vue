<template>
	<div>
		<img id="logo" alt="Logo Diplomabourg" title="Logo Diplomabourg"
			src="../assets/img/logo.png"/>
		<div id="pays">
			<img alt="Drapeau français" title="Drapeau français"
				src="../assets/img/flags/france.png"/>
			<p>France</p>
		</div>
		<button>Créer une partie</button>
	</div>
	<dialog id="param">
		<h1>Paramètres de la partie</h1>
		<form method="dialog">
			<div>
				<label for="nom">Nom de la partie</label>
				<input type="text" id="nom" maxlength="15" name="nom"/>
			</div>
			<div>
				<label for="nbrJ">Nombre de joueurs</label>
				<input type="number" onkeydown="return false" id="nbrJ"
					name="nbrJ" min="2" max="7" value="7"/>
			</div>
			<div>
				<label for="mdp">Mot de passe</label>
				<input type="password" maxlength="15" id="mdp" name="mdp"/>
			</div>
			<p>Tous les champs ne sont pas complétés correctement</p>
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
		let paramBtn = document.querySelector("div:first-child > button")
		let lancerDiag = document.getElementById("param")
		let erreur = document.querySelector("form > p")

		// Ouvrir le formulaire
		paramBtn.addEventListener("click", function onOpen() {
			if (typeof lancerDiag.showModal === "function") {
				erreur.style.display = "none"
				lancerDiag.showModal()
			}
		})

		// Gestion du formulaire
		document.querySelector("form > div > input[type=submit]").addEventListener("click", event => {
			event.preventDefault()
			let hasError = false

			// Regex
			const regexInput = /^[\S\s]{5,15}$/

			// Fonction de vérification
			const inputPostVerif = function(){
				if (this.value.match(regexInput) == null){
					this.classList.add("error")
					this.previousElementSibling.classList.add("error")
					hasError = true
					erreur.style.display = "block"
				}
				else{
					this.classList.remove("error")
					this.previousElementSibling.classList.remove("error")
					hasError = false
					erreur.style.display = "none"
				}
			}
			const inputPostVerifNbr = function(){
				if (this.value < 2 || this.value > 7){
					this.classList.add("error")
					this.previousElementSibling.classList.add("error")
					hasError = true
					erreur.style.display = "block"
				}
				else{
					this.classList.remove("error")
					this.previousElementSibling.classList.remove("error")
					hasError = false
					erreur.style.display = "none"
				}
			}

			function inputPreVerif(donnee){
				if (donnee.value.match(regexInput) == null){
					donnee.classList.add("error")
					donnee.previousElementSibling.classList.add("error")
					hasError = true
					erreur.style.display = "block"
				}
			}
			function inputPreVerifNbr(donnee){
				if (donnee.value < 2 || donnee.value > 7){
					donnee.classList.add("error")
					donnee.previousElementSibling.classList.add("error")
					hasError = true
					erreur.style.display = "block"
				}
			}

			// Nom de la partie
			let nomInput = document.getElementById("nom")
			inputPreVerif(nomInput)
			nomInput.addEventListener("input", inputPostVerif)

			// Mot de passe
			let mdpInput = document.getElementById("mdp")
			inputPreVerif(mdpInput)
			mdpInput.addEventListener("input", inputPostVerif)

			// Nombre de joueurs
			let joueurInput = document.getElementById("nbrJ")
			inputPreVerifNbr(joueurInput)
			joueurInput.addEventListener("input", inputPostVerifNbr)

			// Si tous les tests sont validés, on envoie au back
			if (hasError == false)
				document.querySelector("form").submit()
		})
	}
}
</script>

<style scoped>
	/* Div principale */
	#app > div{
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		width: 100vw;
		height: 100vh;
		align-items: center;
	}

	/* Pays du joueur */
	#pays{
		display: flex;
		flex-direction: column;
		justify-content: space-evenly;
		align-items: center;
		border-radius: 10px;
		height: max-content;
		padding: 0 20px;
	}
	#pays > img{
		height: 128px;
		padding-top: 30px;
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

	/* Boîte de dialogue pour paramétrer la partie */
	#param{
		background-color: #2a3a49;
		border-radius: 10px;
		border-style: none;
		box-shadow: 0px 0px 15px 5px #002843;
		min-width: 35vw;
	}
	#param > h1{
		font-size: 40px;
		margin: 10px 0 30px;
		text-align: center;
	}
	#param > form{
		display: flex;
		flex-direction: column;
		margin: 0;
		align-items: center;
	}
	#param > form > div{
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		width: 80%;
	}
	#param > form > p{
		display: none;
		font-size: 20px;
		margin-bottom: 0;
		color: lightcoral;
		text-align: center;
	}
	#param > form > div > label{
		font-size: 25px;
		width: 49%;
		text-align: left;
	}
	input[type=number],
	input[type=password],
	input[type=text]{
		background-color: #3b5167;
		width: calc(50% - 10px);
		height: 30px;
		font-size: 25px;
		margin: 2px 0;
		padding: 0 5px;
		border-style: none;
		outline: none;
	}
	input[type=number]{
		text-align: right;
		caret-color: transparent;
		user-select: none;
		cursor: default;
	}
	#param > form > div > button,
	#param > form > div > input[type=submit]{
		flex-basis: 40%;
		margin: 30px 0 10px;
		padding: 4px 22px;
		line-height: 40px;
		border: none;
		outline: inherit;
	}
	input.error{
		background-color: rgba(255, 0, 0, 0.4);
	}

/* Version mobile */
@media screen and (max-width:769px){
	/* Pays du joueur */
	#pays{
		display: flex;
		flex-direction: column;
		justify-content: space-evenly;
		align-items: center;
		border-radius: 10px;
		height: max-content;
		padding: 0 20px;
	}
	#pays > img{
		height: 96px;
		padding-top: 20px;
	}
	#pays > p{
		font-size: 40px;
	}

	/* Boîte de dialogue pour paramétrer la partie */
	#param > h1{
		font-size: 30px;
	}
	#param > form > div{
		flex-direction: column;
		width: 90%;
		align-items: center;
	}
	#param > form > div > label{
		font-size: 25px;
		width: 100%;
		text-align: center;
	}
	#param > form > div > input{
		width: 100%;
		margin-bottom: 10px;
	}
	#param > form > div:last-child{
		flex-direction: row;
	}
	#param > form > div > button,
	#param > form > div > input[type=submit]{
		font-size: 25px;
	}
}
</style>