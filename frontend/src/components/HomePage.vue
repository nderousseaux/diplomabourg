<template>
  <div>
    <div id="bandeau">
      <img
        id="logo"
        alt="Logo Diplomabourg"
        title="Logo Diplomabourg"
        src="../assets/img/logo.png"
      />
      <button>Télécharger</button>
    </div>
    <div id="pays">
      <img
        alt="Drapeau de la France"
        title="France"
        src="../assets/img/flags/france.png"
      />
      <p>France</p>
    </div>
    <div id="actions">
      <button>Créer une partie</button>
      <button>Rejoindre une partie</button>
    </div>
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
      <p></p>
      <div>
        <button>Annuler</button>
        <input type="submit" value="Créer" />
      </div>
    </form>
  </dialog>
  <dialog id="rejoindre">
		<h1>Rejoindre une partie</h1>
		<form method="dialog">
			<div>
				<label for="numPart">Numéro de partie</label>
				<input type="text" id="numPart" name="numPart"/>
			</div>
      <p>Le numéro de partie doit être supérieur à 0 et n'être composé que de chiffres !</p>
			<div>
        <button>Annuler</button>
        <input type="submit" value="Rejoindre" />
			</div>
		</form>
	</dialog>
  <dialog id="telecharger">
    <h1>Télécharger le jeu</h1>
    <form method="dialog">
      <div>
        <h2>MacOS</h2>
        <a href="../installers/Diplomabourg-1.0.0-arm.dmg" download>MacOS ARM</a>
        <a href="../installers/Diplomabourg-0.1.0.dmg" download>MacOS x64</a>
      </div>
      <div>
        <h2>Windows</h2>
        <a href="/installers/Diplomabourg-00-arm64.dmg" download>Windows x64</a>
      </div>
      <div>
        <h2>Linux</h2>
        <a href="/installers/Diplomabourg-0.1.0-arm64.dmg" download>Linux x64</a>
      </div>
      <button>Fermer</button>
    </form>
  </dialog>
</template>

<script>
import api from "../api";
import store from "../store.js";

export default {
  data() {
    return {
      game_id: "",
      player_id: "",
    };
  },
  methods: {
    storeGameId(id) {
      store.setGameId(Number(id));
    },
    storePlayerId(id) {
      store.setPlayerId(Number(id));
    },
    storeToken(token) {
      store.setToken(token);
    },
    storeJeu(jeu) {
      store.setJeu(jeu);
    }
  },
  mounted() {
    // Rejoindre une partie
    function rejoindreGame() {
      var id = document.getElementById('numPart')
      window.location = (window.location.origin + '/lobby/' + id.value)
    }
    // Liste des téléchargements
    let teleBtn = document.querySelector("#bandeau > button");

    // Masquer le bouton si on est déjà sur le logiciel
    var userAgent = navigator.userAgent.toLowerCase();
    if (userAgent.indexOf("electron/") > -1) {
      teleBtn.style.visibility = "hidden";
    }

    let lancerTele = document.getElementById("telecharger")
    teleBtn.addEventListener("click", function onOpen() {
      if (typeof lancerTele.showModal === "function") {
        lancerTele.showModal();
      }
    });

    // Formulaire pour rejoindre une partie
    let rejoindreBtn = document.querySelector("#actions > button:last-child");
    let lancerJoin = document.getElementById("rejoindre");
    let erreurJoin = document.querySelector("#rejoindre > form > p");

    rejoindreBtn.addEventListener("click", function onOpen() {
      if (typeof lancerJoin.showModal === "function") {
        lancerJoin.showModal();
      }
    });

    // Gestion du formulaire pour rejoindre une partie
    document
      .querySelector("#rejoindre > form > div > input[type=submit]")
      .addEventListener("click", (event) => {
        event.preventDefault();
        let erreurForm = false;

        // Regex
        const regexInputRjd = /^[1-9][0-9]*$/;

        const inputPostVerifNbrJr = function () {
          if (this.value.match(regexInputRjd) == null) {
            this.classList.add("erreur");
            this.previousElementSibling.classList.add("erreur");
            erreurForm = true;
            erreurJoin.style.display = "block";
          } else {
            this.classList.remove("erreur");
            this.previousElementSibling.classList.remove("erreur");
            erreurForm = false;
            if (document.querySelectorAll("input.erreur").length == 0)
              erreurJoin.style.display = "none";
          }
        };
        function inputPreVerifNbrJr(donnee) {
          if (donnee.value.match(regexInputRjd) == null) {
            donnee.classList.add("erreur");
            donnee.previousElementSibling.classList.add("erreur");
            erreurForm = true;
            erreurJoin.style.display = "block";
          }
        }

        // Nom de la partie
        let numPartie = document.getElementById("numPart");
        inputPreVerifNbrJr(numPartie);
        numPartie.addEventListener("input", inputPostVerifNbrJr);

        // Si tous les tests sont validés, on peut envoyer
        if (erreurForm == false) {
          rejoindreGame()
        }
      });


    // Formulaire pour paramétrer la partie
    let paramBtn = document
                  .querySelector("#actions > button:first-child");
    let lancerDiag = document.getElementById("param");
    let erreurCreer = document.querySelector("#param > form > p");

    // Ouvrir le formulaire
    paramBtn.addEventListener("click", function onOpen() {
      if (typeof lancerDiag.showModal === "function") {
        erreurCreer.style.display = "none";
        lancerDiag.showModal();
      }
    });

    // Gestion du formulaire pour créer une partie
    document
      .querySelector("#param > form > div > input[type=submit]")
      .addEventListener("click", (event) => {
        event.preventDefault();
        let erreurForm = false;

        // Valeurs de tests
        let minJoueurs = 2;
        let maxJoueurs = 7;
        let minCara = 5;
        let maxCara = 15;

        // Regex
        const regex = "^[\\S\\s]" + "{" + minCara + "," + maxCara + "}" + "$";
        const regexInput = new RegExp(regex);

        // Fonction de vérification
        const inputPostVerif = function () {
          if (this.value.match(regexInput) == null) {
            this.classList.add("erreur");
            this.previousElementSibling.classList.add("erreur");
            erreurForm = true;
            erreurCreer.innerText = "Les nom de la partie et le mot de passe doivent être composés de " + minCara + " à " + maxCara + " caractères";
            erreurCreer.style.display = "block";
          } else {
            this.classList.remove("erreur");
            this.previousElementSibling.classList.remove("erreur");
            erreurForm = false;
            if (document.querySelectorAll("input.erreur").length == 0)
              erreurCreer.style.display = "none";
          }
        };
        const inputPostVerifNbr = function () {
          if (this.value < minJoueurs || this.value > maxJoueurs) {
            this.classList.add("erreur");
            this.previousElementSibling.classList.add("erreur");
            erreurForm = true;
            erreurCreer.innerText = "Le nombre de joueurs doit être compris entre " + minJoueurs + " et " + maxJoueurs;
            erreurCreer.style.display = "block";
          } else {
            this.classList.remove("erreur");
            this.previousElementSibling.classList.remove("erreur");
            erreurForm = false;
            if (document.querySelectorAll("input.erreur").length == 0)
              erreurCreer.style.display = "none";
          }
        };

        function inputPreVerif(donnee) {
          if (donnee.value.match(regexInput) == null) {
            donnee.classList.add("erreur");
            donnee.previousElementSibling.classList.add("erreur");
            erreurForm = true;
            erreurCreer.innerText = "Les nom de la partie et le mot de passe doivent être composés de " + minCara + " à " + maxCara + " caractères";
            erreurCreer.style.display = "block";
          }
        }
        function inputPreVerifNbr(donnee) {
          if (donnee.value < minJoueurs || donnee.value > maxJoueurs) {
            donnee.classList.add("erreur");
            donnee.previousElementSibling.classList.add("erreur");
            erreurForm = true;
            erreurCreer.innerText = "Le nombre de joueurs doit être compris entre " + minJoueurs + " et " + maxJoueurs;
            erreurCreer.style.display = "block";
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
          // document.querySelector("form").submit();
          const player = { username: "France" };

          const game = {
            name: `${nomInput.value}`,
            password: `${mdpInput.value}`,
            map_id: 1,
          };

          const jeu = {
            player: player,
            game: game,
          };

          this.storeJeu(jeu);

          api.games
            .create_game(player.username, game.name, game.password, game.map_id)
            .then(response => {
              //store les infos utiles de la game dans un objet pour le récup dans le lobby
              this.storeGameId(response.data.game.id);
              this.storePlayerId(response.data.game.players[0].id);
              this.storeToken(response.data.token);

							document.cookie = `token${response.data.game.id}=` + response.data.token + "; sameSite=Lax";
							document.cookie = "game_id=" + response.data.game.id + "; sameSite=Lax";
							this.$router.push({ path: `/lobby/${response.data.game.id}` });
            })
            .catch((err) => {
              console.log(err)
              if (err.response.status == 400) {
                erreurCreer.innerText = "Le nom de la partie existe déjà"
                erreurCreer.style.display = "block"
              } else if (err.response.status == 500) {
                console.log(err.response.data);
              } else {
                console.log("Erreur inconnue");
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

/* Télécharger le jeu */
#bandeau{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  width: 100vw;
}
#bandeau > button,
#bandeau::before{
  width: 15%;
  margin-right: 20px;
}
#bandeau > button{
  height: max-content;
}
#bandeau::before{
  content: "";
}

#telecharger{
  min-width: 25vw;
  width: fit-content;
}
#telecharger > form > div{
  display: flex;
  flex-direction: column;
  align-items: center;
}
#telecharger > form > div > h2{
  font-size: 32px;
}
#telecharger > form > div:first-child > h2{
  margin-top: 0;
}
#telecharger > form > div > a{
  font-size: 18px;
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
  background-clip: text;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}

/* Boutons */
#actions{
  display: flex;
  justify-content: space-around;
  width: 45vw;
}
#actions > button{
  width: 45%;
}

/* Boîte de dialogue pour paramétrer et rejoindre la partie */
#param > form > div > label{
  margin-right: 10px;
  width: 50%;
}
input[type="number"] {
  text-align: center;
  caret-color: transparent;
  user-select: none;
  cursor: default;
}
input[type=number],
input[type=password],
input[type=text]{
	width: calc(50% - 20px);
}

/* Version tablette */
@media only screen and (min-width: 770px) and (max-width: 1370px){
  /* Télécharger le jeu */
  #bandeau > button,
  #bandeau::before{
    display: none;
  }
  #bandeau{
    justify-content: center;
  }

  /* Boutons */
  #actions{
    width: 80vw;
  }
  #actions > button{
		font-size: 26px;
  }
}

/* Version mobile */
@media only screen and (max-width: 769px){
  /* Télécharger le jeu */
  #bandeau > button,
  #bandeau::before{
    display: none;
  }
  #bandeau{
    justify-content: center;
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
    height: 96px;
    padding-top: 20px;
  }
  #pays > p {
    font-size: 40px;
  }

  /* Boîte de dialogue pour paramétrer et rejoindre la partie */
  #param{
    min-width: unset;
  }
	#param > form > div,
  #rejoindre > form > div {
		flex-direction: column;
		width: 90%;
		align-items: center;
	}
	#param > form > div > label,
  #rejoindre > form > div > label {
		font-size: 25px;
		width: 100%;
    margin: 0;
		text-align: center;
	}
	#param > form > div > input,
  #rejoindre > form > div > input {
		width: calc(100% - 10px);
		margin-bottom: 10px;
	}
	#param > form > div:last-child,
  #rejoindre > form > div:last-child{
		flex-direction: column;
	}
  #param > form > div:last-child > button,
  #param > form > div:last-child > input[type=submit],
  #rejoindre > form > div:last-child > button{
    width: 60%;
	}
  #param > form > div:last-child > input[type=submit],
  #rejoindre > form > div:last-child > button:last-child{
    margin-top: 10px;
  }

  /* Boutons */
  #actions{
    width: 90vw;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  #actions > button{
    font-size: 22px;
    width: 80%;
    margin-top: 0;
  }
}
</style>
