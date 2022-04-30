<template>
	<div>
		<img id="logo" alt="Logo Diplomabourg" title="Logo Diplomabourg"
			src="../assets/img/logo.png"/>
		<div>
			<div id="lobby">
				<div id="joueurs">
					<div>
						<img alt="Drapeau français" title="Drapeau français"
							:src="getImgFlagUrl('france')"/>
						<button id="fr" @click="ready()">Prêt</button>
					</div>
					<div>
						<img alt="Drapeau allemand" title="Drapeau allemand"
							:src="getImgFlagUrl('germany')"/>
						<button class="inactif">Prêt</button>
					</div>
					<div>
						<img value="2" alt="Attente du joueur" title="Attente du joueur"
							:src="getImgFlagUrl('loading')"/>
					</div>
					<div>
						<img value="3" alt="Attente du joueur" title="Attente du joueur"
							:src="getImgFlagUrl('loading')"/>
					</div>
					<div>
						<img value="4" alt="Attente du joueur" title="Attente du joueur"
							:src="getImgFlagUrl('loading')"/>
					</div>
					<div>
						<img value="5" alt="Attente du joueur" title="Attente du joueur"
							:src="getImgFlagUrl('loading')"/>
					</div>
					<div>
						<img value="6" alt="Attente du joueur" title="Attente du joueur"
							:src="getImgFlagUrl('loading')"/>
					</div>
				</div>
				<div id="actions">
					<button id="test" @click="copyLink()">Générer le lien</button>
					<button id="beginGame" @click="beginGame()">Commencer la partie</button>
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
				<label for="username">Pseudo</label>
				<input type="text" maxlength="15" id="username" name="username"/>
			</div>
			<div>
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
import api from "../api";
import router from "../router/index.js";
/*import { io } from "socket.io-client";
var socket;
*/
const game_num = window.location.pathname.split('/')[2];
/*
function getGameId() {
	const value = `; ${document.cookie}`;
	const parts = value.split("; game_id=");
	if (parts.length === 2) {
		return parts.pop().split(";").shift();
	}
}
*/
function getTokenCookie() {
	const value = `; ${document.cookie}`;
	const parts = value.split(`; token${game_num}=`);
	if (parts.length === 2) {
		return parts.pop().split(';').shift();
	}
}

function getRefresh()  {
	const value = `; ${document.cookie}`;
	const parts = value.split(`; refreshed=`);
	return parts.pop().split(';').shift();
}

export default
{
	data() {
		return {
			game_id: game_num,
			player_id: '',
			token: getTokenCookie(),
			username: '',
			//is_admin: false
		}
	},
	methods: {
		getChange(game_id, config) {
			api.games
				.get_game(game_id, config)
				.then(response => {
					console.log(response.data);
					if (response.data.state == "GAME")
					{
						router.push({ name: "Jeu"});
					}
				})
				.catch(function(error) {
					console.log(error);
				})
		},

		beginGame() {
			const config = {
				headers: {Authorization: `Bearer ${this.token}`}
			}
			api.games
				.get_game(this.game_id, config)
				.then(response => {
					console.log(response.data);
					for (var player = 0; player < response.data.players.length; player++){
						console.log(player);
						var id = response.data.players[player].id;
						var username = response.data.players[player].username;
						var power_id = player + 1;

						api.players
							.update(this.game_id, id, username, power_id, true, config)
							.then(() => {
								console.log(username + ": ok");
							})
							.catch(function(error) {
								console.log(error);
							})
					}
					//router.push({ name: "Jeu"})
				})
				.catch(function(error) {
					console.log(error);
				})
		},
		joinGame(mdp, username) {
			api.games
				.join_game(username.value, window.location.pathname.split('/')[2], mdp.value)
				.then(response => {
					/*
					console.log(response);
					this.player_id = response.data.game.players[response.data.game.players.length - 1].id;
					console.log(this.player_id);*/
					document.cookie = `token${response.data.game.id}=` + response.data.token + "; sameSite=Lax";
					let ok_close = document.getElementById("joindre");
					ok_close.close();
					location.reload();
				})
				.catch(function(error) {
					console.log(error);
					if (error.response.status == 400) {
						console.log(error.response.data.error.message[0]);
					}
				})
		},
		copyLink() {
			var link = window.location.host + "/games/" + this.game_id;
			navigator.clipboard.writeText(link);
			alert("Lien copié : " + link);
		},
		ready() {
			console.log(this.game_id);
			console.log(this.player_id);
			console.log(this.token);

			const config = {
				headers: { Authorization: `Bearer ${this.token}`}
			};
			api.players
				.update(this.game_id, this.player_id, 'FRANCE', 1, true, config)
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
		},
		getImgFlagUrl: function(imgName) {
			return require('@/assets/img/flags/' + imgName + '.png');
		}
	},
	mounted()
	{
		// Pour paramétrer la partie
		let lancerDiag = document.getElementById("joindre")
		let erreur = document.querySelector("form > p")

		var cookie = getTokenCookie();

		var is_refreshed = getRefresh();
		//récupère l'id de l'utilisateur courant
		if (cookie == null) {
			if (is_refreshed == 'true') {
				lancerDiag.showModal();
			}
			else {
				var expiration = new Date(Date.now() + 10000).toUTCString();
				document.cookie = `refreshed=true; expires=${expiration}; sameSite=Lax`
				location.reload();
			}
		}
		else {
			const config = {
				headers: {Authorization: `Bearer ${cookie}`}
			};

			setInterval(this.getChange, 5000, game_num, config);
			/*
			socket = io("http://localhost:8080",
				{path: "/backend/"},
			//socket = io("http://127.0.0.1:6543",
				{ auth: cookie }
			);
			socket.on('ping', () => {
				console.log("game update")
			})
			*/

			var indexOfPlayer;
			api.games
				.get_game(this.game_id, config)
				.then(response => {
					indexOfPlayer = response.data.players.map(function(e) {
						return e.is_you;
					}).indexOf(true)
					/*
					if (indexOfPlayer == 0) {
						this.is_admin = true;
					}
					*/
					this.player_id = response.data.players[indexOfPlayer].id
					this.username = response.data.players[indexOfPlayer].username
					console.log("player_id : " + this.player_id);
				})
				.catch(function(error) {
					console.log(error);
				})
		}
		/*
		if (this.is_admin == false) {
			document.getElementById("beginGame").disabled = true;
		}
		*/

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

			// Nom de la partie
			let pseudoJr = document.getElementById("username");
			inputPreVerif(pseudoJr);
			pseudoJr.addEventListener("input", inputPostVerif);

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
					// Récupérer le username là dedans
					var username = "Patrick"

					// Créer le message
					var para = document.createElement("p")
					var contenu = document.createTextNode(username + " : " +
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


		// Créé la liste des div "en attente"
		let imgAttente = []
		document.querySelectorAll("#joueurs > div > img").forEach(element =>
		{
			var valeur = element.getAttribute("value")
			if (valeur != undefined)
				imgAttente.push(element)
		})
		console.log(imgAttente)

		// Récupère le premier élément de la liste à modifier
		var imgRejoins = imgAttente.shift()

		// Le modifie par le nouveau drapeau (le nom du pays est renvoyé par le back [?])
		let nomPaysBack = 'russia'
		imgRejoins.setAttribute("src", this.getImgFlagUrl(nomPaysBack))
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
		height: calc(100vh - 201px);
	}

	/* Chat */
	#chat{
		width: calc(25vw - 10px);
		height: calc(100vh - 221px);
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
		margin: auto;
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
		width: 138px;
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
		width: 30%;
		padding: 0 10px;
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

	/* Boîte de dialogue */
	#joindre{
		width: max-content;
	}
	#joindre > form > div:last-child{
		justify-content: center;
	}

/* Version tablette */
@media only screen and (max-width: 1370px){
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
	#joueurs > div > button{
		margin-bottom: 0;
		width: 108px
	}

	/* Bouton */
	#actions{
		justify-content: space-between;
		width: 100%;
		margin-top: 5vh;
	}
	#actions > button{
		width: 40%;
	}
}

/* Version mobile */
@media only screen and (max-width: 769px){
	/* Div principale */
	#lobby{
		height: calc(80vh - 201px)
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
