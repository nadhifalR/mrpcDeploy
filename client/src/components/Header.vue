<template>
    <header class="grid grid-cols-2 mx-6 mt-4 text-lg lg:text-2xl">
        <ul class="flex">
            <a href="/"><li class="mr-5">Home</li></a>
            <a href="/Simulation"><li class="mr-5">Simulasi</li></a>
            <a href="/Build"><li class="mr-5">Builds</li></a>
        </ul>
        <div class="right-0 ml-auto flex">
            <p @click="$router.push('/')" class="cursor-pointer my-auto mr-3">mendingrakitpc.id</p>
            <img @click="() => ToggleLogin('loginButtonTrigger')" class="w-10 lg:w-auto cursor-pointer" src="../assets/profile.svg">
        </div>
    </header>
    <Login v-if="loginTriggers.loginButtonTrigger" :ToggleLogin="() => ToggleLogin('loginButtonTrigger')"></Login>
</template>

<script>
import { ref } from 'vue'

export default{

}
</script>

<script setup>
import Login from './Login.vue'
import Signup from './Signup.vue'

const loginTriggers = ref({
    loginButtonTrigger:false
});

const ToggleLogin = (trigger) => {
    loginTriggers.value[trigger] = !loginTriggers.value[trigger]
}
</script>

<style scoped>
    .marginright{
        margin-right: auto;
    }
    header{
        color: #00B570;
    }

</style>