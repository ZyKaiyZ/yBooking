<script setup>
import axios from 'axios';
import Swal from 'sweetalert2'
import { useRouter } from 'vue-router';
import { ref, computed } from 'vue';
import { baseUrl } from '../main';
import { useStore } from 'vuex';

const router = useRouter();
const store = useStore();
const email = computed(() => store.state.email);
let user = email.value;
const country = ref('');
const city = ref('');
const startDate = ref('');
const endDate = ref('');
const price = ref('');

function submitForm() {
    Swal.fire(
        'Success',
        'Your product has been launched',
        'success'
    )
    try {
        axios.post(`${baseUrl}/lanuch_product`, {
            country: country.value,
            city: city.value,
            start_date: startDate.value,
            end_date: endDate.value,
            price: price.value,
            img: 'https://grinews.com/news/wp-content/uploads/2022/07/ADDY3088.jpg',
            owner: user
        })
        .then(()=>{
            router.push('/');
        })
    } catch (error) {
        console.error(error);
    }
}

</script>
<template>
    <div class="container">
      <form @submit.prevent="submitForm" class="launch-container">
        <table class="product-info">
            <tr>
                <td class="property">Country *</td>
                <td colspan="2"><input v-model="country" type="text" class="input" required></td>
                <td rowspan="0" class="img-container">
                    <p class="img-text"><font-awesome-icon icon="fa-solid fa-arrow-up-from-bracket" />  Upload Image</p>
                </td>
                </tr>
            <tr>
                <td class="property">City *</td>
                <td colspan="2"><input v-model="city" type="text" class="input" required></td>
            </tr>
            <tr>
                <td class="property" rowspan="2">Date *</td>
                <td>From</td>
                <td><input v-model="startDate" type="date" class="input" required></td>
            </tr>
            <tr>
                <td>To</td>
                <td><input v-model="endDate" type="date" class="input" required></td>
            </tr>
            <tr>
                <td class="property">Price *</td>
                <td colspan="2"><input v-model="price" type="number" class="input" required>&nbsp; TWD</td>
            </tr>
        </table>
        <button class="submit-btn" type="submit">Launch</button>
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
    padding: 30px;
    display: inline;
    width: 700px;
    height: 400px;
    border: 5px solid #3ca2f5;
    border-radius: 20px;
}

.product-info{
    width: 100%;
    height: 90%;
}

.property{
    font-size: 30px;
    font-weight: bold;
    cursor: default;
}

.img-container{
    text-align: center;
    border: 1px black;
    border-style: dashed;
    cursor: pointer;
}
.img-text:hover {
    transform: scale(1.05);
}

.img-text:active {
    transform: scale(1);
    box-shadow: inset 0 0 10px 1px rgba(0, 0, 0, .2);
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
</style>
