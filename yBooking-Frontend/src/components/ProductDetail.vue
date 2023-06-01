<script setup>
import Swal from 'sweetalert2'
import axios from 'axios';
import { useRouter } from 'vue-router';
import { onMounted, reactive, ref, computed } from 'vue';
import { baseUrl } from '../main';
import { useStore } from 'vuex';

const router = useRouter();
const store = useStore();
const email = computed(() => store.state.email);
const isLogin = computed(() => store.state.isLogin);
let user = email.value;
let product = reactive([]);
let productLike = reactive([]);
let product_id = router.currentRoute.value.params.id;

function submitForm() {
    if(!isLogin.value){
        router.push('/login');
    }
    else{
        Swal.fire(
            'Success',
            'Order successfully',
            'success'
        );
        try {
            axios.post(`${baseUrl}/order_product`, {
                product_id: product_id,
                user: user
            })
            .then(()=>{
                router.push('/');
            })
        } catch (error) {
            console.error(error);
        }
    }
}
function formatDate(dateString) {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

onMounted(async () => {
  try {
    const res = await axios.post(`${baseUrl}/get_product`, {
      product_id: product_id
    });
    product.value = res.data.data;
    product.value.start_date = formatDate(product.value.start_date);
    product.value.end_date = formatDate(product.value.end_date);
  } catch (error) {
    console.log(error);
  }
  try {
    const res = await axios.post(`${baseUrl}/get_like`, {
      product_id: product_id,
      user : user
    });
    productLike.value = res.data.data;
  } catch (error) {
    console.log(error);
  }
});

</script>

<template>
    <div class="container" v-if="product.value">
        <img class="product-img" :src="product.value.img" alt="">
        <form @submit.prevent="submitForm" class="launch-container">
            <table class="product-info">
                <tr>
                    <td class="property">Country *</td>
                    <td colspan="2" class="text">{{ product.value.country }}</td>
                </tr>
                <tr>
                    <td class="property">City *</td>
                    <td colspan="2" class="text">{{ product.value.city }}</td>
                </tr>
                <tr>
                    <td class="property" rowspan="2">Date *</td>
                    <td>From</td>
                    <td class="text-small">{{ product.value.start_date }}</td>
                </tr>
                <tr>
                    <td>To</td>
                    <td class="text-small">{{ product.value.end_date }}</td>
                </tr>
                <tr>
                    <td class="property">Price *</td>
                    <td colspan="2" class="text-small">{{ product.value.price }} &nbsp; TWD </td>
                </tr>
            </table>
            <button class="submit-btn" type="submit" v-if="productLike.value">Order</button> 
        </form>
    </div>    
</template>
<style scoped>
.container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    padding: 50px 30px 100px 50px;
}

.launch-container{
    display: inline;
    padding: 30px;
    width: 400px;
    height: 338px;
    border: 5px solid #3ca2f5;
    border-radius: 0px 20px 20px 0px;
}

.product-info{
    width: 100%;
    height: 86%;
}

.property{
    font-size: 30px;
    font-weight: bold;
    cursor: default;
}

.product-img {
    border: 5px solid #3ca2f5;
    border-right: none;
    border-radius: 20px 0px 0px 20px;
    width: 545px;
    height: 398px;
    background-color: white;
    background-image: none;
    background-size: contain; 
    background-repeat: no-repeat;
    background-position: center;
}

.input{
    border: 2px solid black;
    border-radius: 5px;
    cursor: default;
}

.submit-btn{
    margin: 20px;
    width: 100px;
    height: 40px;
    border-radius: 20px;
    background: #3ca2f5;
    color: white;
    font-weight: bold;
    margin: 15px 300px 0px 300px;
    cursor: pointer;
}
.submit-btn:hover {
    transform: scale(1.05);
}

.submit-btn:active {
    transform: scale(1);
    box-shadow: inset 0 0 10px 1px rgba(0, 0, 0, .2);
}

.text{
    font-size: 30px;
}

.text-small{
    font-size: 25px;
}
</style>
