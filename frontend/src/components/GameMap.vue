<template>
	<div>
		<div>
			<div id="minuteur">
				<img id="params" alt="Paramètres" title="Paramètres" src="../assets/img/settings.png"/>
				<p>5:30</p>
			</div>
			<div id="drapeaux">
				<h1>Pays</h1>
				<div>
					<img alt="Drapeau français" title="France" src="../assets/img/flags/france.png"/>
					<img alt="Drapeau allemand" title="Allemagne" src="../assets/img/flags/germany.png"/>
					<img alt="Drapeau italien" title="Italie" src="../assets/img/flags/italy.png"/>
					<img alt="Drapeau russe" title="Russie" src="../assets/img/flags/russia.png"/>
					<img alt="Drapeau turque" title="Turquie" src="../assets/img/flags/turkey.png"/>
					<img alt="Drapeau anglais" title="Angleterre" src="../assets/img/flags/great-britain.png"/>
					<img alt="Drapeau autrichien" title="Autriche" src="../assets/img/flags/austria-hungary.png"/>
				</div>
			</div>
			<div id="chat">
				<h1>Chat</h1>
			</div>
		</div>
		<div id="carte">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 609 559">
			</svg>
		</div>
		<div>
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
		<p>Voulez-vous quitter la partie ?</p>
		<form method="dialog">
			<button value="annuler">Annuler</button>
			<button value="confirmer">Quitter</button>
		</form>
	</dialog>
</template>

<script>
export default {
	mounted() {
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
				path.addEventListener("mouseover", function ()
				{
					this.style.cursor = "pointer"
					this.style.fill = "lightgreen"
					this.style.transition = "0.2s"
				})
				path.addEventListener("mouseout", function ()
				{
					this.style.fill = "#fcf2d4"
				})
				path.addEventListener("click", function ()
				{
					document.querySelector("#app > div > div:last-child > h1").innerHTML = "Ordres"
					document.querySelector("#infos").style.display = "none"
					document.querySelector("#ordres").style.display = "flex"
					console.log("Clic zone terrestre : ", nomZone)
				})
			}

			// Zone neutre
			else if (carte["areas"][j].type == "impassable")
			{
				path.setAttribute("fill", "grey")

				// Changement du curseur
				path.addEventListener("mouseover", function ()
				{
					this.style.cursor = "not-allowed"
				})
			}

			// Zone maritime
			else
			{
				path.setAttribute("fill", "#b4b6cc")

				// Couleur et changement du curseur lors du passage de souris
				path.addEventListener("mouseover", function ()
				{
					this.style.cursor = "pointer"
					this.style.fill = "lightblue"
					this.style.transition = "0.2s"
				})
				path.addEventListener("mouseout", function ()
				{
					this.style.fill = "#b4b6cc"
				})
				path.addEventListener("click", function ()
				{
					document.querySelector("#app > div > div:last-child > h1").innerHTML = "Ordres"
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
			// Labels
			let point = document.createElementNS(ns, "text")
			var text = document.createTextNode(k)
			point.setAttribute("x", carte["infos"][k].coords[0])
			point.setAttribute("y", carte["infos"][k].coords[1])
			point.appendChild(text)

			// Empêche la selection du label
			point.addEventListener("mouseover", function ()
			{
				this.style.pointerEvents = "none"
			})
			svg.appendChild(point)

			// Points de ravitaillement
			if (typeof carte["infos"][k].coordsRav != "undefined")
			{
				let pays = k // obligatoire, sinon toujours "Yor"
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
				circleOut.addEventListener("mouseover", function ()
				{
					this.style.cursor = "pointer"
					this.style.fill = "lightcoral"
				})
				circleOut.addEventListener("mouseout", function ()
				{
					this.style.fill = "none"
				})
				circleOut.addEventListener("click", function ()
				{
					console.log("Clic ravitaillement : ", pays)
				})

				svg.appendChild(circleIn)
				svg.appendChild(circleOut)
			}

			// Création de pion
			if (k == "Par")
			{
				let pays = k // obligatoire, sinon toujours "Yor"
				let pion = document.createElementNS(ns, "circle")
		
				pion.setAttribute("cx", carte["infos"][k].coordsRav[0]-10)
				pion.setAttribute("cy", carte["infos"][k].coordsRav[1])
				pion.setAttribute("r", 4)
				pion.setAttribute("fill", "red")
				pion.setAttribute("stroke", "red")
				svg.appendChild(pion)

				// Couleur et changement du curseur lors du passage de souris
				pion.addEventListener("mouseover", function ()
				{
					this.style.cursor = "pointer"
					this.style.fill = "lightcoral"
				})
				pion.addEventListener("mouseout", function ()
				{
					this.style.fill = "red"
				})
				pion.addEventListener("click", function ()
				{
					console.log("Clic pion : ", pays)
				})
			}
		}

		// Pour quitter la partie
		let paramBtn = document.getElementById("params");
		let quitDialog = document.getElementById("quitter");

		paramBtn.addEventListener("click", function onOpen() {
			if (typeof quitDialog.showModal === "function") {
				quitDialog.showModal();
			}
		})

		// Action effectuée lors de l'appuie sur l'un des boutons
		quitDialog.addEventListener("close", function onClose() {
			console.log(quitDialog.returnValue)
		})
	}
}
</script>
<style scoped>
	/* Div principale */
	#app > div{
		background-color: #f0f0f0;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	}
	img{
		cursor: pointer;
	}
	h1, p{
		text-align: center;
	}

	/* Carte */
	#carte{
		border-radius: 10px;
		box-shadow: 0px 0px 15px 5px #CECECE;
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
		background-color: #535353;
		height: 100%;

		/* Style pour le blocage de la carte */
		/* pointer-events: none;
		filter: grayscale(1) invert(0.1); */
	}

	/* Colonne de gauche */
	#app > div > div:first-child,
	#app > div > div:last-child{
		width: 25vw;
		height: 98vh;
		background-color: white;
		box-shadow: 0px 0px 15px 5px #CECECE;
		border-radius: 10px;
		margin: 1vh 1vw 1vh 1vw;
	}

	/* Minuteur */
	#minuteur{
		display: flex;
		justify-content: space-between;
		border-bottom: grey 3px solid;
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
		height: 30%;
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

	/* Chat (masqué pendant l'alpha) */
	#chat{
		display: none; /* Placeholder pour plus tard */
		width: 30vw;
		height: calc(60% - 48px);
		border-radius: 10px;
	}

	/* Colonne d'ordres */
	#app > div > div:last-child{
		width: 18vw;
		height: 98vh;
	}
	#app > div > div:last-child > h1{
		line-height: 88px;
		margin: 0;
		border-bottom: grey 3px solid;
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
		font-size: 25px;
	}
	#ordres{
		display: none;
	}
	#ordres > p,
	#quitter > form > button{
		background-color: #F0F0F0;
		padding: 0 10% 0 10%;
		margin: 0 10px;
		line-height: 55px;
		font-size: 25px;
		border-radius: 10px;
		border-style: grey 3px solid;
		cursor: pointer;
		transition: 0.3s;
		font-weight: bold;
	}
	#ordres > p:hover,
	#quitter > form > button:hover{
		background-color: #e4e4e4;
	}
	#ordres > p:active,
	#quitter > form > button:active{
		background-color: #d6d6d6;
	}
	#ordres > p:last-child{
		background-color: grey;
		color: white;
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
		background-color: white;
		border-radius: 10px;
		border-style: none;
		box-shadow: 0px 0px 15px 5px #5b5b5b;
	}
	#quitter > p{
		font-size: 25px;
		padding: 0 30px;
	}
	#quitter > form{
		display: flex;
		justify-content: space-evenly;
	}
	#quitter > form > button{
		border: none;
		line-height: 40px;
		margin: 0 10px;
		outline: inherit;
		flex-basis: 50%;
	}

/* Version tablette */
@media screen and (min-width:770px) and (max-width:1370px){
	/* Carte */
	#carte{
		margin: 1vh 1vw 1vh 0;
		font-size: 10px;
	}

	/* Colonne de gauche */
	#app > div > div:first-child,
	#app > div > div:last-child{
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
	#infos > p{
		font-size: 32px;
	}
	#ordres > p,
	#quitter > form > button{
		font-size: 22px;
	}
}

/* Version mobile */
@media screen and (max-width:769px){
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

	/* Colonne de gauche */
	#app > div > div:first-child{
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
	#ordres{
		flex-direction: row;
	}
	#app > div > div:last-child{
		width: 96vw;
		margin: 1vh 2vw 1vh 2vw;
		height: max-content;
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

/* Thème sombre */
@media (prefers-color-scheme: dark){
	/* Colonnes */
	#app > div > div:first-child,
	#app > div > div:last-child,
	#carte,
	#quitter{
		background-color: #232224;
		box-shadow: 0px 0px 15px 5px #131313;
	}
	#minuteur > img{
		filter: grayscale(1) invert(1);
	}

	/* Boutons */
	#ordres > p,
	#quitter > form > button{
		background-color: #bbbbbb;
	}
	#ordres > p:hover,
	#quitter > form > button:hover{
		background-color: #a0a0a0;
	}
	#ordres > p:active,
	#quitter > form > button:active{
		background-color: #868686;
	}

	/* Boîte de dialogue pour quitter */
	#quitter{
		box-shadow: 0px 0px 15px 5px #424242;
	}
}
</style>