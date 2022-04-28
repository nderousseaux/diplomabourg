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
        alt="Drapeau français"
        title="Drapeau français"
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
      <p>Tous les champs ne sont pas complétés correctement</p>
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
				<input type="submit" value="Rejoindre"/>
			</div>
		</form>
	</dialog>
  <dialog id="telecharger">
    <h1>Télécharger le jeu</h1>
    <form method="dialog">
      <div>
        <h2>MacOS</h2>
        <a href="/installers/Diplomabourg-0.1.0-arm64.dmg" download>MacOS ARM</a>
        <a href="/installers/Diplomabourg-0.1.0-arm64.dmg" download>MacOS x64</a>
      </div>
      <div>
        <h2>Windows</h2>
        <a href="/installers/Diplomabourg-0.1.0-arm64.dmg" download>Windows x64</a>
        <a href="/installers/Diplomabourg-0.1.0-arm64.dmg" download>Windows x86</a>
      </div>
      <div>
        <h2>Linux</h2>
        <a href="/installers/Diplomabourg-0.1.0-arm64.dmg" download>Linux x64</a>
        <a href="/installers/Diplomabourg-0.1.0-arm64.dmg" download>Linux x86</a>
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
    },
  },
  mounted() {
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
        const regexInputRjd = /^\d+$/;

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
          document.querySelector("form").submit();
          console.log("ok");
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
            erreurCreer.style.display = "block";
          }
        }
        function inputPreVerifNbr(donnee) {
          if (donnee.value < minJoueurs || donnee.value > maxJoueurs) {
            donnee.classList.add("erreur");
            donnee.previousElementSibling.classList.add("erreur");
            erreurForm = true;
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
          document.querySelector("form").submit();

          const player = { username: "FRANCE" };

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

              console.log(response);
              this.$router.push({ name: "Lobby" });
              var token = response.data.token;
              document.cookie = "session_game=" + token;
            })
            .catch((err) => {
              console.log(err);
              if (err.status == 400) {
                var err_name;
                var err_pwd;
                console.log(err.response.data);

                if (err.response.data.error.message[0].game.name) {
                  err_name = err.response.data.error.message[0].game.name[0];
                  console.log(err_name);
                }
                if (err.response.data.error.message[0].game.password) {
                  err_pwd = err.response.data.error.message[0].game.password[0];
                  console.log(err_pwd);
                }
              } else if (err.status == 500) {
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

/* Télécharger le jeu */
#bandeau{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  width: 100vw;
}
#bandeau > button{
  width: 15%;
  height: max-content;
}
#bandeau::before{
  content: "";
  width: 15%;
}

#telecharger{
  min-width: 25vw;
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
#param,
#rejoindre {
  min-width: 35vw;
}

input[type="number"] {
  text-align: center;
  caret-color: transparent;
  user-select: none;
  cursor: default;
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
		font-size: 22px;
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
  #param,
  #rejoindre {
    width: 80vw;
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
		text-align: center;
	}
	#param > form > div > input,
  #rejoindre > form > div > input {
		width: calc(100% - 10px);
		margin-bottom: 10px;
	}
	#param > form > div:last-child,
  #rejoindre > form > div:last-child{
		flex-direction: row;
	}

  /* Boutons */
  #actions{
    width: 90vw;
    display: flex;
    flex-direction: column;
  }
  #actions > button{
    font-size: 22px;
    width: 100%;
    margin-top: 0;
  }
}
</style>