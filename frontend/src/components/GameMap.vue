<template>
  <div>
    <div id="colonneInfos">
      <div>
        <div id="minuteur">
          <img
            id="quit"
            alt="Quitter la partie"
            title="Quitter la partie"
            src="../assets/img/quitter.png"
          />
          <button value="valider" @click="ready()">Prêt</button>
        </div>
        <div id="tour">
        </div>
      </div>
      <div id="drapeaux">
        <h1>Pays</h1>
        <div>
          <img v-if="this.fr == true"
            alt="Drapeau de la France"
            title="France"
            id="france"
            src="../assets/img/flags/france.png"
          />
          <img v-if="this.ge"
            alt="Drapeau de l'Allemagne"
            title="Allemagne"
            id="allemagne"
            src="../assets/img/flags/germany.png"
          />
          <img v-if="this.it"
            alt="Drapeau d'Italie"
            title="Italie"
            id="italie"
            src="../assets/img/flags/italy.png"
          />
          <img v-if="this.ru"
            alt="Drapeau de Russie"
            title="Russie"
            id="russie"
            src="../assets/img/flags/russia.png"
          />
          <img v-if="this.tu"
            alt="Drapeau de Turquie"
            title="Turquie"
            id="turquie"
            src="../assets/img/flags/turkey.png"
          />
          <img v-if="this.en"
            alt="Drapeau du Royaume-Uni"
            title="Royaume-Uni"
            id="royaume-uni"
            src="../assets/img/flags/great-britain.png"
          />
          <img v-if="this.au"
            alt="Drapeau d'Autriche"
            title="Autriche"
            id="autriche"
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
            <p id="ATTACK">Attaquer</p>
            <div class="ciblage" id="att">
              <label id="cible_attaque"></label>
              <div>
                <button>✔️</button>
                <button id="annulation_attaque">✖️</button>
              </div>
            </div>
          </div>
          <p id="HOLD">Tenir</p>
          <p id="SUPPORT">Soutenir</p>
          <div>
            <p id="CONVOY">Convoyer</p>
            <div class="ciblage" id="conv">
              <label id="cible_convoyer"></label>
              <div>
                <button>✔️</button>
                <button id="annulation_convoie">✖️</button>
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
        <p>Sélectionnez un pion pour choisir les ordres</p>
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
  <dialog id="inaccessible">
		<h1>Partie inaccessible</h1>
		<form method="dialog">
			<div>
        Cette partie est inaccessible.... mais vous pouvez en créer une nouvelle !
			</div>
			<div>
				<button>Accueil</button>
			</div>
		</form>
	</dialog>
</template>

<script>
import api from "../api";
import router from "../router/index.js";

const game_num = window.location.pathname.split("/")[2];
let ns;
let svg;

var unite;

const order = {
  type_order: "",
  dst_region_id: '',
  unit_id: '',
};

const ordres = [];

var num_tour= 0;

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



// import ns et svg
function ravitaillement(carte, pays, couleur){
  let k = pays;
  if (typeof carte["infos"][k].coordsRav != "undefined") {
    let circleIn = document.createElementNS(ns, "circle");
    let circleOut = document.createElementNS(ns, "circle");

    circleIn.setAttribute("cx", carte["infos"][k].coordsRav[0]);
    circleIn.setAttribute("cy", carte["infos"][k].coordsRav[1]);
    circleIn.setAttribute("r", 2);
    circleIn.setAttribute("fill", couleur);
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
      console.log("Clic ravitaillement : ", pays);
    });

    svg.appendChild(circleIn);
    svg.appendChild(circleOut);
  }
}


function  delete_pion(unite,carte){
  var taille = Object.keys(unite).length
  for(var i=0; i < taille; i++){
    var id = unite[i].id;
    let ex = document.getElementById(id);
    ex.remove();
  }
  
  for(var j in unite)
  {
    var p = trouver_pays(carte, unite[j].cur_region_id);
    ravitaillement(carte, p,"lightgrey");
  }

}
// import ns et svg
function color_armee(x,y, p,couleur, id){
  let armee = document.createElementNS(ns, "rect");

  armee.setAttribute("x", x - 7.5);
  armee.setAttribute("y", y);
  armee.setAttribute("width", 5);
  armee.setAttribute("height", 5);
  armee.setAttribute("fill", couleur);
  armee.setAttribute("stroke", couleur);
  armee.setAttribute("id",id);
  svg.appendChild(armee);

  // Couleur et changement du curseur lors du passage de souris
  armee.addEventListener("mouseover", function () {
    this.style.cursor = "pointer";
    this.style.fill = "lightgreen";
  });
  armee.addEventListener("mouseout", function () {
    this.style.fill = couleur;
  });
  // Ordre
  armee.addEventListener("click", function () {
    document.querySelector("#colonneOrdres > h1").innerHTML = "Ordres";
    document.querySelector("#infos").style.display = "none";
    document.querySelector("#ordres").style.display = "flex";

    
    console.log("Clic armee : ", p);
    console.log("Id de l'armée: ", id);
    order.unit_id = id;

    let $ = require("jquery");
    $(document.querySelector("#ordres > div > div:nth-child(4)")).hide()
    document.getElementById("cible_attaque").innerText = ""

    console.log("Clic zone terrestre : ", p);
  });
}

// import ns et svg
function color_flotte(x,y, p,couleur, id){
  let flotte = document.createElementNS(ns, "ellipse");

  flotte.setAttribute("cx", x - 7.5);
  flotte.setAttribute("cy", y);
  flotte.setAttribute("rx", 5);
  flotte.setAttribute("ry", 2);
  flotte.setAttribute("fill", couleur);
  flotte.setAttribute("stroke", couleur);
  flotte.setAttribute("id",id);
  svg.appendChild(flotte);

  // Couleur et changement du curseur lors du passage de souris
  flotte.addEventListener("mouseover", function () {
    this.style.cursor = "pointer";
    this.style.fill = "lightseagreen";
  });
  flotte.addEventListener("mouseout", function () {
    this.style.fill = couleur;
  });
  // Ordre
  flotte.addEventListener("click", function () {
    document.querySelector("#colonneOrdres > h1").innerHTML = "Ordres";
    document.querySelector("#infos").style.display = "none";
    document.querySelector("#ordres").style.display = "flex";


    console.log("Clic flotte : ", p);
    console.log("Id de la flotte: ", id);
    order.unit_id = id;

    let $ = require("jquery");
    $(document.querySelector("#ordres > div > div:nth-child(4)")).show()
    document.getElementById("cible_convoyer").innerText = ""
    document.getElementById("cible_attaque").innerText = ""

    console.log("Clic zone maritime : ", p);
  });
}

function trouver_pays(carte, src_region){
  for (var j in carte["areas"]){
    if (src_region == carte["areas"][j].id){
      let pays = j;
      return pays;
    }
  }
}

function init_rav(carte,unite){
  if(num_tour > 0)
  {
    // console.log("INIT RAV NUM TOUR > 0");
    for(var i in unite)
    {
      
      var p = trouver_pays(carte, unite[i].cur_region_id);
      //console.log(unite[i].type_unit);
      if(unite[i].power.id == 1) // ALLEMAGNE
      {
        ravitaillement(carte, p,"black");
      }else if(unite[i].power.id == 2) // Autriche-Hongrie
      {
        ravitaillement(carte, p,"orange");
      }else if(unite[i].power.id == 3)// FRANCE
      {
        ravitaillement(carte, p,"blue");
      }else if(unite[i].power.id == 4) // GB
      {
        ravitaillement(carte, p,"pink");
      }else if(unite[i].power.id == 5) // ITALIE
      {
        ravitaillement(carte, p,"red");
      }else if(unite[i].power.id == 6) // RUSSIA
      {
        ravitaillement(carte, p,"purple");
      }else if(unite[i].power.id == 7)// TURKEY
      {
        ravitaillement(carte, p,"green");
      }else{
        ravitaillement(carte, p,"lightgrey");
      }
    }
  }
}

function  init_pion(carte, unite){
  for(var i in unite){
    init_rav(carte,unite);
    let id = unite[i].id;
    let power = unite[i].power_id;
    let type = unite[i].type_unit;
    let region = unite[i].cur_region_id;
    let pays = trouver_pays(carte, region);
    var couleur = "grey";
    if(!(pays == "Con_sea" || pays == "Den_sea" || pays == "Kie_sea"))
    {
          let x = carte["infos"][pays].coords[0];
          let y = carte["infos"][pays].coords[1];
          if (power == 1){
            couleur = "black";
            if (type == "ARMY"){
              color_armee(x, y, pays, couleur, id);
            }
            if (type == "FLEET"){
              color_flotte(x, y, pays, couleur, id);
            }
            let allemagne = document.getElementById("allemagne");
            if (allemagne != null)
              allemagne.style.borderColor = couleur;
          }
          else  if (power == 2){
            couleur = "orange";
            if (type == "ARMY"){
              color_armee(x, y, pays, couleur, id);
            }
            if (type == "FLEET"){
              color_flotte(x, y, pays, couleur, id);
            }
            let autriche = document.getElementById("autriche");
            if (autriche != null)
              autriche.style.borderColor = couleur;
          }
          else if (power == 3){
            couleur = "blue";
            if (type == "ARMY"){
              color_armee(x, y, pays, couleur, id);
            }
            if (type == "FLEET"){
              color_flotte(x, y, pays, couleur, id);
            }
            let france = document.getElementById("france");
            if (france != null)
              france.style.borderColor = couleur;
          }
          else if (power == 4){
            couleur = "pink";
            if (type == "ARMY"){
              color_armee(x, y, pays, couleur, id);
            }
            if (type == "FLEET"){
              color_flotte(x, y, pays, couleur, id);
            }
            let royaumeUni = document.getElementById("royaume-uni");
            if (royaumeUni != null)
              royaumeUni.style.borderColor = couleur;
          }
          else if (power == 5){
            couleur = "red";
            if (type == "ARMY"){
              color_armee(x, y, pays, couleur, id);
            }
            if (type == "FLEET"){
              color_flotte(x, y, pays, couleur, id);
            }
            let italie = document.getElementById("italie");
            if (italie != null)
              italie.style.borderColor = couleur;
          }
          else if (power == 6){
            couleur = "purple";
            if (type == "ARMY"){
              color_armee(x, y, pays, couleur, id);
            }
            if (type == "FLEET"){
              color_flotte(x, y, pays, couleur, id);
            }
            let russie = document.getElementById("russie");
            if (russie != null)
              russie.style.borderColor = couleur;
          }
          else if (power == 7){
            couleur = "green";
            if (type == "ARMY"){
              color_armee(x, y, pays, couleur, id);
            }
            if (type == "FLEET"){
              color_flotte(x, y, pays, couleur, id);
            }
            let turquie = document.getElementById("turquie");
            if (turquie != null)
              turquie.style.borderColor = couleur;
          }
    }
  }
}


export default {
  data() {
    return {
      token: getTokenCookie(),
      player_id: '',
      power_id: '',
      username: '',
      dst: '',
      //num_tour: 0,
      fr: '',
      en: '',
      it: '',
      ru: '',
      au: '',
      tu: '',
      ge: '',
    }
  },
  methods: {
	// si le joueur clique sur valider tous les ordres
    ready() 
    {
      document.querySelector("#minuteur > button").classList.add("bloqueBtn");
			const config = {
				headers: { Authorization: `Bearer ${this.token}`}
			};

			api.players
				.update(game_num, this.player_id, this.username, this.power_id, true, config)
				.then(() =>
				{
          //console.log(ordres)
          for(let i = 0 ; i < ordres.length; i++)
          {
            console.log(ordres[i])
            api.orders
            .create(game_num, ordres[i].type_order, ordres[i].dst_region_id, ordres[i].unit_id,config)
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
          }
          
					// désactiver tous les boutons
				})
				.catch((err) => {
					console.log(err);
				})
    },
      changeTour(carte,unite,game_id,config) { // attendre qu'on passe au prochain tour
      // on prends les infos de la game
      api.games.get_game(game_id,config)
      .then(response => {
        // si le tour s'est incrémenté
        if(response.data.state == "END"){
          console.log("FIN")
          // Annoncer le vainqueur
        }else if(response.data.num_tour == (num_tour+1)){ // si on passe au prochain tour
            

            api.units.get_all(config)
            .then(response => {
              var test = response.data; 
              console.log(test)
              // update le plateau
                            // maj le num tour de notre côté
              num_tour +=1;
              delete_pion(unite,carte);
              ordres.length = 0;
              init_pion(carte,test);

              //console.log("ORDRES normalement vide : " + ordres);
              document.getElementById("tour").innerHTML = "Tour n°" + num_tour;
              document.querySelector("#minuteur > button").classList.remove("bloqueBtn");
              
            })
            .catch((erreur) => {
              console.log(erreur);
            })
        }
      })
      .catch(err => {
        console.log(err);
      })
    },
  },
  mounted() {
    svg = document.querySelector("svg");
    ns = "http://www.w3.org/2000/svg";
    var cookie = getTokenCookie();
    var is_refreshed = getRefresh();

    const carte = require("../assets/json/map.json");

    if(cookie == null)
    {
        if(!is_refreshed)
        {
          var expiration = new Date(Date.now() + 10000).toUTCString();
          document.cookie = `refreshed=true; expires=${expiration}; sameSite=Lax`
          location.reload();
        }
    }

    const config = {
        headers: {Authorization: `Bearer ${cookie}`}
    };
    var game_id = game_num;

    api.games
      .get_game(game_id, config)
      .then(response => {
        //console.log(response.data);
        for (var p in response.data.players) {
          //console.log("aaa");
          switch (response.data.players[p].username.toLowerCase()) {
            case 'france':

              this.fr = true;
              break;
            case 'germany':
              this.ge = true;
              break;
            case 'russia':
              this.ru = true;
              break;
            case 'austria-hungary':
              this.au = true;
              break;
            case 'great-britain':
              this.en = true;
              break;
            case 'turkey':
              this.tu = true;
              break;
            case 'italy':
              this.it = true;
              break;
            default:
              break;
          }
        }
        //console.log(this.fr);
      })
      .catch(function(error) {
        console.log(error);
        if ((error.response.status == 401) ||
            (error.response.status == 404)) {
          // Partie non accessible
          let inaccDialog = document.getElementById("inaccessible");
          let inaccQuit = document.querySelector("#inaccessible > form > div:last-child > button");

          if (typeof inaccDialog.showModal === "function") {
            document.querySelector("body").style.filter = "grayscale(1) invert(0.1)";
            inaccDialog.showModal();
          }
          inaccDialog.addEventListener('cancel', (event) => {
            event.preventDefault();
          });
          inaccQuit.addEventListener("click", function () {
            document.querySelector("body").style.filter = "unset";
            router.push({ path: `/`})
          });
        }
      })

    // Création de territoire
    for (var j in carte["areas"]) {
      let nomZone = carte["areas"][j].name;
      let etiquette = j;

      // Zone de terre
      let path = document.createElementNS(ns, "path");
      // ID POUR CHAQUE TERROIRE
      let id_zone = carte["areas"][j].id;
      path.setAttribute("id",id_zone);
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
          // reinitOrdres()
          console.log("Clic zone terrestre : ", nomZone);
          console.log("ID zone terrestre : ", id_zone);

          this.dst = nomZone;
          order.dst_region_id = id_zone;
          //console.log(etiquette)
          document.getElementById("cible_attaque").innerText = etiquette;
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
          // reinitOrdres() /////////////////////////////////////////////////

          console.log("Clic zone maritime : ", nomZone);
          this.dst = nomZone;
          order.dst_region_id = id_zone;
          console.log(etiquette);
          document.getElementById("cible_attaque").innerText = etiquette;
        });
      }

      path.setAttribute("d", carte["areas"][j].path);
      path.setAttribute("name", carte["areas"][j].name);
      svg.appendChild(path);
    }

    // Creation des labels
    for (var k in carte["infos"]) {

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
    }


    ////////////////// DEBUT ALGO
    //init plateau de jeu
    api.games.get_game(game_id,config)
    .then(response =>
    {
        for(var p in response.data.players)
        {
          for(var i in response.data.players[p].power){
            // si c'est nous, on remplit les infos
            if(response.data.players[p].is_you)
            {
              this.player_id = response.data.players[p].id ;
              this.username = response.data.players[p].username ;

              //console.log(response.data.players[p].power[i].id)
              this.power_id = response.data.players[p].power[i].id;
            }
          }
        }

        //console.log(response.data.players)
        // si on est bien à l'init du plateau
        
        // Code pour afficher le nombre de tour
        document.getElementById("tour").innerHTML = "Tour n°" + num_tour;
        if(response.data.num_tour == 0)
        {
          // get toutes les unités pour les placer initialement
            api.units.get_all(config)
            .then(response => {
              // console.log("INIT");
              //console.log(response.data)
              unite = response.data;
              init_pion(carte, unite);
              setInterval(this.changeTour,5000,carte, unite,game_id, config);
            })
            .catch((erreur) => {
              console.log(erreur);
            })
        }

    })
    .catch((err) => {
      console.log(err);
    })
    

    //var win = 15;
    //while(num_tour < 15){
      // vérifier si on passe au prochain

    //}

////////////////////////////////////////////////////
    // Validation d'un ordre
    let valider_ordres = document.getElementById("valider_ordres");
    valider_ordres.addEventListener("click", function valider() {
      //console.log(order);
      ordres.push(order);
    });


    // Attaquer
    let btn_attaque = document.getElementById("ATTACK");
    btn_attaque.addEventListener("click", function attaque_ordre() {
      order.type_order = btn_attaque.id;
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
    btn_ok_att.addEventListener("click", function attaque_ordre() {
      btn_attaque.classList.remove("enCours");
      $(document.getElementById("att")).hide()

      let valLab = document.querySelector("#att > label").textContent;
      console.log(valLab);
    });
      // Bouton annulation
    let btn_notok_att = document.querySelector("#att > div > button:last-child");
    btn_notok_att.addEventListener("click", function attaque_ordre() {
      btn_attaque.classList.remove("enCours");
      $(document.getElementById("att")).hide()

      console.log("Mission annulée !");
    });

    // Tenir
    let btn_tenir = document.getElementById("HOLD");
    btn_tenir.addEventListener("click", function tenir_ordre() {
      order.type_order = btn_tenir.id;
    });

    // Soutenir
    let btn_soutenir = document.getElementById("SUPPORT");
    btn_soutenir.addEventListener("click", function soutenir_ordre() {
      order.type_order = btn_soutenir.id;
    });

    // Annuler la cible ////////////////////A MOI ADD///////////////////////////////////////////////
    let btn_annulation_attaque = document.getElementById("annulation_attaque");
    btn_annulation_attaque.addEventListener("click", () => {
      this.dst ='';
      order.dst_region_id = "";
    })
    let btn_annulation_convoie = document.getElementById("annulation_convoie");
    btn_annulation_convoie.addEventListener("click", () => {
      this.dst = '';
      order.dst_region_id = "";
    })

    // Convoyer
    let btn_convoyer = document.getElementById("CONVOY");
    btn_convoyer.addEventListener("click", function convoyer_ordre() {
      order.type_order = btn_convoyer.id;
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

    // Quitter les ordres
    let quitterOrdres = document.getElementById("annuler_ordres");
    quitterOrdres.addEventListener("click", () => {
      document.querySelector("#colonneOrdres > h1").innerHTML = "Informations";
      document.querySelector("#infos").style.display = "flex";
      document.querySelector("#ordres").style.display = "none";
      // reinitOrdres();
    })
    let validerOrdres = document.getElementById("valider_ordres");
    validerOrdres.addEventListener("click", () => {
      console.log("Ordres validés");
      // reinitOrdres();
    })

    // Pour quitter la partie
    let quitBtn = document.getElementById("quit");
    let quitDialog = document.getElementById("quitter");

    quitBtn.addEventListener("click", function onOpen() {
      if (typeof quitDialog.showModal === "function") quitDialog.showModal();
    });

    document.querySelector("#quitter > form > div > button:last-child").addEventListener("click", function onClose() {
      // Prévenir le back que le joueur quitte
      router.push({ path: `/`})
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
    let $ = require("jquery");
    document.querySelector("#chat > h1").addEventListener("click", () => {
      if (window.innerWidth < 769) {
        $(document.getElementById("historique")).slideToggle(100);
        $(document.getElementsByTagName("form")[0]).slideToggle(100);
        $(document.querySelector("#chat > h1")).toggleClass("bas");
      }
    });

    // Code pour afficher le nombre de tour
    let nbrTour = 1;
    document.getElementById("tour").innerHTML = "Tour n°" + nbrTour;
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
    cursor: pointer;
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
  #tour{
    text-align: center;
    font-size: 25px;
    line-height: 30px;
    margin-bottom: 10px;
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
    border: 2px solid grey;
    border-radius: 6px;
	}

	/* Chat */
	#chat{
		width: 100%;
		height: calc(70% - 132px);
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
    width: calc(80% - 70px - 20px);
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
  #ATTACK,
  #CONVOY{
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
  #tour{
    font-size: 28px;
  }

	/* Drapeaux */
	#drapeaux > div > img{
		width: 30%;
	}

  /* Chat */
	#chat{
    height: calc(70% - 186px);
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
  #tour{
    font-size: 28px;
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
  #ATTACK,
  #CONVOY{
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