<template>
	<div>
		<div>
			<div>
				<img alt="Paramètres" title="Paramètres" src="../assets/img/rouage.png"/>
				<p>5:30</p>
			</div>
			<div id="flags">
				<h1>Pays</h1>
				<div>
					<img alt="Drapeau Français" title="France" src="../assets/img/france.png"/>
					<img alt="Drapeau Allemand" title="Allemagne" src="../assets/img/germany.png"/>
					<img alt="Drapeau Italien" title="Italie" src="../assets/img/italy.png"/>
					<img alt="Drapeau Russe" title="Russie" src="../assets/img/russia.png"/>
					<img alt="Drapeau Turque" title="Turquie" src="../assets/img/turkey.png"/>
					<img alt="Drapeau Anglais" title="Angleterre" src="../assets/img/uk.png"/>
				</div>
			</div>
			<div id="chat">
				<h1>Chat</h1>
			</div>
		</div>
		<div id="map">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 609 559">
				
			</svg>
		</div>
	</div>
</template>

<script>
export default {
	mounted() {
		let ns = "http://www.w3.org/2000/svg"
		let svg = document.querySelector("svg")
		const map = require("../assets/json/map.json")

		for (var j in map["areas"])
		{
			// Zone de terre
			let path = document.createElementNS(ns, "path")
			if (map["areas"][j].type == "land")
			{
				path.setAttribute("fill", "#fcf2d4")

				// Couleur lors du passage de souris
				path.addEventListener("mouseover", function () {
					this.style.cursor =  "pointer"
					this.style.fill = "lightgreen"
				})
				path.addEventListener("mouseout", function () {
					this.style.cursor =  "pointer"
					this.style.fill = "#fcf2d4"
				})
			}

			// Zone neutre
			else if (map["areas"][j].type == "impassable")
			{
				path.setAttribute("fill", "grey")
			}

			// Zone maritime
			else
			{
				path.setAttribute("fill", "#b4b6cc")

				// Couleur lors du passage de souris
				path.addEventListener("mouseover", function () {
					this.style.cursor =  "pointer"
					this.style.fill = "lightblue"
				})
				path.addEventListener("mouseout", function () {
					this.style.cursor =  "pointer"
					this.style.fill = "#b4b6cc"
				})
			}

			path.setAttribute("d", map["areas"][j].path)
			path.setAttribute("name", map["areas"][j].name)
			svg.appendChild(path)
		}

		for (var k in map["infos"])
		{
			// Labels
			let point = document.createElementNS(ns, "text")
			var text = document.createTextNode(k)
			point.setAttribute("x", map["infos"][k].coords[0])
			point.setAttribute("y", map["infos"][k].coords[1])
			point.appendChild(text)

			// Empêche la selection du label
			point.addEventListener("mouseover", function () {
				this.style.pointerEvents = "none"
			})
			svg.appendChild(point)

			// Points de ravitaillement
			if (typeof map["infos"][k].coordsRav != "undefined")
			{
				let circleIn = document.createElementNS(ns, "circle")
				let circleOut = document.createElementNS(ns, "circle")
			
				circleIn.setAttribute("cx", map["infos"][k].coordsRav[0])
				circleIn.setAttribute("cy", map["infos"][k].coordsRav[1])
				circleIn.setAttribute("r", 2)
				circleIn.setAttribute("fill", "black")
				circleIn.setAttribute("stroke", "none")
				circleIn.setAttribute("stroke-width", 0)

				circleOut.setAttribute("cx", map["infos"][k].coordsRav[0])
				circleOut.setAttribute("cy", map["infos"][k].coordsRav[1])
				circleOut.setAttribute("r", 4)
				circleOut.setAttribute("fill", "none")
				circleOut.setAttribute("stroke", "black")

				// Couleur lors du passage de souris
				circleOut.addEventListener("mouseover", function () {
					this.style.cursor = "pointer"
					this.style.fill = "lightcoral"
				})
				circleOut.addEventListener("mouseout", function () {
					this.style.cursor =  "pointer"
					this.style.fill = "none"
				})

				svg.appendChild(circleIn)
				svg.appendChild(circleOut)
			}
		}
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
	#map{
		width: 70vw;
		height: 100vh;
		font-size: 11px;
	}
	svg{
		background-color: #535353;
		height: 100%;
	}

	/* Colonne de gauche */
	#app > div > div:first-child{
		width: 30vw;
		height: 94vh;
		background-color: #FFFFFF;
		box-shadow: 0px 0px 15px 5px  #CECECE;
		border-radius: 10px;
		margin-top: 3vh;
		margin-left: 20px;
	}
	#app > div > div:first-child > div{
		font-weight: bold;
		font-size: 12px;
	}

	/* Minuteur */
	#app > div > div > div:first-child{
		display: flex;
		justify-content: space-between;
		border-bottom: grey 3px solid;
	}
	#app > div > div > div > img{
		padding: 20px 0 20px 20px;
		width: 48px;
		height: 48px;
	}
	#app > div > div > div > p{
		font-size: 30px;
		line-height: 88px;
		margin: 0;
		text-align: center;
	}
	#app > div > div > div:first-child:after{
		content:"";
		width: 48px;
		padding-right: 20px;
	}

	/* Drapeaux */
	#flags{
		display: flex;
		flex-direction: column;
		height: 30%;
		margin-bottom: 30px;
	}
	#flags > div{
		display: flex;
		flex-wrap: wrap;
		align-items: center;
		justify-content: center;
	}
	#flags > div > img{
		width: 17%;
		margin: 0 10px;
	}

	/* Chat (masqué pendant l'alpha) */
	#chat{
		visibility: hidden; /* Placeholder pour plus tard */
		width: 30vw;
		height: calc(60% - 48px);
		border-radius: 10px;
	}

@media (prefers-color-scheme: dark){
	#app > div > div:first-child{
		background-color: #232224;
		box-shadow: 0px 0px 15px 5px #131313;
	}
	#app > div > div > div > img{
		filter: grayscale(1) invert(1);
	}
}
</style>