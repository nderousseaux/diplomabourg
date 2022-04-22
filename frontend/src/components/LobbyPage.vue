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
						<button id="fr" @click="ready()">Prêt</button>
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
					<button @click="copyLink()">Générer le lien</button>
					<button>Commencer la partie</button>
				</div>
			</div>
			<div id="chat">
				<h1>Chat</h1>
				<div id="historique"></div>
				<form name="message">
					<input type="text" name="msg" id="msg"
						placeholder="Entrez votre message"/>
				</form>
			</div>
		</div>


	</div>
	<dialog id="joindre">
		<h1>Joindre la partie</h1>
		<form method="dialog">
			<div>
				<label for="username">Username</label>
				<input maxlength="15" id="username" name="username"/>
				<label for="mdp">Mot de passe</label>
				<input type="password" maxlength="15" id="mdp" name="mdp"/>
			</div>
			<p>Tous les champs ne sont pas complétés correctement</p>
			<div>
				<input type="submit" value="Joindre"/>
			</div>
		</form>
	</dialog>
</template>

<script>
import api from "../api.js"

const game_num = window.location.pathname.split('/')[2];

function getTokenCookie() {
	const value = `; ${document.cookie}`;
	const parts = value.split(`; token${game_num}=`);
	if (parts.length === 2) {
		return parts.pop().split(';').shift();
	}
}

export default
{
	data() {
		return {
			game_id: game_num,
			player_id: '',
			token: getTokenCookie(),
			username: ''
		}
	},
	methods: {
		joinGame(mdp, username) {
			api
				.post("/games/" + this.game_id + "/players?password=" + mdp.value, {username: username.value})
				.then(response => {
					console.log(response);
					this.player_id = response.data.game.players[response.data.game.players.length - 1].id;
					console.log(this.player_id);
					document.cookie = `token${response.data.game.id}=` + response.data.token + "; sameSite=Lax";
					let ok_close = document.getElementById("joindre");
					ok_close.close();
				})
				.catch(function(error) {
					console.log(error);
					if (error.response.status == 400) {
						console.log(error.response.data.error.message[0]);
					}
				})
		},
		copyLink() {
			var link = `http://localhost:8080/games/${this.game_id}`;
			navigator.clipboard.writeText(link);
			alert("Copied : " + link);
		},
		ready() {
			console.log(this.game_id);
			console.log(this.player_id);
			console.log(this.token);

			const config = {
				headers: { Authorization: `Bearer ${this.token}`}
			};

			const bodyParameters = {
				username: this.username,
				power_id: 1,
				is_ready: true
			};

			api
				.put("/games/" + this.game_id + "/players/" + this.player_id,
					bodyParameters,
					config
				)
				.then(response => {
					console.log(response);
					if (response.status == 204) {
						document.getElementById("fr").classList.add("inactif");
						console.log("France is ready");
					}
				})
				.catch((err) => {
					console.log(err);
				})
		}
	},
	mounted()
	{
		// Pour paramétrer la partie
		let lancerDiag = document.getElementById("joindre")
		let erreur = document.querySelector("form > p")

		var cookie = this.token;
		//récupère l'id de l'utilisateur courant
		if (cookie == null) {
			lancerDiag.showModal()
		}
		else {
			const config = {
				headers: {Authorization: `Bearer ${cookie}`}
			};
			var indexOfPlayer;
			api
				.get("/games/" + window.location.pathname.split('/')[2], config)
				.then(response => {
					indexOfPlayer = response.data.players.map(function(e) {
						return e.is_you;
					}).indexOf(true)
					this.player_id = response.data.players[indexOfPlayer].id
					this.username = response.data.players[indexOfPlayer].username
					console.log(response);
				})
				.catch(function(error) {
					console.log(error);
				})
			}


		// Gestion du formulaire
		document.querySelector("form > div > input[type=submit]")
		.addEventListener("click", event =>
		{
			event.preventDefault()
			let erreurForm = false

			// Regex
			const regexInput = /^[\S\s]{5,15}$/

			// Fonction de vérification
			const inputPostVerif = function()
			{
				if (this.value.match(regexInput) == null)
				{
					this.classList.add("erreur")
					this.previousElementSibling.classList.add("erreur")
					erreurForm = true
					erreur.style.display = "block"
				}
				else
				{
					this.classList.remove("erreur")
					this.previousElementSibling.classList.remove("erreur")
					erreurForm = false
					if (document.querySelectorAll("input.erreur").length == 0)
						erreur.style.display = "none"
				}
			}

			function inputPreVerif(donnee)
			{
				if (donnee.value.match(regexInput) == null)
				{
					donnee.classList.add("erreur")
					donnee.previousElementSibling.classList.add("erreur")
					erreurForm = true
					erreur.style.display = "block"
				}
			}

			// Mot de passe
			let mdpInput = document.getElementById("mdp");
			let usernameInput = document.getElementById("username");
			inputPreVerif(mdpInput);
			mdpInput.addEventListener("input", inputPostVerif)

			// Si tous les tests sont validés, on peut envoyer
			if (erreurForm == false)
				this.joinGame(mdpInput, usernameInput)
		})

		// Action effectuée quand on appuie sur "Entrer" dans le chat
		let texte = document.querySelector("input[type=text]")
		document.querySelector("form").onkeypress = function(e)
		{
			if (e.key === "Enter")
			{
				e.preventDefault()
				if (texte.value != "")
				{
					// Récupérer le pseudo là dedans
					var pseudo = "Patrick"

					// Créer le message
					var para = document.createElement("p")
					var contenu = document.createTextNode(pseudo + " : " +
						texte.value)
					para.appendChild(contenu)
					para.style.textAlign = "left"
					para.style.margin = "0"

					// Changer la couleur du joueur en fonction du pays
					para.style.color = "wheat"

					let historique = document.getElementById("historique")
					historique.appendChild(para)

					// Réinitialiser l'input et afficher le dernier message
					texte.value = ""
					historique.scrollTop = historique.scrollHeight
				}
			}
		}

		// Affiche ou masque l'historique et l'input
		var $ = require("jquery")
		document.querySelector("#chat > h1").addEventListener("click", () =>
		{
			if (window.innerWidth < 769)
			{
				$(document.getElementById("historique")).slideToggle(100)
				$(document.getElementsByTagName("form")[0]).slideToggle(100)
				$(document.querySelector("#chat > h1")).toggleClass("bas")
			}
		})
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
		height: calc(100vh - 203px);
	}

	/* Chat */
	#chat{
		width: calc(25vw - 10px);
		height: calc(100vh - 223px);
	}
	#chat > h1{
		line-height: 64px;
		margin: 0;
		text-align: center;
	}
	#historique{
		border-style: solid;
		border-width: 4px 0 0;
		border-image: radial-gradient(#ae0132, #1c0043) 1;
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
@media screen and (max-width: 1370px){
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
@media screen and (max-width: 769px){
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
