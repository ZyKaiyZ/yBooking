<script setup>
import { baseUrl } from '../main';
import axios from 'axios';
import Swal from 'sweetalert2';
import { useRouter } from 'vue-router';
import { useStore } from 'vuex';

const router = useRouter();
const store = useStore();

let email = '', password = '', password2 = '';

function signUp(){
    if (password === password2){
        axios.post(`${baseUrl}/sign_up`,{
            email: email,
            password: password
        })
        .then( (response) => {
            const isSuccess = response['data']['code'] === 200 ? true : false;
            Swal.fire(
                isSuccess?'Success':'Failure',
                isSuccess?'Sign up successfully': 'Email already in use',
                isSuccess?'success':'error'
            )
            if(isSuccess){
                store.dispatch('updateEmail', email);
                store.dispatch('updateLogin', true);
                router.push('/')
            }
        })
        .catch((error) => console.log(error))
    }
    else{
        Swal.fire(
            'Failure',
            'Passwords do not match',
            'error'
        )
    }
}
</script>
<template>
    <div class="main">
        <div class="first">
            <div id="top">
                <h3 class="header">Welcome to yBooking</h3>
            </div>
            <hr style="width: 100%;">
            <form class="mid" @submit.prevent="signUp">
                <div class="opt">
                    <input type="email" placeholder="Email *" required v-model="email">
                    <input type="password" placeholder="Password *" required v-model="password">
                    <input type="password" placeholder="Confirm your Password *" required v-model="password2">
                </div>
                <div class="cbt">
                    <button type="submit">Sign Up</button>
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
    margin-top: 50px;
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
    border-radius: 10px;
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
</style>