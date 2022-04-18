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
        <input type="text" id="nom" name="nom" />
      </div>
      <div>
        <label for="nbrJ">Nombre de joueurs</label>
        <input
          type="number"
          onkeydown="return false"
          id="nbrJ"
          name="nbrJ"
          min="2"
          max="7"
          value="7"
        />
      </div>
      <div>
        <label for="mdp">Mot de passe</label>
        <input type="password" id="mdp" name="mdp" />
      </div>
      <p>Tous les champs ne sont pas complétés</p>
      <div>
        <button>Annuler</button>

        <input type="submit" value="Créer" />
      </div>
    </form>
  </dialog>
</template>

<script>
import api from "../api.js";
import store from "../store.js";

export default {
  data() {
    return {
      game_id: ''
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
      .querySelector("input[type=submit]")
      .addEventListener("click", (event) => {
        event.preventDefault();
        var form = event.target.form;

        // Si le formulaire n'est pas complet
        if (form["nom"].value === "" || form["mdp"].value === "") {
          console.log("Erreur");
          erreur.style.display = "block";
        }

        // Si l'utilisateur a modifié l'HTML
        else if (form["nbrJ"].value < 2 || form["nbrJ"].value > 7) {
          erreur.innerText =
            "Le nombre de joueurs doit être compris\
						entre 2 et 7";
          erreur.style.display = "block";
        }

        // Sinon on peut envoyer au back
        else {
          erreur.style.display = "none";

          var username = "FRANCE";
          var game_name = form["nom"].value;
          var game_password = form["mdp"].value;
          var map_id = 1;

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
              //store l'id de la game dans un objet pour le récuperer depuis le lobby
              this.game_id = response.data.game.id;
              this.storeGameId(this.game_id);

              //pareil pour l'id du joueur
              this.player_id = response.data.game.players[0].id;
              this.storePlayerId(this.player_id);

              //enregistre le token reçu
              this.storeToken(response.data.token);
              api.defaults.headers.common['Authorization'] = response.data.token;
            })
            .then(() => {
              this.$router.push({ path: `/games/${this.game_id}` });
            })
            .catch((err) => {
              console.log(err);
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
  background: url("../assets/img/map.jpeg");
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100vw;
  height: 100vh;
  align-items: center;
}
#logo {
  width: 430px;
  height: 163px;
  margin: 20px 0;
}

/* Pays du joueur */
#pays {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  background-color: rgba(42, 58, 73, 0.7);
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

/* Bouton */
button,
input[type="submit"] {
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
input[type="submit"]:hover {
  background-color: #4682b4;
}
button:active,
input[type="submit"]:active {
  background-color: #376890;
}

/* Boîte de dialogue pour paramétrer la partie */
#param {
  background-color: #2a3a49;
  border-radius: 10px;
  border-style: none;
  box-shadow: 0px 0px 15px 5px #002843;
  min-width: 35vw;
}
#param > h1 {
  color: #ffffff;
  font-size: 40px;
  margin: 10px 0 30px;
  text-align: center;
}
#param > form {
  display: flex;
  flex-direction: column;
  margin: 0;
  align-items: center;
}
#param > form > div {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 80%;
}
#param > form > p {
  display: none;
  font-size: 20px;
  color: lightcoral;
  margin-bottom: 0;
  text-align: center;
}
#param > form > div > label {
  color: #ffffff;
  font-size: 25px;
  width: 49%;
  text-align: left;
}
input[type="number"],
input[type="password"],
input[type="text"] {
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
input[type="number"] {
  text-align: right;
  caret-color: transparent;
  user-select: none;
  cursor: default;
}
#param > form > div > button,
#param > form > div > input[type="submit"] {
  padding: 4px 22px;
  border: none;
  line-height: 40px;
  margin: 30px 0 10px;
  outline: inherit;
  flex-basis: 40%;
}

/* Version mobile */
@media screen and (max-width: 769px) {
  /* Div principale */
  #logo {
    width: 324px;
    height: 123px;
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
