<template>
	<div>
		<img id="logo" alt="Logo Diplomabourg" title="Logo Diplomabourg"
			src="../assets/img/logo.png"/>
		<div>
			<div id="chat">
				<h1>Chat</h1>
				<div id="historique"></div>
				<form name="message">
					<input type="text" name="msg" id="msg"
						placeholder="Entrez votre message"/>
				</form>
			</div>
			<div id="lobby">
				<div id="joueurs">
					<div>
						<img alt="Drapeau de la France" title="France"
							:src="getImgFlagUrl('france')"/>
						<button v-if="this.username == 'France'" id="ready" @click="ready()">Prêt</button>
					</div>
					<div>
						<img alt="Drapeau de l'Allemagne" title="Allemagne"
							:src="getImgFlagUrl('germany')"/>
						<button v-if="this.username == 'Germany'" id="ready" @click="ready()">Prêt</button>
					</div>
					<div>
						<img alt="Drapeau d'Italie" title="Italie"
							:src="getImgFlagUrl('italy')"/>
						<button v-if="this.username == 'Italy'" id="ready" @click="ready()">Prêt</button>
					</div>
					<div>
						<img alt="Drapeau de Russie" title="Russie"
							:src="getImgFlagUrl('russia')"/>
						<button v-if="this.username == 'Russia'" id="ready" @click="ready()">Prêt</button>
					</div>
					<div>
						<img alt="Drapeau de Turquie" title="Turquie"
							:src="getImgFlagUrl('turkey')"/>
						<button v-if="this.username == 'Turkey'" id="ready" @click="ready()">Prêt</button>
					</div>
					<div>
						<img alt="Drapeau du Royaume-Uni" title="Royaume-Uni"
							:src="getImgFlagUrl('great-britain')"/>
						<button v-if="this.username == 'Great-Britain'" id="ready" @click="ready()">Prêt</button>
					</div>
					<div>
						<img alt="Drapeau d'Autriche" title="Autriche"
							:src="getImgFlagUrl('austria-hungary')"/>
						<button v-if="this.username == 'Austria-Hungary'" id="ready" @click="ready()">Prêt</button>
					</div>
				</div>
				<div id="actions">
					<button id="test" @click="copyLink()">Générer le lien</button>
					<button v-if="this.username == 'France'" id="beginGame" @click="beginGame()">Commencer la partie</button>
				</div>
			</div>
		</div>
	</div>
	<dialog id="joindre">
		<h1>Joindre la partie</h1>
		<form method="dialog">
			<div>
				<label for="username">Pays souhaité</label>
				<select name="country" id="username">
					<option value="Germany">Allemagne</option>
					<option value="Russia">Russie</option>
					<option value="Austria-Hungary">Autriche</option>
					<option value="Turkey">Turquie</option>
					<option value="Great-Britain">Royaume-Uni</option>
					<option value="Italy">Italie</option>
				</select>
			</div>
			<div>
				<label for="mdp">Mot de passe</label>
				<input type="password" maxlength="15" id="mdp" name="mdp"/>
			</div>
			<p></p>
			<div>
				<input type="submit" value="Joindre"/>
			</div>
		</form>
	</dialog>
	<dialog id="lienCopie">
		<h1>Lien de la partie</h1>
		<form method="dialog">
			<div>
			</div>
			<div>
				<button>Fermer</button>
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

var interId;

export default
{
	data() {
		return {
			game_id: game_num,
			player_id: '',
			token: getTokenCookie(),
			username: '',
			power_id: ''
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
						clearInterval(interId)
						document.getElementById("app").style.cursor = "default";
						// router.push({ name: "Jeu"});
						router.push({ path: `/jeu/${response.data.id}` })
					}
				})
				.catch(function(error) {
					console.log(error);
				})
		},

		beginGame() {
			document.getElementById("app").style.cursor = "progress";
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
					let erreur = document.querySelector("#joindre > form > p")
					if (error.response.status == 400) {
						console.log(error.response.data.error.message[0]);
						erreur.innerText = "Le pays est déjà sélectionné"
						erreur.style.display = "block"
					}
					else if (error.response.status == 401) {
						console.log(error.response.data.error.message[0]);
						erreur.innerText = "Le mot de passe est incorrect"
						erreur.style.display = "block"
					}
					else if (error.response.status == 410) {
						console.log(error.response.data.error.message[0]);
						erreur.innerText = "La partie est déjà en cours"
						erreur.style.display = "block"
					}
				})
		},
		copyLink() {
			var link = window.location.host + "/lobby/" + this.game_id;
			navigator.clipboard.writeText(link);
			document.querySelector("#lienCopie > form > div").innerHTML = "Copié dans le presse-papier :\n" + link
			document.getElementById("lienCopie").showModal();
		},
		ready() {
			console.log(this.game_id);
			console.log(this.player_id);
			console.log(this.token);

			const config = {
				headers: { Authorization: `Bearer ${this.token}`}
			};
			api.players
				.update(this.game_id, this.player_id, this.username, this.power_id, true, config)
				.then(response => {
					console.log(response);
					if (response.status == 204) {
						document.getElementById("ready").classList.add("inactif");
						console.log(this.username + " is ready");
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
				lancerDiag.addEventListener("cancel", (event) => {
					event.preventDefault();
				});

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

			interId = setInterval(this.getChange, 5000, game_num, config);
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
					this.player_id = response.data.players[indexOfPlayer].id;
					this.username = response.data.players[indexOfPlayer].username;

					switch (this.username) {
						case 'France':
							this.power_id = 3;
							break;
						case 'Germany':
							this.power_id = 1;
							break;
						case 'Russia':
							this.power_id = 6;
							break;
						case 'Austria-Hungary':
							this.power_id = 2;
							break;
						case 'Great-Britain':
							this.power_id = 4;
							break;
						case 'Italy':
							this.power_id = 5;
							break;
						case 'Turkey':
							this.power_id = 7;
							break;
						default:
							console.log("erreur pseudo");
					}
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
					if (donnee.value == mdpInput.value)
					{
						erreur.innerText = "Les champs ne sont pas correctement complétés"
					}
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
		margin: 0 0 0 10px;
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

	/* Boîtes de dialogue */
	#joindre > form > div:last-child{
		justify-content: center;
	}
	select{
		width: 50%;
		border-radius: 0;
		text-align: center;
		-webkit-appearance: none;
	}
	#lienCopie > h1{
		margin: 10px 20px 30px;
	}

	/* Régler bug de Safari 11 */
	@media not all and (min-resolution:.001dpcm) {
		@supports (-webkit-appearance:none) and (stroke-color:transparent) {
			select:active {
				font-size: 18px;
			}
		}
	}
	option{
		font-family: "Iceland";
		font-size: 20px;
	}

/* Version tablette */
@media only screen and (max-width: 1370px){
	/* Div principale */
	#app > div > div{
		flex-direction: column;
		align-items: center;
		justify-content: space-evenly;
	}
	#lobby{
		width: 80vw;
		height: calc(100vh - 201px - 33vh);
	}

	/* Chat */
	#chat{
		width: 80vw;
		height: 30vh;
		margin: 3vh 0 0 0;
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
		width: 100%;
	}
	#actions > button{
		width: 40%;
	}

	/* Boîte de dialogue */
	#lienCopie > h1{
		margin: 10px 30px 30px;
	}
}

/* Version mobile */
@media only screen and (max-width: 769px){
	/* Div principale */
	#lobby{
		width: calc(100vw - 2vw - 2vw);
		height: calc(100vh - 168px - 25vh);
	}

	/* Chat */
	#chat{
		width: calc(100vw - 2vw - 2vw);
		margin-bottom: 20px;
	}

	/* Bouton */
	#actions{
		margin-top: unset;
		width: 80%;
	}
	#actions > button{
		width: 100%;
	}
	#actions > button:first-child{
		margin-bottom: 0;
	}
}
</style>
