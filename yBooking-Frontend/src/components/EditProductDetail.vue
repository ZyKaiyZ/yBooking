<script setup>
import Swal from 'sweetalert2'
import axios from 'axios';
import { useRouter } from 'vue-router';
import { onMounted, reactive, computed, ref } from 'vue';
import { baseUrl } from '../main';
import { useStore } from 'vuex';

const router = useRouter();
const store = useStore();
const email = computed(() => store.state.email);
const isLogin = computed(() => store.state.isLogin);
let user = email.value;
let productData = reactive({});
let product = reactive({});
let img = ref('');
let country = ref('');
let city = ref('');
let startDate = ref('');
let endDate = ref('');
let price = ref('');
let product_id = router.currentRoute.value.params.id;

function submitForm() {
    if (!isLogin.value) {
        router.push('/login');
    } else {
        Swal.fire(
            'Success',
            'Edit successfully',
            'success'
        );
        try {
            axios.post(`${baseUrl}/edit_product`, {
                product_id: product_id,
                user: user,
                country: country,
                city: city,
                start_date: startDate,
                end_date: endDate,
                price: price
            })
            .then(() => {
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
        productData.value = res.data.data;
        img = productData.value.img
        country = productData.value.country;
        city = productData.value.city;
        startDate = formatDate(productData.value.start_date);
        endDate = formatDate(productData.value.end_date);
        price = productData.value.price;
    } catch (error) {
        console.log(error);
    }
});
</script>

<template>
    <div class="container" v-if="productData.value">
        <img class="product-img" :src="img" alt="">
        <form @submit.prevent="submitForm" class="launch-container">
            <table class="product-info">
                <tr>
                    <td class="property">Country *</td>
                    <td colspan="2">
                        <input v-model="country" class="input" type="text">
                    </td>
                </tr>
                <tr>
                    <td class="property">City *</td>
                    <td colspan="2">
                        <input v-model="city" class="input" type="text">
                    </td>
                </tr>
                <tr>
                    <td class="property" rowspan="2">Date *</td>
                    <td>From</td>
                    <td>
                        <input v-model="startDate" class="input" type="date">
                    </td>
                </tr>
                <tr>
                    <td>To</td>
                    <td>
                        <input v-model="endDate" class="input" type="date">
                    </td>
                </tr>
                <tr>
                    <td class="property">Price *</td>
                    <td colspan="2">
                        <input v-model="price" class="input" type="number">
                    </td>
                </tr>
            </table>
            <button class="submit-btn" type="submit">Edit</button>
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

.launch-container {
    display: inline;
    padding: 30px;
    width: 400px;
    height: 338px;
    border: 5px solid #3ca2f5;
    border-radius: 0px 20px 20px 0px;
}

.product-info {
    width: 100%;
    height: 86%;
}

.property {
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

.input {
    border: 2px solid black;
    border-radius: 5px;
    cursor: default;
    width: 100%;
    padding: 5px;
}

.submit-btn {
    margin-top: 20px;
    width: 100px;
    height: 40px;
    border-radius: 20px;
    background: #3ca2f5;
    color: white;
    font-weight: bold;
    cursor: pointer;
    float: right;
}

.submit-btn:hover {
    transform: scale(1.05);
}

.submit-btn:active {
    transform: scale(1);
    box-shadow: inset 0 0 10px 1px rgba(0, 0, 0, .2);
}

.text {
    font-size: 30px;
}

.text-small {
    font-size: 25px;
}
</style>
