import { createRouter, createWebHistory } from 'vue-router';
const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: ()=>import("./components/Home.vue")
        },
        {
          path: '/login',
          name: 'login',
          component: ()=>import("./components/Login.vue")
        },
        {
            path: '/signup',
            name: 'signup',
            component: ()=>import("./components/SignUp.vue")
        },
        {
            path: '/product',
            name: 'product',
            component: ()=>import("./components/Product.vue")
        }
    ],
});
export default router;
