<template>
    <div>
    <body>
        <Header/>
        <div class="mainContainer h-auto my-3 mx-5 lg:mx-16 p-0 overflow-hidden xl:mx-44">
            <div class="sim-grid-container md:grid p-0 m-0">
                <div class="sim-grid-item text-left m-0 p-0 text-white text-base leading-none xl:leading-none xl:text-xl">
                <p class="text-5xl font-bold mb-5 md:mb-0 xl:text-7xl xl:title">Rekomendasi build untuk anda.</p>
                <p class="subtitle mt-5 mb-5 md:mb-0">Rekomendasi pilihan dari kami untuk PC idaman anda.</p>
                </div>
                <div class="vertical-allign-center grid justify-center items-center">
                    <div class="sim-card-container grid">
                        <router-link v-for="build in builds.slice(-2)" :to="{name:'Save', params: {id: build.id} }" :key="build.id">
                            <BuildCard  class="cursor-pointer">
                                <p class="sim-rekcard-Title text-black text-xs md:text-sm xl:text-lg m-0 bg-green1">{{build.title}}</p>
                                <p class="sim-rekcard-Subtitle text-black text-xs md:text-sm xl:text-lg m-0 bg-green1">Total Harga Rp.XX.XXX.XXX</p>
                                <div class="sim-rekcard-detail text-xs text-white m0">
                                    <p>{{build.cpu}}</p>
                                    <p>{{build.memory}}</p>
                                    <p>{{build.video_card}}</p>
                                    <p>{{build.case}}</p>
                                </div>
                            </BuildCard>
                        </router-link>        
                    </div>
                    <button @click="$router.push('/Build')" class="sim-rekcard-btn cursor-pointer text-black bg-green1 text-xl py-2 px-8 inline-block text-center my-2 mx-10 sm:mx-30 md:mx-24 lg:mx-36 xl:mx-36">Explore Builds</button> 
                </div>
            </div>

            <div class="line w-full h-1 bg-green1 my-3 overflow-hidden"> </div>

            <p class="text-5xl font-bold mb-5 md:my-5 xl:text-7xl title">Simulasi</p>
            <SimulationContent/>
        </div>
        <Footer/>
    </body>
    </div>
</template>

<script setup>
import Header from './Header.vue'
import BuildCard from './BuildCard.vue'
import SimulationContent from './SimulationContent.vue'
import Footer from './Footer.vue'

const route = useRoute();
const id = computed(() => route.params.id);
// This starter template is using Vue 3 experimental <script setup> SFCs
// Check out https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md
</script>

<script>
import axios from 'axios'
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

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

<style>
body {
    background-image: url(../assets/SimulatorBG.png);
    background-repeat: no-repeat;
    background-position: top center;  
    background-size:100%;
    background-color: black;
}
.sim-grid-container {
    grid-template-columns: 40% 60%;
}
.sim-card-container {
    grid-template-columns: 50% 50%;
}

.sim-rekcard-btn:hover{
    background-color: #00B570;
}
</style>
