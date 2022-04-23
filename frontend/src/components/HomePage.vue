<template>
	<div>
		<img
			id="logo"
			alt="Logo Diplomabourg"
			title="Logo Diplomabourg"
			src="../assets/img/logo.png"
		/>
		<div id="pays">
			<img
				alt="Drapeau français"
				title="Drapeau français"
				src="../assets/img/flags/france.png"
			/>
			<p>France</p>
		</div>
		<button>Créer une partie</button>
	</div>
	<dialog id="param">
		<h1>Paramètres de la partie</h1>
		<form method="dialog">
			<div>
				<label for="nom">Nom de la partie</label>
				<input type="text" id="nom" maxlength="15" name="nom" />
			</div>
			<div>
				<label for="nbrJ">Nombre de joueurs</label>
				<input type="number" id="nbrJ" name="nbrJ" min="2" max="7" value="7" />
			</div>
			<div>
				<label for="mdp">Mot de passe</label>
				<input type="password" maxlength="15" id="mdp" name="mdp" />
			</div>
			<p>Tous les champs ne sont pas complétés correctement</p>
			<div>
				<button>Annuler</button>
				<input type="submit" value="Créer" />
			</div>
		</form>
	</dialog>
</template>

<script>
import api from "../api.js";
import store from "../store.js"

export default {
  data() {
    return {
      game_id: '',
      player_id: ''
    }
  },
  methods: {
    storeGameId(id) {
      store.setGameId(Number(id))
    },
    storePlayerId(id) {
      store.setPlayerId(Number(id))
    },
    storeToken(token) {
      store.setToken(token)
    },
    storeJeu(jeu) {
      store.setJeu(jeu)
    }
  },
  mounted() {
    // Pour paramétrer la partie
    let paramBtn = document.querySelector("div:first-child > button");
    let lancerDiag = document.getElementById("param");
    let erreur = document.querySelector("form > p");

		// Ouvrir le formulaire
		paramBtn.addEventListener("click", function onOpen() {
			if (typeof lancerDiag.showModal === "function") {
				erreur.style.display = "none";
				lancerDiag.showModal();
			}
		});

		// Gestion du formulaire
		document
			.querySelector("form > div > input[type=submit]")
			.addEventListener("click", (event) => {
				event.preventDefault();
				let erreurForm = false;

				// Regex
				const regexInput = /^[\S\s]{5,15}$/;

				// Valeurs de tests
				let minJoueurs = 2;
				let maxJoueurs = 7;

				// Fonction de vérification
				const inputPostVerif = function () {
					if (this.value.match(regexInput) == null) {
						this.classList.add("erreur");
						this.previousElementSibling.classList.add("erreur");
						erreurForm = true;
						erreur.style.display = "block";
					} else {
						this.classList.remove("erreur");
						this.previousElementSibling.classList.remove("erreur");
						erreurForm = false;
						if (document.querySelectorAll("input.erreur").length == 0)
							erreur.style.display = "none";
					}
				};
				const inputPostVerifNbr = function () {
					if (this.value < minJoueurs || this.value > maxJoueurs) {
						this.classList.add("erreur");
						this.previousElementSibling.classList.add("erreur");
						erreurForm = true;
						erreur.style.display = "block";
					} else {
						this.classList.remove("erreur");
						this.previousElementSibling.classList.remove("erreur");
						erreurForm = false;
						if (document.querySelectorAll("input.erreur").length == 0)
							erreur.style.display = "none";
					}
				};

				function inputPreVerif(donnee) {
					if (donnee.value.match(regexInput) == null) {
						donnee.classList.add("erreur");
						donnee.previousElementSibling.classList.add("erreur");
						erreurForm = true;
						erreur.style.display = "block";
					}
				}
				function inputPreVerifNbr(donnee) {
					if (donnee.value < 2 || donnee.value > 7) {
						donnee.classList.add("erreur");
						donnee.previousElementSibling.classList.add("erreur");
						erreurForm = true;
						erreur.style.display = "block";
					}
				}

				// Nom de la partie
				let nomInput = document.getElementById("nom");
				inputPreVerif(nomInput);
				nomInput.addEventListener("input", inputPostVerif);

				// Mot de passe
				let mdpInput = document.getElementById("mdp");
				inputPreVerif(mdpInput);
				mdpInput.addEventListener("input", inputPostVerif);

				// Nombre de joueurs
				let joueurInput = document.getElementById("nbrJ");
				inputPreVerifNbr(joueurInput);
				joueurInput.addEventListener("input", inputPostVerifNbr);

				// Si tous les tests sont validés, on peut envoyer
				if (erreurForm == false) {
					document.querySelector("form").submit();

					var username = "FRANCE";
					var game_name = nomInput.value;
					var game_password = mdpInput.value;
					var map_id = 1;

					console.log(game_name);
					console.log(game_password);

					const player = { username: `${username}` };

					const game = {
						name: `${game_name}`,
						password: `${game_password}`,
						map_id: `${map_id}`,
					};

          const jeu = {
            player: player,
            game: game,
          };

          this.storeJeu(jeu);

          api
            .post("/games", jeu)
            .then(response => {
              //store les infos utiles de la game dans un objet pour le récup dans le lobby
              this.storeGameId(response.data.game.id);
              this.storePlayerId(response.data.game.players[0].id);
              this.storeToken(response.data.token);
            })
            .then((data) => {
              this.$router.push({ name: "Lobby" });
              var token = data.data.token;
              document.cookie = "session_game=" + token;
							document.cookie = `token${data.data.game.id}=` + data.data.token + "; sameSite=Lax";
							this.$router.push({ path: `/games/${data.data.game.id}` });
            })
            .catch((err) => {
              if (err.response.status == 400) {
                var err_name;
                var err_pwd;

                if (err.response.data.error.message[0].game.name) {
                  err_name = err.response.data.error.message[0].game.name[0];
                  console.log(err_name);
                }
                if (err.response.data.error.message[0].game.password) {
                  err_pwd = err.response.data.error.message[0].game.password[0];
                  console.log(err_pwd);
                }
              } else if (err.response.status == 500) {
                console.log(err.response.data);
              } else {
                console.log("ERREUR INCONNUE");
              }
            });
        }
      });
  },
};
</script>

<style scoped>
/* Div principale */
#app > div {
	display: flex;
	flex-direction: column;
	justify-content: space-between;
	width: 100vw;
	height: 100vh;
	align-items: center;
}

/* Pays du joueur */
#pays {
	display: flex;
	flex-direction: column;
	justify-content: space-evenly;
	align-items: center;
	border-radius: 10px;
	height: max-content;
	padding: 0 20px;
}
#pays > img {
	height: 128px;
	padding-top: 30px;
}
#pays > p {
	font-size: 80px;
	margin: 0;
	font-weight: bold;
	background-image: linear-gradient(0.25turn, #002843, #800124);
	-webkit-background-clip: text;
	-moz-background-clip: text;
	-webkit-text-fill-color: transparent;
	-moz-text-fill-color: transparent;
}

/* Boîte de dialogue pour paramétrer la partie */
#param {
	min-width: 35vw;
}
input[type="number"] {
	text-align: center;
	caret-color: transparent;
	user-select: none;
	cursor: default;
}

/* Version mobile */
@media only screen and (max-width: 769px){
	/* Pays du joueur */
	#pays {
		display: flex;
		flex-direction: column;
		justify-content: space-evenly;
		align-items: center;
		border-radius: 10px;
		height: max-content;
		padding: 0 20px;
	}
	#pays > img {
		height: 96px;
		padding-top: 20px;
	}
	#pays > p {
		font-size: 40px;
	}

	/* Boîte de dialogue pour paramétrer la partie */
	#param > h1 {
		font-size: 30px;
	}
	#param > form > div {
		flex-direction: column;
		width: 90%;
		align-items: center;
	}
	#param > form > div > label {
		font-size: 25px;
		width: 100%;
		text-align: center;
	}
	#param > form > div > input {
		width: 100%;
		margin-bottom: 10px;
	}
	#param > form > div:last-child {
		flex-direction: row;
	}
	#param > form > div > button,
	#param > form > div > input[type="submit"] {
		font-size: 25px;
	}
}
</style>
