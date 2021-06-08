<template>
  <div class="sim-rekcard rounded-2xl bg-black ml-4 mb-4">
        <div class="sim-rekcard-img w-full h-20 xl:h-32 bg-aqua rounded-t-2xl overflow-hidden">
            <img class="w-full" src="../assets/pc1.jpg">
        </div>
        <slot/>
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