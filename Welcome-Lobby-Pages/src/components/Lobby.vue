<template>
  <div class="hello" style="background-image: url('map4.jpeg'); background-color: #cccccc;  ">
  

    <div class="container">
		
        <div class="" style="text-align: center;">
            <img src="../assets/logo.png" alt="logo" class="logo"/>
        </div>
        <div class="card-columns" style="text-align: center; ">
            <div class="card" style=" margin:center; text-align: center;   background-color: transparent;">
                <img class="card-img-top img" src="../assets/images.png" >
                <p class="choix">FRANCE</p>
            </div>
            <div class="card" style="  margin:center; text-align: center;   background-color: transparent;">
                <img class="card-img-top img" src="../assets/images.png" >
                <p class="choix">FRANCE</p>
            </div>
            <div class="card" style="  margin:center; text-align: center;   background-color: transparent;">
                <img class="card-img-top img" src="../assets/images.png" >
                <p class="choix">FRANCE</p>
            </div>
            <div class="card" style="  margin:center; text-align: center;   background-color: transparent;">
                <img class="card-img-top img" src="../assets/images.png" >
                <p class="choix">FRANCE</p>
            </div>
            <div class="card" style="  margin:center; text-align: center;   background-color: transparent;">
                <img class="card-img-top img" src="../assets/images.png" >
                <p class="choix">FRANCE</p>
            </div>
            <div class="card" style="  margin:center; text-align: center;   background-color: transparent;">
                <img class="card-img-top img" src="../assets/images.png" >
                <p class="choix">FRANCE</p>
            </div>
        </div> 
        <div style="text-align: center;">
            <button class="button text-center" > <a href="">START</a>  </button>
        </div>
        <div style="text-align: center;">
            <button class="button text-center" > <a href="">Lien Partie</a></button>
        </div>
            
    </div>

  </div>
</template>

<script>
export default {
  name: 'Lobby',
  props: {
  }
}
</script>

<style scoped>

.logo {
    width: 35%;
    height: 100%;
    text-align: center;
}
.button {
    background: linear-gradient( #810124, #002843);
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none !important;
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
    -webkit-transition-duration: 0.4s;
    transition-duration: 0.4s;
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
    border: 1px solid #99002A;
    border-radius: 20px 20px  20px 20px !important; 
    font-family: Iceland; 
    font-size:48px;
    min-width: 354px;
    margin: 10px;
    -webkit-text-stroke: 0.5px #99002A;   
}
.button a {
    color: white;
     text-decoration: none !important;
    -webkit-text-stroke: 0.5px #99002A;   
}
.button a:hover {
    text-decoration: none;  
}
.img {
    max-width: 100px; 
    min-height: 5em;
    border: 1px solid #99002A;
    border-radius: 10px 10px 10px 10px !important; 
}
.choix{
    font-family: Arial, sans-serif;
    color:white; 
    -webkit-text-stroke: 0.5px #99002A; 
    font-size:24px;
}
.card {
    border: none !important; 
}

.card-columns .card {
    display: inline-block;
    width: 150px !important; 
    margin-right: 25px;
}
  
@media only screen and (max-width: 800px) {
    .logo {
        width: 50%;
    }
    .button {
        font-size:30px;
    }
    .img {
        max-width: 50px; 
        min-height: 3em;
        border: 1px solid #99002A;
        border-radius: 10px 10px 10px 10px;
    }
    .choix{
        font-size:12px;
    }
    .card-columns .card {
        display: inline-block;
        width: 150px !important; 
        margin-right: 0px;
    }
}

.logo2 {
    width: 35%;
    height: 100%;
    text-align: center;
}
.button2 {
    background: linear-gradient( #810124, #002843);
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
    -webkit-transition-duration: 0.4s; /* Safari */
    transition-duration: 0.4s;
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
    border: 1px solid #99002A;
    border-radius: 20px 20px;
     font-family: Iceland; 
    font-size:48px;
    -webkit-text-stroke: 0.5px #99002A;   
}
.img2 {
    max-width: 200px; 
    min-height: 5em;
    border: 1px solid #99002A;
    border-radius: 10px 10px;
}
.choix2{
    font-family: Arial, sans-serif;
     color:white; 
     -webkit-text-stroke: 0.5px #99002A; 
     font-size:48px;
}
@media only screen and (max-width: 800px) {
    .logo2 {
        width: 100%;
    }
    .button2 {
        font-size:30px;
    }
    .img2 {
        max-width: 100px; 
        min-height: 5em;
        border: 1px solid #99002A;
        border-radius: 10px 10px;
    }
    .choix2{
        font-size:24px;
    }
}

</style>
