<script setup>
import { baseUrl } from '../main';
import axios from 'axios';
import Swal from 'sweetalert2';
import { useRouter } from 'vue-router';
const router = useRouter();

let email = '';
let password = '';

function signIn(){
    console.log(email, password)
    axios.post(`${baseUrl}/sign_in`,{
        email: email,
        password: password
    })
    .then( (response) => {
        const isSuccess = response['data']['code'] === 200 ? true : false;
        Swal.fire(
            isSuccess?'Success':'Failure',
            isSuccess?'Sign in successfully': 'Email or Password is wrong',
            isSuccess?'success':'error'
        )
        if(isSuccess){
            router.push('/')
        }
    })
    .catch( (error) => console.log(error))
}
</script>
<template>
    <div class="main">
        <div class="first">
            <div id="top">
                <h3 class="header">Welcome to yBooking</h3>
            </div>
            <hr style="width: 100%;">
            <form class="mid" @submit.prevent="signIn">
                <div class="opt">
                    <input type="email" placeholder="Email" required v-model="email" autocomplete="username">
                    <input type="password" placeholder="Password" required v-model="password" autocomplete="current-password">
                    <p class="forgot-pwd">Forgot password?</p>
                </div>
                <div class="cbt">
                    <button>Login</button>
                </div>
            </form>
        </div>
    </div>
</template>
<style scoped>
* {
    font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue, sans-serif;
}

.main {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top:  50px;
}

.header{
    font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue, sans-serif; 
    font-size: 55px; 
    color: #222222; 
    font-weight: 600; 
    font-style: normal; 
    line-height: 22px;
    text-align: center;
}

.first {
    border: 3px solid #3ca2f5;
    width: 40%;
    padding-left: 30px;
    padding-right: 30px;
    border-radius: 5px;
}

.form {
    width: 95%;
    height: 55px;
    border-radius: 10px 10px 0 0;
}

select {
    font-size: 40px;
    padding-left: 20px;
}

.opt input {
    width: 91%;
    height: 55px;
    border-radius: 10px;
    border: 1px solid gray;
    padding-left: 20px;
    margin: 20px;
    font-size: 30px;
    cursor: default;
}

::placeholder {
    font-size: 30px;
    padding-left: 10px;

}

.cbt button {
    width: 95%;
    height: 50px;
    margin: 20px;
    background-color: #3ca2f5;
    border-radius: 10px;
    color: aliceblue;
    font-size: 30px;
    font-weight: 55px;
    border: none;
    cursor: pointer;
}

#text>p {
    font-size: 12px;
    margin-top: 8px;
    margin-bottom: -10px;
    line-height: 16px;
    color: #222222;
    font-weight: 400;
    font-style: normal;
    font-family: Circular, -apple-system, BlinkMacSystemFont, Roboto, "Helvetica Neue", sans-serif;
}

.forgot-pwd{
    font-size: 25px;
    margin: 5px 30px 5px 30px;
}

.forgot-pwd:hover{
    color: #3ca2f5;
    cursor: pointer;
}
</style>