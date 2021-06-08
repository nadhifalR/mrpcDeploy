<template>
  <body>
      <Header/>
      <div class="mainContainer h-auto my-3 mx-5 lg:mx-16 p-0 overflow-hidden xl:mx-44 min-h-screen">
            <div class="line w-full h-1 bg-green1 my-5 overflow-hidden"> </div>

            <div class="roboto flex mb-10 mx-auto content-center text-xl">
                <button class="beli-btn w-full py-2 px-4 mx-1">Your Builds</button>
                <button class="beli-btn w-full py-2 px-4 mx-1">Other's Builds</button>
            </div>

            <ul class="grid grid-cols-2 md:grid-cols-3">
                <li v-for="build in builds" :key="build.id">
                    <div class="sim-rekcard rounded-2xl bg-black ml-4 mb-4">
                        <div class="sim-rekcard-img w-full h-20 xl:h-32 bg-aqua rounded-t-2xl overflow-hidden">
                            <img class="w-full" src="../assets/pc1.jpg">
                        </div>
                        <p class="sim-rekcard-Title text-black text-xs md:text-sm xl:text-lg m-0 bg-green1">{{build.title}}</p>
                        <p class="sim-rekcard-Subtitle text-black text-xs md:text-sm xl:text-lg m-0 bg-green1">Total Harga Rp.XX.XXX.XXX</p>
                        <div class="sim-rekcard-detail text-xs text-white m0">
                            <p>{{build.cpu}}</p>
                            <p>{{build.memory}}</p>
                            <p>{{build.video_card}}</p>
                            <p>{{build.case}}</p>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
        <Footer/>
  </body>
</template>

<script>
import axios from 'axios'
import { ref } from 'vue'

export default{
    data(){
        return{
            builds: []
        }
    },
    mounted () {
        window.scrollTo(0, 0)
    },
    async mounted() {
        this.loadBuilds();
    },
    methods: {
        async loadBuilds(){
            const response = await axios.get(`https://34.101.183.41:5000/api/v1/builds/`)
            this.builds = response.data
        }
    }
}
</script>

<script setup>
import Header from './Header.vue'
import Footer from './Footer.vue'

const popupTriggers = ref({
    buttonTrigger:false
});

const TogglePopup = (trigger) => {
    popupTriggers.value[trigger] = !popupTriggers.value[trigger]
}
</script>

<style>
body {
    background-repeat: no-repeat;
    background-position: top center;  
    background-size:100%;
    background-color: black;
}

.roboto{
    font-family: 'Roboto', sans-serif;
}

.simluasi-boldtext{
    font-weight: 700;
}

.beli-btn{
    border: none;
    color: black;
    background-color: #02F39B;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    cursor: pointer;
    /* font-size: 20px; */
}

.beli-btn:hover, .saveBuild-btn:hover{
    background-color: #00B570;
}

.sim-rekcard-Title{
    font-family: 'Roboto', sans-serif;
    font-weight: 500;
    padding: 5px 0px 0px 10px;
}

.sim-rekcard-Subtitle{
    font-family: 'Roboto', sans-serif;
    font-weight: 300;
    padding: 5px 0px 5px 10px;
}

.sim-rekcard-detail{
    font-family: 'Roboto', sans-serif;
    font-weight: 400;
    padding: 20px 10px;
}
</style>