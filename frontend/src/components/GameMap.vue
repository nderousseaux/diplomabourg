<template>
  <div>
    <div id="colonneInfos">
      <div id="minuteur">
        <img
          id="quit"
          alt="Quitter la partie"
          title="Quitter la partie"
          src="../assets/img/quitter.png"
        />
        <!-- <p>5:30</p> -->
        <button value="valider">Valider</button>
      </div>
      <div></div>
      <div id="drapeaux">
        <h1>Pays</h1>
        <div>
          <img
            alt="Drapeau français"
            title="France"
            src="../assets/img/flags/france.png"
          />
          <img
            alt="Drapeau allemand"
            title="Allemagne"
            src="../assets/img/flags/germany.png"
          />
          <img
            alt="Drapeau italien"
            title="Italie"
            src="../assets/img/flags/italy.png"
          />
          <img
            alt="Drapeau russe"
            title="Russie"
            src="../assets/img/flags/russia.png"
          />
          <img
            alt="Drapeau turque"
            title="Turquie"
            src="../assets/img/flags/turkey.png"
          />
          <img
            alt="Drapeau anglais"
            title="Angleterre"
            src="../assets/img/flags/great-britain.png"
          />
          <img
            alt="Drapeau autrichien"
            title="Autriche"
            src="../assets/img/flags/austria-hungary.png"
          />
        </div>
      </div>
      <div id="chat">
        <h1>Chat</h1>
        <div id="historique"></div>
        <form name="message">
          <input
            type="text"
            name="msg"
            id="msg"
            placeholder="Entrez votre message"
          />
        </form>
      </div>
    </div>
    <div id="carte">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 609 559"></svg>
    </div>
    <div id="colonneOrdres">
      <h1>Informations</h1>
      <div id="ordres"> 
        <div>
          <div>
            <p id="attaquer">Attaquer</p>
            <div class="ciblage" id="att">
              <label>Par</label>
              <div>
                <button>✔️</button>
                <button>✖️</button>
              </div>
            </div>
          </div>
          
          <p id="tenir">Tenir</p>
          <p id="soutenir">Soutenir</p>

          <div>
            <p id="convoyer">Convoyer</p>
            <div class="ciblage" id="conv">
              <label>Mun</label>
              <div>
                <button>✔️</button>
                <button>✖️</button>
              </div>
            </div>
          </div>
        </div>
        <div>
          <button id="annuler_ordres">✖️</button>
          <button id="valider_ordres">✔️</button>
        </div>
      </div>

      <div id="infos">
        <p>Sélectionnez une région pour choisir les ordres</p>
        <div>
          <button>Réinitialiser</button>
          <button class="bloqueBtn">Valider</button>
        </div>
      </div>
    </div>
  </div>
  <dialog id="quitter">
    <h1>Quitter la partie ?</h1>
    <form method="dialog">
      <div>
        <button value="annuler">Annuler</button>
        <button value="confirmer">Quitter</button>
      </div>
    </form>
  </dialog>
</template>

<script>
import api from "../api";

export default {
  mounted() {
    // Fonction pour réinitialiser la colonne d'ordres
    function reinitOrdres() {
      if (btn_attaque.classList.contains("enCours")) {
        btn_attaque.classList.remove("enCours");
        $(document.getElementById("att")).hide();
      }
      if (btn_convoyer.classList.contains("enCours")) {
        btn_convoyer.classList.remove("enCours");
        $(document.getElementById("conv")).hide();
      }
    }
    // Modèle de code pour changer le nombre de pions à poser
    var nbrPions = 2;
    var btnBloque = true;
    let infosPions = document.querySelector("#infos > p")
    let btnValider = document.querySelector("#infos > div > button:last-child")
    infosPions.innerHTML = "Vous avez " + nbrPions + " pions à placer sur la carte";

    document.querySelector("#colonneOrdres > h1").addEventListener("click", () => {
      if (nbrPions > 0)
      {
        nbrPions--
      }
      if (nbrPions == 1)
      {
        infosPions.innerHTML = "Vous avez " + nbrPions + " pion à placer sur la carte";
      }
      else if (nbrPions == 0 && btnBloque == true)
      {
        infosPions.innerHTML = "Vous avez placé tous vos pions sur la carte, vous pouvez valider leur positon";
        btnValider.classList.toggle("bloqueBtn")
        btnBloque = false
      }
      else if (nbrPions > 0)
        infosPions.innerHTML = "Vous avez " + nbrPions + " pions à placer sur la carte";
    })
    document.querySelector("#infos > div > button:first-child").addEventListener("click", () => {
      if (btnBloque == false)
      {
        nbrPions = 2
        infosPions.innerHTML = "Vous avez " + nbrPions + " pion à placer sur la carte";
        btnValider.classList.toggle("bloqueBtn")
        btnBloque = true;
      }
    })

    const order = {
      type_order: "",
      dst_region_id: 0,
      unit_id: 0,
    };

    let ns = "http://www.w3.org/2000/svg";
    let svg = document.querySelector("svg");
    const carte = require("../assets/json/map.json");

    var ordre;

    for (var j in carte["areas"]) {
      let nomZone = carte["areas"][j].name;

      // Zone de terre
      let path = document.createElementNS(ns, "path");
      if (carte["areas"][j].type == "land") {
        path.setAttribute("fill", "#fcf2d4");

        // Couleur et changement du curseur lors du passage de souris
        path.addEventListener("mouseover", function () {
          this.style.cursor = "pointer";
          this.style.fill = "lightgreen";
          this.style.transition = "0.2s";
        });

        path.addEventListener("mouseout", function () {
          this.style.fill = "#fcf2d4";
        });

        path.addEventListener("click", function () {
          reinitOrdres()
          $(document.querySelector("#ordres > div:first-child > div:last-child")).hide();

          document.querySelector("#colonneOrdres > h1").innerHTML = "Ordres";
          document.querySelector("#infos").style.display = "none";
          document.querySelector("#ordres").style.display = "flex";
          console.log("Clic zone terrestre : ", nomZone);
        });
      }

      // Zone neutre
      else if (carte["areas"][j].type == "impassable") {
        path.setAttribute("fill", "#808080");

        // Changement du curseur
        path.addEventListener("mouseover", function () {
          this.style.cursor = "not-allowed";
        });
      }

      // Zone maritime
      else {
        path.setAttribute("fill", "#b4b6cc");

        // Couleur et changement du curseur lors du passage de souris
        path.addEventListener("mouseover", function () {
          this.style.cursor = "pointer";
          this.style.fill = "lightblue";
          this.style.transition = "0.2s";
        });

        path.addEventListener("mouseout", function () {
          this.style.fill = "#b4b6cc";
        });

        path.addEventListener("click", function () {
          reinitOrdres()
          document.querySelector("#colonneOrdres > h1").innerHTML = "Ordres";
          document.querySelector("#infos").style.display = "none";
          document.querySelector("#ordres").style.display = "flex";

          // DEVENU INUTILE, JE SAVAIS PAS SI VOUS AVIEZ DU CODE A RECUP

          $(document.querySelector("#ordres > div:first-child > div:last-child")).show();
          // $(document.getElementById("convoyer")).show();
          // if (!btn_convoyer) {
          //   const conv = document.createElement("p");
          //   conv.innerText = "Convoyer";
          //   conv.setAttribute("id", "convoyer");
          //   if (window.innerWidth < 769) {
          //     conv.style.cssText = "width: 40%; line-height: 55px; font-size: 22px; margin: 10px 0; font-weight: bold;";
          //   }
          //   else if (window.innerWidth > 770 && window.innerWidth < 1370) {
          //     conv.style.cssText = "width: 40%; line-height: 55px; margin: 0; font-weight: bold;";
          //   }
          //   else {
          //     conv.style.cssText = "width: 60%; line-height: 55px; margin: 0; font-weight: bold;"
          //   }

          //   var btn_valider = document.querySelector("#soutenir");

          //   btn_valider.after(conv);

          //   conv.addEventListener("click", function convoyer_ordre() {
          //     ordre = conv.id;
          //     console.log("CONVOYER");
          //   });
          // }

          console.log("Clic zone maritime : ", nomZone);
        });
      }

      path.setAttribute("d", carte["areas"][j].path);
      path.setAttribute("name", carte["areas"][j].name);
      svg.appendChild(path);
    }

    for (var k in carte["infos"]) {
      let pays = k; // obligatoire, sinon toujours "Yor"

      // Labels
      let point = document.createElementNS(ns, "text");
      var text = document.createTextNode(k);
      point.setAttribute("x", carte["infos"][k].coords[0]);
      point.setAttribute("y", carte["infos"][k].coords[1]);
      point.appendChild(text);

      // Empêche la selection du label
      point.addEventListener("mouseover", function () {
        this.style.pointerEvents = "none";
      });
      svg.appendChild(point);

      // Points de ravitaillement
      if (typeof carte["infos"][k].coordsRav != "undefined") {
        let circleIn = document.createElementNS(ns, "circle");
        let circleOut = document.createElementNS(ns, "circle");

        circleIn.setAttribute("cx", carte["infos"][k].coordsRav[0]);
        circleIn.setAttribute("cy", carte["infos"][k].coordsRav[1]);
        circleIn.setAttribute("r", 2);
        circleIn.setAttribute("fill", "black");
        circleIn.setAttribute("stroke", "none");
        circleIn.setAttribute("stroke-width", 0);

        circleOut.setAttribute("cx", carte["infos"][k].coordsRav[0]);
        circleOut.setAttribute("cy", carte["infos"][k].coordsRav[1]);
        circleOut.setAttribute("r", 4);
        circleOut.setAttribute("fill", "none");
        circleOut.setAttribute("stroke", "black");

        // Couleur et changement du curseur lors du passage de souris
        circleOut.addEventListener("mouseover", function () {
          this.style.cursor = "pointer";
          this.style.fill = "lightcoral";
        });
        circleOut.addEventListener("mouseout", function () {
          this.style.fill = "none";
        });
        circleOut.addEventListener("click", function () {
          reinitOrdres()
          console.log("Clic ravitaillement : ", pays);
        });

        svg.appendChild(circleIn);
        svg.appendChild(circleOut);
      }

      // Pion marqueur
      if (k == "Par") {
        let marqueur = document.createElementNS(ns, "circle");

        marqueur.setAttribute("cx", carte["infos"][k].coords[0] - 5);
        marqueur.setAttribute("cy", carte["infos"][k].coords[1]);
        marqueur.setAttribute("r", 2.5);
        marqueur.setAttribute("fill", "red");
        marqueur.setAttribute("stroke", "red");
        svg.appendChild(marqueur);

        // Couleur et changement du curseur lors du passage de souris
        marqueur.addEventListener("mouseover", function () {
          this.style.cursor = "pointer";
          this.style.fill = "white";
        });
        marqueur.addEventListener("mouseout", function () {
          this.style.fill = "red";
        });
        marqueur.addEventListener("click", function () {
          reinitOrdres()
          console.log("Clic marqueur : ", pays);
        });
      }

      // Pion flotte
      if (k == "Nwg") {
        let flotte = document.createElementNS(ns, "ellipse");

        flotte.setAttribute("cx", carte["infos"][k].coords[0] - 7.5);
        flotte.setAttribute("cy", carte["infos"][k].coords[1]);
        flotte.setAttribute("rx", 5);
        flotte.setAttribute("ry", 2);
        flotte.setAttribute("fill", "blue");
        flotte.setAttribute("stroke", "blue");
        svg.appendChild(flotte);

        // Couleur et changement du curseur lors du passage de souris
        flotte.addEventListener("mouseover", function () {
          this.style.cursor = "pointer";
          this.style.fill = "white";
        });
        flotte.addEventListener("mouseout", function () {
          this.style.fill = "blue";
        });
        flotte.addEventListener("click", function () {
          reinitOrdres()
          console.log("Clic flotte : ", pays);
        });
      }

      // Pion armée
      if (k == "Gal") {
        let armee = document.createElementNS(ns, "rect");

        armee.setAttribute("x", carte["infos"][k].coords[0] - 7.5);
        armee.setAttribute("y", carte["infos"][k].coords[1]);
        armee.setAttribute("width", 5);
        armee.setAttribute("height", 5);
        armee.setAttribute("fill", "green");
        armee.setAttribute("stroke", "green");
        svg.appendChild(armee);

        // Couleur et changement du curseur lors du passage de souris
        armee.addEventListener("mouseover", function () {
          this.style.cursor = "pointer";
          this.style.fill = "white";
        });
        armee.addEventListener("mouseout", function () {
          this.style.fill = "green";
        });
        armee.addEventListener("click", function () {
          reinitOrdres()
          console.log("Clic armee : ", pays);
        });
      }
    }

    // Attaquer
    let btn_attaque = document.getElementById("attaquer");
    btn_attaque.addEventListener("click", function attaque_ordre() {
      ordre = btn_attaque.id;
      if (btn_attaque.classList.contains("enCours")) {
        btn_attaque.classList.remove("enCours");
        $(document.getElementById("att")).hide()
      }
      else {
        btn_attaque.classList.add("enCours");
        $(document.getElementById("att")).css("display", "flex")
      }
    });
      // Bouton validation
    let btn_ok_att = document.querySelector("#att > div > button:first-child");
    btn_ok_att.addEventListener("click", function convoyer_ordre() {
      btn_attaque.classList.remove("enCours");
      $(document.getElementById("att")).hide()

      let valLab = document.querySelector("#att > label").textContent;
      console.log(valLab);
    });
      // Bouton annulation
    let btn_notok_att = document.querySelector("#att > div > button:last-child");
    btn_notok_att.addEventListener("click", function convoyer_ordre() {
      btn_attaque.classList.remove("enCours");
      $(document.getElementById("att")).hide()

      console.log("Mission annulée !");
    });


    // Tenir
    let btn_tenir = document.getElementById("tenir");
    btn_tenir.addEventListener("click", function tenir_ordre() {
      ordre = btn_tenir.id;
      //console.log("TENIR");
    });


    // Soutenir
    let btn_soutenir = document.getElementById("soutenir");
    btn_soutenir.addEventListener("click", function soutenir_ordre() {
      ordre = btn_soutenir.id;
      //console.log("SOUTENIR");
    });

    // Convoyer
    let btn_convoyer = document.getElementById("convoyer");
    btn_convoyer.addEventListener("click", function convoyer_ordre() {
      ordre = btn_convoyer.id;
      if (btn_convoyer.classList.contains("enCours")) {
        btn_convoyer.classList.remove("enCours");
        $(document.getElementById("conv")).hide()
      }
      else {
        btn_convoyer.classList.add("enCours");
        $(document.getElementById("conv")).css("display", "flex")
      }
    });
      // Bouton validation
    let btn_ok_conv = document.querySelector("#conv > div > button:first-child");
    btn_ok_conv.addEventListener("click", function convoyer_ordre() {
      btn_convoyer.classList.remove("enCours");
      $(document.getElementById("conv")).hide()

      let valLab = document.querySelector("#conv > label").textContent;
      console.log(valLab);
    });
      // Bouton annulation
    let btn_notok_conv = document.querySelector("#conv > div > button:last-child");
    btn_notok_conv.addEventListener("click", function convoyer_ordre() {
      btn_convoyer.classList.remove("enCours");
      $(document.getElementById("conv")).hide()

      console.log("Mission annulée !");
    });

    // Validation d'un ordre
    let valider_ordres = document.getElementById("valider_ordres");
    valider_ordres.addEventListener("click", function valider() {
      var id_game = 7;

      order.type_order = ordre;
      order.dst_region_id = 1;
      order.unit_id = 1;

      console.log(order);
      //.post(`/games/${id}/orders`, order)
      api.orders
        .create(id_game, order.type_order, order.dst_region_id, order.unit_id)
        .then((response) => console.log(response.data))
        .catch((err) => {
          if (err.status == 400) {
            console.log(err.message);
          }
          if (err.status == 401) {
            console.log(err.message);
          }
          if (err.status == 404) {
            console.log(err.message);
          }
          if (err.status == 500) {
            console.log(err.message);
          }
        });
    });

    
    // Quitter les ordres
    let quitterOrdres = document.getElementById("annuler_ordres");
    quitterOrdres.addEventListener("click", () => {
      document.querySelector("#colonneOrdres > h1").innerHTML = "Informations";
      document.querySelector("#infos").style.display = "flex";
      document.querySelector("#ordres").style.display = "none";
      reinitOrdres();
    })
    let validerOrdres = document.getElementById("valider_ordres");
    validerOrdres.addEventListener("click", () => {
      console.log("Ordres validés");
      reinitOrdres();
    })

    // Pour quitter la partie
    let quitBtn = document.getElementById("quit");
    let quitDialog = document.getElementById("quitter");

    quitBtn.addEventListener("click", function onOpen() {
      if (typeof quitDialog.showModal === "function") quitDialog.showModal();
    });

    // Action effectuée lors de l'appuie sur l'un des boutons
    quitDialog.addEventListener("close", function onClose() {
      console.log(quitDialog.returnValue);
    });

    // Action effectuée quand on appuie sur "Entrer" dans le chat
    let texte = document.querySelector("input[type=text]");
    document.querySelector("form").onkeypress = function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        if (texte.value != "") {
          // Récupérer le pseudo là dedans
          var pseudo = "Patrick";

          // Créer le message
          var para = document.createElement("p");
          var contenu = document.createTextNode(pseudo + " : " + texte.value);
          para.appendChild(contenu);
          para.style.textAlign = "left";
          para.style.margin = "0";

          // Changer la couleur du joueur en fonction du pays
          para.style.color = "wheat";

          let historique = document.getElementById("historique");
          historique.appendChild(para);

          // Réinitialiser l'input et afficher le dernier message
          texte.value = "";
          historique.scrollTop = historique.scrollHeight;
        }
      }
    };

    // Affiche ou masque l'historique et l'input
    var $ = require("jquery");
    document.querySelector("#chat > h1").addEventListener("click", () => {
      if (window.innerWidth < 769) {
        $(document.getElementById("historique")).slideToggle(100);
        $(document.getElementsByTagName("form")[0]).slideToggle(100);
        $(document.querySelector("#chat > h1")).toggleClass("bas");
      }
    });
  },
};
</script>

<style scoped>
	/* Div principale */
	#app > div{
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}

	/* Carte */
	#carte{
		border-radius: 10px;
		width: fit-content;
		height: 98vh;
		margin: 1vh 0 1vh 0;
		overflow-x: auto;
		overflow-y: hidden;
		font-size: 13px;
		user-select: none;
		cursor: not-allowed;
	}
	svg{
		background-color: rgba(112, 128, 143, 0.9);
		height: 100%;
	}
	.bloqueBtn{
		background-color: #555555 !important;
    cursor: not-allowed !important;
	}
  .bloqueBtn:hover{
		background-color: #555555 !important;
	}
  .bloqueBtn:active{
		background-color: #555555 !important;
	}
  .bloque{
    pointer-events: none;
		filter: grayscale(1) invert(0.1);
  }

	/* Minuteur */
	#minuteur{
		display: flex;
		justify-content: space-between;
		height: 88px;
	}
	#minuteur > img{
		width: 48px;
		height: 48px;
		margin: 20px 0 20px 20px;
		transition: 0.6s;
	}
	#minuteur > img:hover{
		transition: 0.6s;
		filter: invert(40%);
	}
	#minuteur > p{
		font-size: 40px;
		line-height: 88px;
		margin: 0;
		font-weight: bold;
		text-align: center;
	}
	#minuteur:first-child:after{
		content: "";
		width: 48px;
		padding-right: 20px;
	}
  #minuteur > button{
    width: 45%;
    line-height: 48px;
  }

	/* Drapeaux */
	#drapeaux{
		display: flex;
		flex-direction: column;
		height: 30%;
		overflow-x: auto;
	}
	#drapeaux > h1{
		font-size: 35px;
		font-weight: bold;
		margin: 20px 0;
	}
	#drapeaux > div{
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		justify-content: center;
	}
	#drapeaux > div > img{
		width: 17%;
		margin: 10px;
		user-select: none;
	}

	/* Chat */
	#chat{
		width: 100%;
		height: calc(70% - 92px);
		background-color: unset;
    margin: 0;
	}
	#chat > h1{
		padding-top: 20px;
    margin: 20px 0;
		border-style: solid;
		border-width: 4px 0 0;
		border-image: radial-gradient(#ae0132, #1c0043) 1;
	}

	/* Colonnes */
	#colonneInfos,
	#colonneOrdres{
		width: 22vw;
		height: 98vh;
		border-radius: 10px;
		margin: 1vh 1vw 1vh 1vw;
	}
	#infos,
	#ordres{
		display: flex;
		flex-wrap: wrap;
		height: calc(100% - 88px);
		flex-direction: column;
		justify-content: space-evenly;
		align-items: center;
	}
  #ordres > div:first-child > p,
  #ordres > div:first-child > div > p,
  #infos > div > button{
		width: 60%;
		line-height: 55px;
		font-weight: bold;
	}
	#ordres > div:first-child > button,
  #infos > div > button:last-child{
    line-height: 55px;
		background-color: #808080;
    width: 90%;
	}
	#ordres > button:hover,
  #infos > div > button:last-child:hover{
		background-color: #686868;
	}
	#ordres > button:active
  #infos > div > button:last-child:active{
		background-color: #535353;
	}

	/* Colonne d'ordres */
	#colonneOrdres > h1{
		line-height: 88px;
		margin: 0;
	}
	#ordres{
		display: none;
	}
  #ordres > div:first-child{
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;
    height: calc(100% - 95px);
    overflow-y: auto;
  }
  #ordres > div:last-child{
    display: flex;
    width: 100%;
    justify-content: space-evenly;
  }
  #ordres > div:first-child > div{
    display: flex;
    flex-direction: column;
    width: 60%;
    align-items: center;
    justify-content: center;
  } 
  .enCours{
    background-color: #376890 !important;
  }
  .ciblage{
    display: none;
    width: 100%;
    justify-content: space-evenly;
  }
  .ciblage > div{
    display: flex;
    width: calc(30px + 30px + 10px);
    justify-content: space-evenly;
  }
  .ciblage > label{
    min-width: fit-content;
    width: calc(60% - 70px - 20px);
    height: 30px;
    text-align: center;
    margin: 0;
  }
  .ciblage > div > button,
  #ordres > div:last-child > button{
    width: 30px;
    line-height: 30px;
    margin: 0;
    font-size: 15px;
    border-radius: 5px;
    color: transparent;
    text-shadow: 0 0 0 #ffffff;
  }
  #ordres > div:last-child > button{
    font-size: 25px;
    width: 30%;
    line-height: 55px;
    border-radius: 10px;
  }
  .ciblage > div > button:first-child{
    margin-right: 10px;
  }
  .ciblage > div > button:first-child,
  #ordres > div:last-child > button:last-child{
    background-color: #008000;
  }
  .ciblage > div > button:first-child:hover,
  #ordres > div:last-child > button:last-child:hover{
    background-color: #006e00;
  }
  .ciblage > div> button:first-child:active,
  #ordres > div:last-child > button:last-child:active{
    background-color: #005200;
  }
  .ciblage > div > button:last-child,
  #ordres > div:last-child > button:first-child{
    background-color: #ff0000;
  }
  .ciblage > div > button:last-child:hover,
  #ordres > div:last-child > button:first-child:hover{
    background-color: #c90000;
  }
  .ciblage > div > button:last-child:active,
  #ordres > div:last-child > button:first-child:active{
    background-color: #a00000;
  }
  #attaquer,
  #convoyer{
    width: 100% !important;
  }

  /* Colonne d'infos */
  #infos{
    justify-content: space-between;
  }
  #infos > div{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }
	#infos > p{
    padding: 0 4px;
	}

/* Version tablette */
@media only screen and (min-width: 770px) and (max-width: 1370px){
	/* Div principale */
	#app > div{
		flex-wrap: wrap;
		justify-content: space-between;
	}

	/* Carte */
	#carte{
		width: calc(75vw - 3vw);
		max-width: max-content;
		margin: 1vh 1vw 0 0;
		font-size: 10px;
	}

	/* Minuteur */
  #minuteur{
    flex-direction: column;
    align-items: center;
    height: 142px;
  }
	#minuteur > img{
		width: 36px;
		height: 36px;
    margin: 20px 0 0 0;
	}
	#minuteur > p{
		font-size: 40px;
		line-height: 76px;
	}
	#minuteur:first-child:after{
		width: 18px;
	}
  #minuteur > button{
    width: 70%;
  }

	/* Drapeaux */
	#drapeaux > div > img{
		width: 30%;
	}

  /* Chat */
	#chat{
    height: calc(70% - 146px);
	}

  /* Colonnes */
	#colonneInfos{
		width: 25vw;
		height: 98vh;
    margin-bottom: 0;
	}

	#ordres > div:first-child > p:first-child,
	#ordres > div:first-child > p:nth-child(2){
		margin-top: 20px;
	}

	/* Colonne d'ordres */
	#colonneOrdres{
		width: 100%;
		height: max-content;
	}
	#ordres{
		flex-direction: row;
		height: max-content;
	}
  #ordres > div:first-child{
    flex-wrap: wrap;
    flex-direction: row;
    align-items: baseline;
  }
  #ordres > div:first-child > p,
  #ordres > div:first-child > div{
    width: 40%;
		margin: 10px 0;
	}

  #ordres > div:first-child > p:nth-child(3){
    margin-bottom: 20px;
  }
  #ordres > div:first-child > div{
    margin: 0;
  }
  #ordres > div:first-child > div:last-child > p{
    margin-top: 10px;
  }
  #ordres > div:first-child > p:nth-child(2){
    margin-bottom: 20px;
  }
	#ordres > div:last-child{
    margin: 10px 0;
	}
  .ciblage > div{
    width: calc(35px + 35px + 20px);
  }
  .ciblage > label{
    font-size: 28px;
    height: 35px;
  }
  .ciblage > div > button{
    width: 35px;
    line-height: 35px;
    font-size: 20px;
  }
  .ciblage > div > button:first-child{
    margin-right: 20px;
  }

  /* Colonne d'infos */
  #infos > div{
    flex-direction: row;
    justify-content: space-evenly;
  }
  #infos > div > button:first-child{
    width: 35%;
  }
  #infos > div > button:last-child{
    width: 35%;
  }

	/* Boîte de dialogue pour quitter */
	#quitter > form > button{
		width: 25%;
	}
}

/* Version mobile */
@media only screen and (max-width: 769px){
	/* Div principale */
	#app > div{
		flex-direction: column;
	}

	/* Carte */
	#carte{
		width: unset;
		margin: 0 2vw 0 2vw;
		font-size: 11px;
	}

	/* Minuteur */
	#minuteur > img{
		width: 48px;
		height: 48px;
	}
	#minuteur > p{
		line-height: 76px;
	}
	#minuteur:first-child:after{
		width: 36px;
	}

	/* Drapeaux */
	#drapeaux > div > img{
		width: 15%;
	}

  /* Colonnes */
	#colonneInfos,
	#colonneOrdres{
		width: calc(100vw - 2vw - 2vw);
		height: max-content;
		margin: 1vh 2vw 1vh 2vw;
	}

	/* Colonne d'ordres */
	#colonneOrdres{
		margin: 1vh 2vw 1vh 2vw;
	}
	#ordres{
		flex-direction: row;
	}
  #ordres > div:first-child{
    flex-wrap: wrap;
    flex-direction: row;
    align-items: baseline;
  }
	#ordres > div:first-child > p,
  #ordres > div:first-child > div{
    width: 40%;
	}
  #ordres > div:first-child > p,
  #attaquer,
  #convoyer{
		margin: 10px 0 !important;
  }
	#ordres > div:first-child > div:first-child > p,
	#ordres > div:first-child > p:nth-child(2){
		margin-top: 20px !important;
	}
  #ordres > div:last-child{
    margin: 20px 0;
	}
  .ciblage{
    flex-direction: column;
    align-items: center;
  }
  .ciblage > div{
    width: 100%;
  }
  .ciblage > label{
    width: 80%;
    margin: 10px 0;
    height: 35px;
  }
  .ciblage > div > button{
    width: 35px;
    line-height: 35px;
    margin-bottom: 10px;
  }
  .ciblage > div > button:first-child{
    margin-right: 0;
  }

  /* Colonne d'infos */
	#infos > p{
		margin: 30px 0;
	}
  #infos > div:last-child > button:first-child{
    width: 50%;
  }
  #infos > div:last-child > button:last-child{
    width: 70%;
  }

	/* Boîte de dialogue pour quitter */
	#quitter > form > div > button{
		margin: 10px;
	}
}

/* Mode sombre */
@media (prefers-color-scheme: dark) {
  /* Carte */
  svg {
    background-color: rgba(42, 58, 73, 0.9);
  }
}
</style>