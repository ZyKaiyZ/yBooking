<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();

function home(){
    router.push('/')
}

function product(){
    router.push("/product")
}

function signUp(){
    router.push('/signup')
}

function login(){
    router.push('/login')
}
</script>
<template>
    <header>
        <h1 class="logo" @click="home">
            yBooking
        </h1>
        <section class="search-bar">
            <svg class="search-icon" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
                <path d="M0 0h24v24H0z" fill="none"/>
            </svg>
            <form class="search-form">
                <input type="text" placeholder="Where to?">
            </form>
        </section>
        <ul class="main-nav">
            <li @click="product" class="product">Product</li>
            <li @click="signUp">Sign Up</li>
            <li @click="login">Sign in</li>
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
    width: 817px;
    height: 70%;
    border: 1px solid #DCE0E0;
    padding: 19px 18px;
    float: left;
    border-right-color: transparent;
    border-bottom-color: transparent;
    border-top: none;
}
.search-icon {
    width: 40px;
    height: 40px;
    margin-right: 4px;
    float: left;
    fill: currentColor;
    color: #D3D5D3;
}
.search-form input{
    width: 730px;
    line-height: 18px;
    font-size: 30px;
    padding: 2px;
    margin-top: 3px;
    border: transparent;
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
</style>