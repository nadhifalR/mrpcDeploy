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
                <li v-for="index in 12" :key="index">
                    <BuildCard @click="$router.push('/Save')" class="cursor-pointer"></BuildCard>
                </li>
            </ul>
        </div>
        <Footer/>
  </body>
</template>

<script>
import { ref } from 'vue'

export default{
    mounted () {
        window.scrollTo(0, 0)
    }
}
</script>

<script setup>
import Header from './Header.vue'
import Footer from './Footer.vue'

import BuildCard from './BuildCard.vue'

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
</style>