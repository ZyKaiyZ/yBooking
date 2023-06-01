<script setup>
import { useRouter } from 'vue-router';
const router = useRouter();

function launchProduct(){
    router.push('/launchproduct');
}

function shoppingCart(){
    router.push('/shoppingcart');
}

function yourOrders(){
    router.push('/order');
}

function cancelLaunchProduct(){
    router.push('/cancellaunchproduct');
}

</script>

<template>
    <div class="container">
        <table class="function-container" @click="launchProduct">
            <tr>
                <td class="icon-container">
                    <font-awesome-icon icon="fa-solid fa-up-long" class="icon"/>                </td>
                <td class="function-text">
                    Launch Product
                </td>
            </tr>
        </table>
        <table class="function-container" @click="shoppingCart">
            <tr>
                <td class="icon-container">
                    <font-awesome-icon icon="fa-solid fa-cart-shopping" class="icon"/>
                </td>
                <td class="function-text">
                    Shopping Cart
                </td>
            </tr>
        </table>
        <table class="function-container" @click="yourOrders">
            <tr>
                <td class="icon-container">
                    <font-awesome-icon icon="fa-solid fa-clipboard" class="icon"/>
                </td>
                <td class="function-text">
                    Your Orders
                </td>
            </tr>
        </table>
        <table class="function-container" @click="cancelLaunchProduct">
            <tr>
                <td class="icon-container">
                    <font-awesome-icon icon="fa-solid fa-down-long" class="icon"/>
                </td>
                <td class="function-text">
                    Cancel Launched
                </td>
            </tr>
        </table>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    flex-wrap: wrap;
    background: white;
    padding: 100px 50px 100px 50px;
}

.function-container {
    display: flex;
    margin: 25px;
    width: 300px;
    height: 300px;
    box-sizing: border-box;
    position: relative;
    border-radius: 20px;
    justify-content: center;
    cursor: pointer;
}

.icon-container{
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: white;
    width: 200px;
    height: 200px;
    border: 5px solid #3ca2f5;
    border-radius: 100px;
    transform:scale(1,1);transition: all 1s ease-out;
    margin-bottom: 20px;
}

.icon-container:hover{
    transform:scale(1.1,1.1);

}

.icon{
    width: 100px;
    height: 100px;
}
.function-text{
    margin-top: 20px;
    font-weight: bold;
    font-size: 30px;
    color: #3ca2f5;
    text-align: center;
}
</style>