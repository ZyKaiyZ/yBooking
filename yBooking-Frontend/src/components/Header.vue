<script setup>
import { useRouter } from 'vue-router';
import { computed, watch, ref } from 'vue';
import { useStore } from 'vuex';
import { baseUrl } from '../main';
import axios from 'axios';

const router = useRouter();
const store = useStore();
const email = computed(() => store.state.email);
const isLogin = computed(() => store.state.isLogin);
let user = email.value;
let keyword = ref();


watch(isLogin, (newValue) => {
  if (newValue) {
    user = computed(() => store.state.email).value;
  }
});
watch(keyword, (keyword) =>{
        store.dispatch('updateKeyword', keyword);
        // axios.post(`${baseUrl}/search_product`,{
        //     keyword: keyword
        // })
        // .then((res)=>{})
        // .catch((err)=>{console.error(err)});
    }
);

function home(){
    router.push('/')
}

function product(){
    router.push("/product");
}

function signUp(){
    router.push('/signup');
}

function login(){
    router.push('/login');
}

function signOut(){
    store.dispatch('updateEmail', '');
    store.dispatch('updateLogin', false);
    router.push('/login')
}

</script>
<template>
    <header>
        <h1 class="logo" @click="home">
            yBooking
        </h1>
        <section class="search-bar">
            <font-awesome-icon icon="fa-solid fa-magnifying-glass" class="search-icon" />
            <form class="search-form">
                <input type="text" placeholder="Where to?" v-model="keyword">
            </form>
        </section>
        <ul class="main-nav">
            <li v-if="isLogin" @click="product" class="product">Product</li>
            <li v-if="!isLogin" @click="signUp" class="no-product">Sign Up</li>
            <li v-else @click="signOut">Sign out</li>
            <li v-if="isLogin">Hi, {{ user }}</li>
            <li v-else @click="login">Sign in</li>
        </ul>
    </header>
    
</template>
<style scoped>
header {
    overflow: hidden;
    top:0;
    width: 100%;
    height: 80px;
    font-family: Circular,Helvetica,Arial,sans-serif;
    color: #484848;
    background-color: white;
    border: 3px solid #DCE0E0;
    border-radius: 0px;
    border-top: none;
    border-right: none;
    border-left: none;
}

.logo {
    width: 145px;
    height: 60px;
    margin: 0px;
    font-size: 33px;
    line-height: 49px;
    padding: 14px 20px;
    float: left;
    color: #3ca2f5;
    border: 1px solid #DCE0E0;
    border-top: none;
    border-left: none;
    border-bottom-color: transparent;
}

.logo:hover{
    background-color: #F5F5F5;
    cursor: pointer;
}

.logo svg {
    width: 100px;
    height: 31px;
}

.search-bar {
    display: inline-flex;
    align-items: center;
    width: 600px;
    height: 100%;
    border: 1px solid #DCE0E0;
    float: left;
    border-right-color: transparent;
    border-bottom-color: transparent;
    border-top: none;
    position: relative;
}

.search-icon {
    width: 40px;
    height: 40px;
    margin-right: 4px;
    fill: currentColor;
    color: #D3D5D3;
    position: absolute;
    left: 10px;
}
.search-form input{
    width: 100%;
    line-height: 18px;
    font-size: 30px;
    padding: 2px;
    border: transparent;
    margin-left: 20px;
    padding-left: 50px;
}

.search-form input:focus {
    outline: none;
}

.main-nav{
    height: 100%;
    float: right;
    margin: 0px;
}

.main-nav li{
    float: left;
    list-style: none;
    padding: 22px 18px;
    border: 3px solid #DCE0E0;
    height: 47px;
    font-size: 30px;
    border-left-color: transparent;
    border-bottom: none;
    border-top: none;
    text-align: center;
    line-height: 37px;
}

.main-nav li:last-child{
    border-right-color: transparent;	
}
.main-nav li:hover{
    background-color: #F5F5F5;
    cursor: pointer;
    color: #3ca2f5;
}

.main-nav li.product {
    border-left: 3px solid #DCE0E0;
}

.main-nav li.no-product{
    border-left: 3px solid #DCE0E0;
}
</style>