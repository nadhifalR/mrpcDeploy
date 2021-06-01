<template>
  <div class="sim-rekcard rounded-2xl bg-black ml-4 mb-4">
        <div class="sim-rekcard-img w-full h-20 xl:h-32 bg-aqua rounded-t-2xl overflow-hidden">
            <img class="w-full" src="../assets/pc1.jpg">
        </div>
        <p class="sim-rekcard-Title text-black text-xs md:text-sm xl:text-lg m-0 bg-green1">Editing Video + Gaming Build</p>
        <p class="sim-rekcard-Subtitle text-black text-xs md:text-sm xl:text-lg m-0 bg-green1">Total Harga Rp.15.330.113</p>
        
        <div class="sim-rekcard-detail text-xs text-white m0">
            <p>AMD Ryzen 5 3600X</p>
            <p>Corsair LPX DDR4 2x8GB</p>
            <p>Palit RTX3060 Dual OC</p>
            <p>LianLi 205Case</p>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
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