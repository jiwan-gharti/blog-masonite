
<script setup>
import { RouterLink } from 'vue-router';
import router from './routes';
import { useStore } from 'vuex';
import axiosInstance from './axios';


    const store = useStore()
    



  const handleLogout = ()=>{
    if(localStorage.getItem('blog_secret_key')){

      localStorage.removeItem('blog_secret_key')
      axiosInstance.post("/logout")
      .then((response)=>router.push("/login"))
      .catch((response)=>router.push('/login'))
    }
    else{
      router.push("/login")
    }
  }
</script>

<template>
  <div class="mainWrapper">
    <h1>Blog App!</h1>
    <p>
    <nav>
      <li><router-link to="/register" ><span>Signup</span></router-link ></li>
        <li><router-link to="/login" v-if="!store.state.auth.is_authenticated"><span>Login</span></router-link ></li>
          <li><router-link to="/blogs" v-if="store.state.auth.is_authenticated"><span>Blogs</span></router-link ></li>
      <li @click="handleLogout" v-if="store.state.auth.is_authenticated"><span>Logout</span></li>
      </nav>
    </p>
    <main>
      <router-view/>
    </main>
  </div>

</template>


<style scoped>
  .mainWrapper{
    width: 1000px;
    margin: 0 auto;
  }
  main{
    margin: 10px 0;
  }

  nav{
    width:1000px;
    display: flex;
    gap: 20px;
    font-size: 1.2rem;
    background-color: cadetblue;
    line-height: 3rem;
  }
  nav  li{
    list-style: none;
    font-weight: 400;
    padding: 0 15px;
    border: none;
    text-transform: capitalize;
    text-decoration: none;
  }
  nav li:hover{
    background-color: green;
  }
  span{
    outline: none;
    color: white;
  }
</style>