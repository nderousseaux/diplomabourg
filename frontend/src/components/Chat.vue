<template>
    <div class="chat-container">


        <div class="writter-container">
            <form action="" method="post">
                <textarea name="message" id="message" v-model="message" placeholder="Type here..."></textarea>
                <button disabled class="submit">Send</button>
            </form>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Chat',
    props: [],
    computed: {
        
    },
    methods: {
        Show(){
            var chat = document.querySelector(".chat-container")
            chat.classList.remove("Hide")
            chat.classList.add("Show")
        },
        Hide(){
            var chat = document.querySelector(".chat-container")
            chat.classList.remove("Show")
            chat.classList.add("Hide")
        }
    },
    data() {
        return {
            message : String
        }
    },
    mounted(){
        
        var chat = document.querySelector(".chat-container")
        chat.style.height = `${window.innerHeight}px` 
        document.querySelector(".chat-container").style.height = `${window.innerHeight}px`;
        document.addEventListener("resize", function () {
            document.querySelector(".chat-container").style.height = `${window.innerHeight}px`;
        })
        // console.log('Chat', this)
        setTimeout(this.Show, 2000)
        setTimeout(this.Hide, 6000)
        this.message = ""

    }

    
}
</script>

<style scoped>
    .chat-container{
        padding: 0px;
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
        width: 30%;
        min-height: 675px;
        position: absolute;
        right: -30%;
        top: 0px;
        background-color: red;
        z-index: 9999;
    }

    button.submit, textarea{
        position: absolute;
        bottom: 10px;
        border-radius: 5px;
    }

    textarea{
        height: 10px;
        padding: 10px 5px 15px 5px;
        left: 10px;
        width: 80%;
        font-size: 1em;
        color: #006eff;
        border-inline: 1px solid none;
    }

    button.submit{
        padding: 10px 10px;
        color: #fff;
        right: 10px;
        background-color: #006eff;
        font-weight: bold;
    }

    button.submit:hover{
        padding: 10px 10px;
        background-color: #fff;
        right: 10px;
        color: #006eff;
        font-weight: bold;
    }

    .Show{
        right: 0%;
        transition: right 3s ease-in-out;
    }

    .Hide{
        right: -30%;
        transition: right 3s ease-in-out;
    }
    
</style>
