<script setup>
import { useRouter } from 'vue-router';
import { reactive, onMounted, watch, computed } from 'vue';
import axios from 'axios';
import { baseUrl } from '../main';
import { useStore } from 'vuex';

const router = useRouter();
const store = useStore();
const isLogin = computed(() => store.state.isLogin);
const email = computed(() => store.state.email);
const keyword = computed(() => store.state.keyword);
let user = email.value;
let productList = reactive([]);

watch(keyword, async (newKeyword) => {
  if(newKeyword!=''){
    try {
      const response = await axios.post(`${baseUrl}/search_product`, {
        keyword: newKeyword
      });
      productList.value = response.data.data.map((product) => {
        const startDate = formatDate(product.start_date);
        const endDate = formatDate(product.end_date);
        return {
          ...product,
          start_date: startDate,
          end_date: endDate
        };
      });
    } catch (error) {
      console.error(error);
    }
  }
  else{
    loadProductList()
  }
});

onMounted(() => {
  loadProductList();
});

const loadProductList = async () => {
  try {
    const response = await axios.post(`${baseUrl}/get_products_and_likes`, {
      user: user
    });
    productList.value = response.data.data.map((product) => {
      const startDate = formatDate(product.start_date);
      const endDate = formatDate(product.end_date);
      return {
        ...product,
        start_date: startDate,
        end_date: endDate
      };
    });
  } catch (error) {
    console.error(error);
  }
};

const formatDate = (dateString) => {
    const date = new Date(dateString);
    const month = date.toLocaleString('en-US', { month: 'short' });
    const day = date.getDate();
    return `${month} ${day}`;
};

const clickProduct = (product) => {
    router.push(`/product/${product.product_id}`);
};

const clickLike = (product)=>{
  loadProductList()
  if(!isLogin.value){
      router.push('/login');
  }
  else{
      axios.post(`${baseUrl}/update_likes`,{
          user: computed(() => store.state.email).value,
          product_id : product.product_id
      })
      .catch((err)=>{console.error(err)});
      loadProductList()
  }
};

</script>

<template>
    <div class="container">
        <div class="product-container" v-for="product in productList.value" :key="product.id">
            <div class="product-img-container" >
                <img class="product-img" :src="product.img" alt="" @click="clickProduct(product)">
                <div class="heart-container">
                    <font-awesome-icon icon="fa-solid fa-heart" class="heart" v-if="product.is_like" @click="clickLike(product)"/>
                    <font-awesome-icon icon="fa-regular fa-heart" class="heart" v-else @click="clickLike(product)"/>
                </div>
            </div>
            <div class="product-text">
                <tr class="product-title">
                    <td>{{ `${product.city}, ${product.country}` }}</td>
                </tr>
                <tr>
                    <td>{{ `${product.start_date} - ${product.end_date}` }}</td>
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
    cursor: pointer;
}

.product-img {
    border: 5px solid #3ca2f5;
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
    color:#3ca2f5;
}

.product-title{
    font-size: 25px;
}

.heart-container{
    background-color: white;
    border-radius: 0px 15px 0px 15px;
    border: 5px solid #3ca2f5;
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
    color: #3ca2f5;
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