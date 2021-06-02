<template>
    <div class="op fixed left-0 right-0 top-0 bottom-0">
        <div class="login-Container bg-green1 top-0 bottom-0 left-0 right-0 fixed m-auto w-5/6 lg:w-3/6 z-50 inline-block justify-center text-center">
            <img @click="ToggleLogin();" class="cursor-pointer w-8 lg:w-10 ml-auto mr-2 mt-2" src="../assets/closeB.svg">
            <p class="text-loginB text-4xl mt-6 mb-3 mx-8 lg:text-7xl title">SIGN UP</p>
            <form v-on:submit.prevent="register" class="form relative mx-8 md:mx-16 py-3">
                <input v-model="form.email" type="email" placeholder="Email" class="signInput bg-green1 w-full rounded-xl py-3 px-4 mt-3 mb-5 mx-auto block text-center text-base md:text-lg xl:text-2xl text-loginB">
                <input v-model="form.name" type="text" placeholder="Your Name" class="signInput bg-green1 w-full rounded-xl py-3 px-4 mt-3 mb-5 mx-auto block text-center text-base md:text-lg xl:text-2xl text-loginB">
                <input v-model="form.password" type="password" placeholder="Password" class="signInput bg-green1 w-full rounded-xl py-3 px-4 mt-3 mb-5 mx-auto block text-center text-base md:text-lg xl:text-2xl text-loginB">
                <button type="submit" id="sign-button" class="signButton bg-loginB text-green1 py-3 px-4 w-full rounded-xl cursor-pointer text-base md:text-lg xl:text-2xl">SIGN UP</button>
        	</form>
            <p class="text-gray-400 text-2xl my-0">- OR -</p>
            <div class="relative mx-8 md:mx-16 py-5">
                <button class="googleSignup bg-loginB text-green1 py-3 px-4 w-full rounded-xl cursor-pointer mb-5 text-base md:text-lg xl:text-2xl">LOGIN WITH YOUR GOOGLE ACCOUNT</button>
                <button @click="ToggleSignup();" class="login bg-loginB text-green1 py-3 px-4 w-full rounded-xl cursor-pointer text-base md:text-lg xl:text-2xl">LOGIN</button>
            </div>
        </div>
    </div> 
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  props: ['ToggleSignup', 'ToggleLogin'],
  data(){
      return{
          form: {
              email: '',
              password: '',
              name: ''
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

<style>
.op{
    background-color: rgb(0, 0, 0, 0.5);
    z-index: 99;
}
form {
  z-index: 2;
}
form .signInput {
  outline: 0;
  border: 2px solid #151515;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
}
form .signInput:hover {
  background-color: #00B570;
  color:white;
}
form .signButton {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
}
form .signButton:hover, .googleSignup:hover, .login:hover{
  background-color: #00B570;
}
.googleSignup, .login {
  font-family: 'Roboto', sans-serif;
  font-weight: 700;
}
</style>