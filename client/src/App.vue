<template>
    <router-view/>
    <!-- <div>
      <Home/>
      <Simulation/>
    </div> -->
</template>

<script setup>
import Simulation from './components/Simulation.vue'
import Home from './components/Home.vue'

// This starter template is using Vue 3 experimental <script setup> SFCs
// Check out https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 0;
  padding: 0;
}

.title{
    font-size: 4.5rem;
    font-family: 'Roboto', sans-serif;
    font-weight: 700;
    color: white;
    padding: 0;
    margin: 0;
    
}

html{
  /* background: black; */
  padding: 0;
  margin: 0;
}

</style>
