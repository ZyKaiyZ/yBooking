<script>
import { ref, reactive, watch } from "vue";
export default {
  setup() {
    const productData = reactive([
        {
            img: 'https://a0.muscache.com/im/pictures/cbfa814d-dd89-42c1-ab33-06470bff74d5.jpg?im_w=720',
            title: 'Fanlu Township, 台灣',
            date: '6-12 Jan',
            price: '3300',
            isLike: false
        },
        {
            img: 'https://a0.muscache.com/im/pictures/4a11ba2e-a04c-4f7a-8983-9a4bd4d1ee50.jpg?im_w=320',
            title: 'Ren\'ai Township, 台灣',
            date: '8-14 Jan',
            price: '4500',
            isLike: false
        },
        {
            img: 'https://a0.muscache.com/im/pictures/1727c4e5-5ac5-4a23-b607-0fba30985832.jpg?im_w=320',
            title: 'Puli Township, 台灣',
            date: '5-10 Jan',
            price: '4000',
            isLike: false
        },
    ]);
    
    const clickLike = (product)=>{
        product.isLike = product.isLike ? false : true ;
    }

    return { productData, clickLike };
  },
};
</script>

<template>
    <div class="container">
        <div class="product-container" v-for="product in productData" :key="product">
            <div class="product-img-container">
                <img class="product-img" :src="product.img" alt="">
                <div class="heart-container">
                    <font-awesome-icon icon="fa-solid fa-heart" class="heart" v-if="product.isLike" @click="clickLike(product)"/>
                    <font-awesome-icon icon="fa-regular fa-heart" class="heart" v-else @click="clickLike(product)"/>
                </div>
            </div>
            <div class="product-text">
                <tr class="product-title">
                    <td>{{ product.title }}</td>
                </tr>
                <tr>
                    <td>{{ product.date }}</td>
                </tr>
                <tr>
                    <td>${{ product.price }} TWD per night</td>
                </tr>
            </div>
        </div>
    </div>
</template>

<style scoped>
.container {
    display: flex;
    flex-wrap: wrap;
    background: white;
    padding: 100px 50px 100px 50px;
}

.product-container {
    display: inline;
    margin: 25px;
    width: 300px;
    height: 300px;
    box-sizing: border-box;
    position: relative;
    /* overflow:hidden; */
}

.product-img {
    border: 5px solid #f53c5e;
    border-radius: 20px;
    width: 99%;
    height: 100%;
    background-color: white;
    background-image: none;
    background-size: contain; 
    background-repeat: no-repeat;
    background-position: center;
}

.product-text {
    width: 100%;
    padding: 10px;
}

.product-text:hover{
    color:#f53c5e;
}

.product-title{
    font-size: 25px;
}

.heart-container{
    background-color: white;
    border-radius: 0px 15px 0px 15px;
    border: 5px solid #f53c5e;
    border-top: none;
    border-right: none;
    position: absolute;
    top: 4px;
    right: -2px;
    width: 40px;
    height: 40px;
    z-index: 0;
}

.heart{
    position: absolute;
    top: 6px;
    right: 8px;
    width: 25px;
    height: 25px;
}

.heart:hover{
    color: #f53c5e;
}

.product-img-container{
    transform:scale(1,1);transition: all 1s ease-out;
    width: 100%;
    height: 66%;
    margin-bottom: 20px;
}

.product-img-container:hover{
    transform:scale(1.1,1.1);
}
</style>