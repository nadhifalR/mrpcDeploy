<template>
    <div class="headerHome flex mx-6 mt-4 text-lg lg:text-2xl text-green2">
        <img @click="() => ToggleLogin('loginButtonTrigger')" class="marginright w-10 lg:w-auto cursor-pointer" src="../assets/profile.svg">
        <div @click="$router.push('/')" class="flex items-center cursor-pointer">
            <p class="text-sm sm:text-lg mx-2 md:mx-5">mendingrakitpc.id</p>
            <img class="logo mr-auto max-w-10 max-h-10 sm:max-w-12 sm:max-h-12 lg:max-w-16 lg:max-h-16" src="../assets/logo.png">
        </div>
    </div>
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

<style>
    .marginright{
        margin-right: auto;
    }

</style>