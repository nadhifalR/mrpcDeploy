<template>
  <body>
      <Header/>

      <div class="mainContainer h-auto my-3 mx-5 lg:mx-16 p-0 overflow-hidden xl:mx-44 ">
            <div class="save-grid-container grid p-0 my-6 text-white text-base leading-none xl:leading-none ">
                <p class="text-5xl font-bold xl:text-7xl">Nama_Build</p>
                <p class="subtitle text-right align-text-bottom mt-auto font-bold text-lg">By User_name</p>
            </div>

            <div class="line w-full h-1 bg-green1 my-3 overflow-hidden"> </div>

            <div class="simulasi-container grid col-auto p-0 m-0">
                <div class="simulasi-container-horizontal grid text-white text-left font-bold m-1 p-0 align-middle text-xs lg:text-xl">
                    <p>Komponen</p>
                    <p>Nama Komponen</p>
                    <p>Harga</p>
                    <p>Marketplace</p>
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>CPU</p>
                    <p>{{savedBuilds.cpu}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Motherboard</p>
                    <p>{{savedBuilds.motherboard}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Memory</p>
                    <p>{{savedBuilds.memory}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>  
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Graphics Card</p>
                    <p>{{savedBuilds.video_card}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Power Supply</p>
                    <p>{{savedBuilds.power_supply}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Case</p>
                    <p>{{savedBuilds.case}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div> 
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Hard Drive</p>
                    <p>{{savedBuilds.internal_hard_drive}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div> 
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Keyboard</p>
                    <p>{{savedBuilds.keyboard}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Mouse</p>
                    <p>{{savedBuilds.mouse}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Monitor</p>
                    <p>{{savedBuilds.monitor}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>CPU Cooler</p>
                    <p>{{savedBuilds.cpu_cooler}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Case Fan</p>
                    <p>{{savedBuilds.case_fan}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Wireless Network Card</p>
                    <p>{{savedBuilds.wireless_network_card}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Wired Network Card</p>
                    <p>{{savedBuilds.wired_network_card}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Optical Drive</p>
                    <p>{{savedBuilds.optical_drive}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Sound Card</p>
                    <p>{{savedBuilds.sound_card}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Speakers</p>
                    <p>{{savedBuilds.speakers}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Headphones</p>
                    <p>{{savedBuilds.headphones}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>UPS</p>
                    <p>{{savedBuilds.ups}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
                <div class="simulasi-container-horizontal text-xs lg:text-xl">
                    <p>Thermal Paste</p>
                    <p>{{savedBuilds.thermal_paste}}</p>
                    <p>Rp.x.xxx.xxx</p>
                    <button @click="() => TogglePopup('buttonTrigger')" class="beli-btn">Beli Sekarang</button> 
                </div>
            </div>
           
           <div class="line w-full h-1 bg-green1 my-3 overflow-hidden"> </div>
           
           <div class="save-grid-container grid p-0 mt-6 mb-12 text-white text-base leading-none xl:leading-none ">
                <button @click="$router.push('Simulation')" class="roboto border-none text-black w-4/5 bg-green1 py-3 text-lg cursor-pointer ">Back to Simulator</button> 
                <p class="roboto text-white text-left font-bold p-0 align-middle text-xs lg:text-xl">Grand Total : Rp.x.xxx.xxx</p>
            </div>
        </div>

        <Footer/>
        <Market v-if="popupTriggers.buttonTrigger" :TogglePopup="() => TogglePopup('buttonTrigger')" ></Market>
  </body>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default{
    id: 'builds',
    data(){
        return{
            savedBuilds: []
        }
    },
    mounted () {
        window.scrollTo(0, 0)
    },
    async mounted(){
        this.loadSavedBuild();
    },
    methods: {
        async loadSavedBuild(){
            const response = await axios.get(`https://34.101.183.41:5000/api/v1/builds/`+this.$route.params.id)
            this.savedBuilds = response.data
        }
    }
}
</script>

<script setup>
import Header from './Header.vue'
import Footer from './Footer.vue'
import Market from './Market.vue'

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

.save-grid-container {
    grid-template-columns: 60% 40%;
}

.simulasi-container-horizontal{
    display: grid;
    grid-template-columns: 20% 40% 20% 20%;
    color: white;
    font-family: 'Roboto', sans-serif;
    font-weight: 400;
    text-align: left;
    margin: 0;
    padding: 0;
    vertical-align: middle;
    align-items: center;
}

.simluasi-boldtext{
    font-weight: 700;
}

.beli-btn{
    border: none;
    color: black;
    width: 100%;
    height: 70%;
    background-color: #02F39B;
    margin: 1rem 0;
    padding: 3px 0;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    cursor: pointer;
    /* font-size: 20px; */
}

.beli-btn:hover, .saveBuild-btn:hover{
    background-color: #00B570;
}
</style>