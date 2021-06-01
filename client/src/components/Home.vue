<template >
    <div class="pointer-events-none top-0 bottom-0 m-0 absolute overflow-hidden min-h-full w-full">
        <img class="home pointer-events-none m-0 p-0 top-0 w-full h-auto absolute" src="../assets/HomeBG.png" alt="">
    </div>

    <div>
        <HeaderHome/>
        <img class="pc top-3 md:top-auto w-72 sm:w-1/2 left-0 right-0 md:w-1/3 ml-auto mx-auto absolute md:right-0 md:mr-20 lg:mr-32 xl:mr-40" src="../assets/asset-pc.svg">
    </div>
    
    <div class="text-center md:text-left md:ml-7 mt-56 sm:mt-72 md:mt-20 xl:mt-24 p-0 text-white text-base leading-none xl:text-xl w-full md:w-3/5">
        <p class="text-4xl md:text-6xl lg:text-7xl font-bold xl:text-7xl">Rakit PC <br> Impian anda</p>
        <button @click="$router.push('Simulation')" class="startButton bg-green1 text-white font-bold py-3 px-4 mt-10 w-5/6 md:w-96 rounded-xl cursor-pointer text-xl md:text-2xl">Mulai Rakit PC</button>
    </div>

    <div class="text-center md:text-left md:ml-7 mt-14 sm:mt-10 md:mt-20 p-0 text-white text-base leading-none xl:text-xl w-full md:w-3/5 xl:w-2/4">
        <p class="mx-10 md:mx-0 text-base md:text-xl ">
            Dewasa ini, komputer merupakan sebuah kebutuhan penting 
            bagi berbagai kalangan. Oleh karena itu, mendingrakitpc.com 
            ada untuk membantu kita semua dalam memilih komponen komputer 
            yang sesuai dengan kriteria dan budget kita.</p>
    </div>
</template>

<script setup>
    import HeaderHome from './HeaderHome.vue'
</script>

<style scoped>
body{
    /* background: url(../assets/HomeBG.png); */
    background-repeat: no-repeat;
    background-position: top center;  
    background-color: #1A2223;
    background-size:auto cover;
}
</style>

<style>
.home{
    z-index: -1;
}

.pc{
    left: 50%;
    right: 50%;
}

.startButton {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
  cursor: pointer;
}

.startButton:hover{
  background-color: #00B570;
}
</style>