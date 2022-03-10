<template>
  <Header />
  <main>
    <router-view></router-view>
  </main>
  <Chat />
  <Footer />
</template>


<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import Chat from '@/components/Chat.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    Chat
  },
  computed: {
    
  },
  methods: {
    currentPage() {
      return window.location.pathname;
    }
  }, 
  mounted () {
    const body = document.querySelector("body")
    body.style.height = `${window.innerHeight}px` 


    const main = document.querySelector("main")
    main.style.height = `70%` 
    
    if(this.currentPage == '/Maps')
    {
      // Faire disparaitre les routers
      document.querySelectorAll("header a").style.display = "none";
    }
  }
}
</script>

<style scoped>
  main{
        display: flex;
        flex-direction: row;
        width: 100%;
        height: auto;
    }
</style>