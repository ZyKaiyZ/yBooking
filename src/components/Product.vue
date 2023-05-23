<script>
import { ref, reactive, watch } from "vue";
export default {
  setup(){
    return {};
  },
};
</script>

<template>
    <div class="container">
        <table class="function-container">
            <tr>
                <td class="icon-container">
                    <font-awesome-icon icon="fa-solid fa-up-long" class="icon"/>                </td>
                <td class="function-text">
                    Launch Product
                </td>
            </tr>
        </table>
        <table class="function-container">
            <tr>
                <td class="icon-container">
                    <font-awesome-icon icon="fa-solid fa-cart-shopping" class="icon"/>
                </td>
                <td class="function-text">
                    Shopping Cart
                </td>
            </tr>
        </table>
        <table class="function-container">
            <tr>
                <td class="icon-container">
                    <font-awesome-icon icon="fa-solid fa-xmark" class="icon"/>
                </td>
                <td class="function-text">
                    Cancel Order
                </td>
            </tr>
        </table>
        <table class="function-container">
            <tr>
                <td class="icon-container">
                    <font-awesome-icon icon="fa-solid fa-left-long" class="icon"/>
                </td>
                <td class="function-text">
                    Return Order
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
}

.icon-container{
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: white;
    width: 200px;
    height: 200px;
    border: 5px solid #f53c5e;
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
    color: #f53c5e;
}
</style>