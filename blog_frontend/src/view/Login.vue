<script setup>
    import {ref} from 'vue';
    import axiosInstance from '../axios';
    import router from '../routes';
    import { useStore } from 'vuex';

    const username = ref('');
    const password = ref('');

    const store = useStore();

    const handleSubmit = ()=>{
        console.log(username.value)
        console.log(password.value)

        const formData = new FormData()
        formData.append("username",username.value.trim())
        formData.append("password",password.value.trim())

        axiosInstance.post('auth',formData)
        .then(response => {
            localStorage.setItem('blog_secret_key',response.data['data'])
            router.push("/blogs")
            store.state.auth.is_authenticated = true
            
        }
        ).catch((error)=>{
            localStorage.removeItem("blog_secret_key")
            router.push("/login")
        }
        )

    }

</script>

<template>
    <div class="form_container">
        <h2>Login Page</h2>
        <form  @submit.prevent="handleSubmit" >
        <!-- <div class="form-wrapper"> -->
            <div>
                <label for="username">Username</label><br />
                <input id="username" name="username" type="text" v-model="username" />
            </div>
            <div>
                <label for="password">Passowrd</label><br />
                <input id="password" name="password" type="text" v-model="password" />
            </div>
            <div>
                <input value="Submit" type="submit" />
            </div>
        <!-- </div> -->
        </form>
    </div>
</template>


<style scoped>

    .form_container{
        padding: 1rem 0;

    }
    .form_container h2{
        color: green;
    }
    .form_container div{
        width: 100%;
    }
    .form_container label{
        font-size: 1.2rem;
        font-weight: 500;
    }
    .form_container input{
        width: 50%;
        margin: 5px 0;
        height: 2rem;
        padding: 0 10px;
        outline: none;
        border-radius: 5px;
    }
    .form_container input[type=submit]{
        width: 5rem;
        font-size: 1rem;
        color: white;
        background-color: green;
        border: none;
        cursor: pointer;
    }


</style>