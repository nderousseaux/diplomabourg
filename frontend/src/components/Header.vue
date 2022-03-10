<template>
    <header>
        <nav>
            <router-link class="HomeButton" to="/">Home</router-link>
            <router-link class="MapsButton" to="/Maps">Carte</router-link>
        </nav>
  </header>
</template>

<script>

export default {
    name: 'Header',
    props: [],
    computed: {
    },
    methods: {
        getPathname(){
            return location.pathname;
        },
        hideRouter(){
            const header = document.querySelector("header")
            header.innerHTML = ``
        }
    },
    data() {
        return {
            
        }
    },
    mounted(){
        if(this.getPathname() === `/Maps`)
            this.hideRouter()
    }
}
</script>

<style scoped>
    header{
        display: flex;
        flex-direction : row;
    }

    nav{
        margin: 5px 0px;
        width: 100%;
        height: auto;
        display: flex;
        flex-direction: inherit;
    }

    a{
        margin: 0px 20px;
        padding: 10px 15px;
        background-color: #006eff;
        border: 1px solid #fff;
        color: #fff;
        text-decoration: none;
        text-transform: uppercase;
        font-weight: bold;
    }

    a:hover{
        margin: 0px 20px;
        padding: 10px 15px;
        color: #006eff;
        background-color: #fff;
        border: 1px solid #006eff;
    }

     a:active{
        color: #006eff;
        background-color: #fff;
        border: 1px dashed #006eff;
    }
</style>
