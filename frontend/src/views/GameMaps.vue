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

		const map = require("../assets/json/map.json");
		console.log("Ici", map);

		for (var i in map)
		{
			for (var j in map[i])
			{
				if (typeof map[i][j].path != "undefined")
				{
					let path = document.createElementNS(ns, "path")
					if (map[i][j].type == "land")
					{
						path.setAttributeNS(null, "fill", "#fcf2d4")
					}
					else if (map[i][j].type == "impassable")
					{
						path.setAttributeNS(null, "fill", "grey")
					}
					else
					{
						path.setAttributeNS(null, "fill", "#b4b6cc")
					}
					path.setAttributeNS(null, "d", map[i][j].path)
					path.setAttributeNS(null, "name", map[i][j].name)
					svg.appendChild(path)
				}
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
	path:hover{
		cursor: pointer;
		fill: lightgreen;
	}
	svg{
		background-color: #535353;
		height: 100%;
	}
	text{
		pointer-events: none;
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