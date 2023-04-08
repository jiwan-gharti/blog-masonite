import { createRouter,createWebHistory} from 'vue-router';
import store from '../store/store';

// import Login from "../view/Login.vue";
// import Home from "../view/Home.vue";
// import Register from "../view/Register.vue";


const Login = () => import('../view/Login.vue')
const Register = () => import('../view/Register.vue')
const Home = () => import('../view/Home.vue')
const BlogDetail = () => import('../view/BlogDetail.vue')

export const routes = [
    { 
        path: '/', 
        component: Login 
    },
    { 
        path: '/blogs', 
        component: Home,
        meta:{
            needsAuth: true
        }
    },
    { 
        path: '/login', 
        component: Login 
    },
    { 
        path: '/register', 
        component: Register 
    },
    {
        path: "/blogs/:id",
        name:'blogs',
        component: BlogDetail,
        meta:{
            needsAuth: true
        }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to,from, next)=>{
    if(to.meta.needsAuth){
        if(store.state.auth.is_authenticated){
            console.log('to.meta.path',to)
            if(to.path === "/login" || to.path === "/register"){
                console.log("insideeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                next(from)
            }else{
                next()
            }
        }else{
            next('/login')
        }
    }else{
        next()
    }

})


export default router;


