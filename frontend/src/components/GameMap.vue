<template>
	<div>
		<div id="colonneInfos">
			<div id="minuteur">
				<img id="params" alt="Paramètres" title="Paramètres"
					src="../assets/img/settings.png"/>
				<!-- <p>5:30</p> -->
				<button value="valider">Valider</button>
			</div>
			<div>
				
			</div>
			<div id="drapeaux">
				<h1>Pays</h1>
				<div>
					<img alt="Drapeau français" title="France"
						src="../assets/img/flags/france.png"/>
					<img alt="Drapeau allemand" title="Allemagne"
						src="../assets/img/flags/germany.png"/>
					<img alt="Drapeau italien" title="Italie"
						src="../assets/img/flags/italy.png"/>
					<img alt="Drapeau russe" title="Russie"
						src="../assets/img/flags/russia.png"/>
					<img alt="Drapeau turque" title="Turquie"
						src="../assets/img/flags/turkey.png"/>
					<img alt="Drapeau anglais" title="Angleterre"
						src="../assets/img/flags/great-britain.png"/>
					<img alt="Drapeau autrichien" title="Autriche"
						src="../assets/img/flags/austria-hungary.png"/>
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
		<div id="carte">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 609 559">
			</svg>
		</div>
		<div id="colonneOrdres">
			<h1>Informations</h1>
			<div id="ordres">
				<p>Ordre 1</p>
				<p>Ordre 2</p>
				<p>Ordre 3</p>
				<p>Ordre 4</p>
				<p>Valider</p>
			</div>
			<div id="infos">
				<p>Sélectionnez une région pour choisir les ordres</p>
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
export default
{
	mounted()
	{
		let ns = "http://www.w3.org/2000/svg"
		let svg = document.querySelector("svg")
		const carte = require("../assets/json/map.json")

		for (var j in carte["areas"])
		{
			let nomZone = carte["areas"][j].name

			// Zone de terre
			let path = document.createElementNS(ns, "path")
			if (carte["areas"][j].type == "land")
			{
				path.setAttribute("fill", "#fcf2d4")

				// Couleur et changement du curseur lors du passage de souris
				path.addEventListener("mouseover", function()
				{
					this.style.cursor = "pointer"
					this.style.fill = "lightgreen"
					this.style.transition = "0.2s"
				})
				path.addEventListener("mouseout", function()
				{
					this.style.fill = "#fcf2d4"
				})
				path.addEventListener("click", function()
				{
					document.querySelector("#colonneOrdres > h1")
						.innerHTML = "Ordres"
					document.querySelector("#infos").style.display = "none"
					document.querySelector("#ordres").style.display = "flex"
					console.log("Clic zone terrestre : ", nomZone)
				})
			}

			// Zone neutre
			else if (carte["areas"][j].type == "impassable")
			{
				path.setAttribute("fill", "#808080")

				// Changement du curseur
				path.addEventListener("mouseover", function()
				{
					this.style.cursor = "not-allowed"
				})
			}

			// Zone maritime
			else
			{
				path.setAttribute("fill", "#b4b6cc")

				// Couleur et changement du curseur lors du passage de souris
				path.addEventListener("mouseover", function()
				{
					this.style.cursor = "pointer"
					this.style.fill = "lightblue"
					this.style.transition = "0.2s"
				})
				path.addEventListener("mouseout", function()
				{
					this.style.fill = "#b4b6cc"
				})
				path.addEventListener("click", function()
				{
					document.querySelector("#colonneOrdres > h1")
						.innerHTML = "Ordres"
					document.querySelector("#infos").style.display = "none"
					document.querySelector("#ordres").style.display = "flex"
					console.log("Clic zone maritime : ", nomZone)
				})
			}

			path.setAttribute("d", carte["areas"][j].path)
			path.setAttribute("name", carte["areas"][j].name)
			svg.appendChild(path)
		}

		for (var k in carte["infos"])
		{
			let pays = k // obligatoire, sinon toujours "Yor"

			// Labels
			let point = document.createElementNS(ns, "text")
			var text = document.createTextNode(k)
			point.setAttribute("x", carte["infos"][k].coords[0])
			point.setAttribute("y", carte["infos"][k].coords[1])
			point.appendChild(text)

			// Empêche la selection du label
			point.addEventListener("mouseover", function()
			{
				this.style.pointerEvents = "none"
			})
			svg.appendChild(point)

			// Points de ravitaillement
			if (typeof carte["infos"][k].coordsRav != "undefined")
			{
				let circleIn = document.createElementNS(ns, "circle")
				let circleOut = document.createElementNS(ns, "circle")
			
				circleIn.setAttribute("cx", carte["infos"][k].coordsRav[0])
				circleIn.setAttribute("cy", carte["infos"][k].coordsRav[1])
				circleIn.setAttribute("r", 2)
				circleIn.setAttribute("fill", "black")
				circleIn.setAttribute("stroke", "none")
				circleIn.setAttribute("stroke-width", 0)

				circleOut.setAttribute("cx", carte["infos"][k].coordsRav[0])
				circleOut.setAttribute("cy", carte["infos"][k].coordsRav[1])
				circleOut.setAttribute("r", 4)
				circleOut.setAttribute("fill", "none")
				circleOut.setAttribute("stroke", "black")

				// Couleur et changement du curseur lors du passage de souris
				circleOut.addEventListener("mouseover", function()
				{
					this.style.cursor = "pointer"
					this.style.fill = "lightcoral"
				})
				circleOut.addEventListener("mouseout", function()
				{
					this.style.fill = "none"
				})
				circleOut.addEventListener("click", function()
				{
					console.log("Clic ravitaillement : ", pays)
				})

				svg.appendChild(circleIn)
				svg.appendChild(circleOut)
			}

			// Pion marqueur
			if (k == "Par")
			{
				let marqueur = document.createElementNS(ns, "circle")

				marqueur.setAttribute("cx", carte["infos"][k].coords[0]-5)
				marqueur.setAttribute("cy", carte["infos"][k].coords[1])
				marqueur.setAttribute("r", 2.5)
				marqueur.setAttribute("fill", "red")
				marqueur.setAttribute("stroke", "red")
				svg.appendChild(marqueur)

				// Couleur et changement du curseur lors du passage de souris
				marqueur.addEventListener("mouseover", function()
				{
					this.style.cursor = "pointer"
					this.style.fill = "white"
				})
				marqueur.addEventListener("mouseout", function()
				{
					this.style.fill = "red"
				})
				marqueur.addEventListener("click", function()
				{
					console.log("Clic marqueur : ", pays)
				})
			}

			// Pion flotte
			if (k == "Nwg")
			{
				let flotte = document.createElementNS(ns, "ellipse")

				flotte.setAttribute("cx", carte["infos"][k].coords[0]-7.5)
				flotte.setAttribute("cy", carte["infos"][k].coords[1])
				flotte.setAttribute("rx", 5)
				flotte.setAttribute("ry", 2)
				flotte.setAttribute("fill", "blue")
				flotte.setAttribute("stroke", "blue")
				svg.appendChild(flotte)

				// Couleur et changement du curseur lors du passage de souris
				flotte.addEventListener("mouseover", function()
				{
					this.style.cursor = "pointer"
					this.style.fill = "white"
				})
				flotte.addEventListener("mouseout", function()
				{
					this.style.fill = "blue"
				})
				flotte.addEventListener("click", function()
				{
					console.log("Clic flotte : ", pays)
				})
			}

			// Pion armée
			if (k == "Gal")
			{
				let armee = document.createElementNS(ns, "rect")

				armee.setAttribute("x", carte["infos"][k].coords[0]-7.5)
				armee.setAttribute("y", carte["infos"][k].coords[1])
				armee.setAttribute("width", 5)
				armee.setAttribute("height", 5)
				armee.setAttribute("fill", "green")
				armee.setAttribute("stroke", "green")
				svg.appendChild(armee)

				// Couleur et changement du curseur lors du passage de souris
				armee.addEventListener("mouseover", function()
				{
					this.style.cursor = "pointer"
					this.style.fill = "white"
				})
				armee.addEventListener("mouseout", function()
				{
					this.style.fill = "green"
				})
				armee.addEventListener("click", function()
				{
					console.log("Clic armee : ", pays)
				})
			}
		}

		// Pour quitter la partie
		let paramBtn = document.getElementById("params")
		let quitDialog = document.getElementById("quitter")

		paramBtn.addEventListener("click", function onOpen()
		{
			if (typeof quitDialog.showModal === "function")
				quitDialog.showModal();
		})

		// Action effectuée lors de l'appuie sur l'un des boutons
		quitDialog.addEventListener("close", function onClose()
		{
			console.log(quitDialog.returnValue)
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
		flex-direction: row;
		justify-content: space-between;
	}
	img{
		cursor: pointer;
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
	.bloque{
		pointer-events: none;
		filter: grayscale(1) invert(0.1);
	}

	/* Colonnes */
	#colonneInfos,
	#colonneOrdres{
		width: 25vw;
		height: 98vh;
		border-radius: 10px;
		margin: 1vh 1vw 1vh 1vw;
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

	/* Drapeaux */
	#drapeaux{
		display: flex;
		flex-direction: column;
		height: 35%;
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
		height: calc(65% - 92px);
		background-color: unset;
	}
	#chat > h1{
		padding-top: 20px;
		border-style: solid;
		border-width: 4px 0 0;
		border-image: radial-gradient(#ae0132, #1c0043) 1;
	}

	/* Colonne d'ordres */
	#colonneOrdres{
		width: 18vw;
		height: 98vh;
	}
	#colonneOrdres > h1{
		line-height: 88px;
		margin: 0;
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
	#infos > p{
		margin: 0;
	}
	#ordres{
		display: none;
	}
	#ordres > p{
		margin: 0 10px;
		padding: 0 10% 0 10%;
		line-height: 55px;
		font-weight: bold;
	}
	#ordres > p:last-child{
		background-color: #808080;
		padding: 0 20% 0 20%;
	}
	#ordres > p:last-child:hover{
		background-color: #686868;
	}
	#ordres > p:last-child:active{
		background-color: #535353;
	}

	/* Boîte de dialogue pour quitter */
	#quitter{
		min-width: 25vw;
	}

/* Mode sombre */
@media(prefers-color-scheme: dark){
	/* Carte */
	svg{
		background-color: rgba(42, 58, 73, 0.9);
	}
}

/* Version tablette */
@media only screen and (min-width: 770px) and (max-width: 1370px){
	/* Div principale */
	#app > div{
		flex-wrap: wrap;
	}
	/* Carte */
	#carte{
		width: calc(75vw - 3vw);
		margin: 1vh 1vw 1vh 0;
		font-size: 10px;
	}

	/* Colonnes */
	#colonneInfos{
		height: 98vh;
	}

	/* Minuteur */
	#minuteur > img{
		width: 36px;
		height: 36px;
	}
	#minuteur > p{
		font-size: 40px;
		line-height: 76px;
	}
	#minuteur:first-child:after{
		width: 18px;
	}

	/* Drapeaux */
	#drapeaux > div > img{
		width: 30%;
	}

	/* Colonne d'ordres */
	#colonneOrdres{
		width: 100%;
		height: 35vh;
	}
	#ordres{
		flex-direction: row;
	}
	#ordres > p,
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
		margin: 0 2vw 1vh 2vw;
		font-size: 11px;
	}

	/* Colonnes */
	#colonneInfos,
	#colonneOrdres{
		width: 96vw;
		height: max-content;
		margin: 1vh 2vw 1vh 2vw;
	}

	/* Minuteur */
	#minuteur > img{
		width: 36px;
		height: 36px;
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

	/* Colonne d'ordres */
	#colonneOrdres{
		margin: 1vh 2vw 1vh 2vw;
	}
	#ordres{
		flex-direction: row;
	}
	#infos > p{
		margin: 30px 0;
		font-size: 32px;
	}
	#ordres > p,
	#quitter > form > button{
		font-size: 22px;
		margin: 10px;
	}
}
</style>