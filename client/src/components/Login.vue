<template>
    <div class="op fixed left-0 right-0 top-0 bottom-0">
        <div class="login-Container bg-loginB top-0 bottom-0 left-0 right-0 fixed m-auto w-5/6 lg:w-3/6 z-50 inline-block justify-center text-center">
            <img @click="ToggleLogin()" class="cursor-pointer w-8 lg:w-10 ml-auto mr-2 mt-2" src="../assets/close.svg">
            <p class="text-green1 text-4xl my-6 mx-8 lg:text-7xl title">LOGIN</p>
            <form v-on:submit.prevent="login" class="form relative mx-8 md:mx-16 py-5">
                <input v-model="email" type="text" placeholder="Email" class="logInput bg-loginB w-full rounded-xl py-3 px-4 mt-3 mb-5 mx-auto block text-center text-base md:text-lg xl:text-2xl text-white">
                <input v-model="password" type="password" placeholder="Password" class="logInput bg-loginB w-full rounded-xl py-3 px-4 mt-3 mb-5 mx-auto block text-center text-base md:text-lg xl:text-2xl text-white">
                <button type="submit" id="login-button" class="logButton bg-green1 text-loginB py-3 px-4 w-full rounded-xl cursor-pointer text-base md:text-lg xl:text-2xl">LOGIN</button>
        	</form>
            <p class="text-gray-400 text-2xl my-4">- OR -</p>
            <div class="relative mx-8 md:mx-16 py-5">
                <button class="googleLogin bg-green1 text-loginB py-3 px-4 w-full rounded-xl cursor-pointer mb-5 text-base md:text-lg xl:text-2xl">LOGIN WITH YOUR GOOGLE ACCOUNT</button>
                <button @click="()=> ToggleSignup('signupButtonTrigger')"  class="signup bg-green1 text-loginB py-3 px-4 w-full rounded-xl cursor-pointer text-base md:text-lg xl:text-2xl">SIGN UP</button>
            </div>
        </div>
    </div> 
    <Signup v-if="signupTriggers.signupButtonTrigger" :ToggleSignup="() => ToggleSignup('signupButtonTrigger')" :ToggleLogin="() => ToggleLogin()"></Signup>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  props: ['ToggleLogin'],
  data(){
    return{
        form: {
            email: '',
            password: ''
        },
        token: ''
    }
  },
  methods: {
    async register(){
      const response = await axios.post(`https://34.101.183.41:5000/api/v1/users/`, this.form)
      this.token = response.data
      localStorage.setItem("token", token)
    }
  }
}
</script>

<script setup>
import Signup from './Signup.vue'

const signupTriggers = ref({
    signupButtonTrigger:false
});

const ToggleSignup = (trigger) => {
    signupTriggers.value[trigger] = !signupTriggers.value[trigger]
}
</script>

<style>
.op{
    background-color: rgb(0, 0, 0, 0.5);
    z-index: 99;
}

form {
  z-index: 2;
}
form .logInput {
  outline: 0;
  border: 2px solid #02F39B;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}
form .logInput:hover {
  background-color: #00B570;
  color: #151515;
}

form .logButton {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
}

form .logButton:hover, .googleLogin:hover, .singup:hover{
  background-color: #00B570;
}

.googleLogin, .signup {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
}
</style>