<script setup>
import { onMounted, ref } from 'vue';
import axiosInstance from '../axios';
import routes from '../routes';
import { useRoute } from 'vue-router';


    const blog = ref([])
    const route = useRoute();

    onMounted(()=>{
        axiosInstance.get(`/blogs/${route.params.id}`)
        .then((response)=>console.log(response.data))
    })

</script>

<template>
    <div class="blog__detail__container">
        <div class="blog__detail-image">
            <img src="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg" alt="blogimage" />
        </div>
        <div class="blog__detail-description">
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Atque maxime 
                esse qui provident nam. Suscipit, dolores nesciunt fuga sequi adipisci tempora mollitia ullam.
                Modi inventore neque exercitationem similique provident. A?

                Lorem, ipsum dolor sit amet consectetur adipisicing elit. Atque maxime 
                esse qui provident nam. Suscipit, dolores nesciunt fuga sequi adipisci tempora mollitia ullam.
                Modi inventore neque exercitationem similique provident. A?
                <br>
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nisi ipsam facere debitis ex quis harum unde id facilis officia culpa obcaecati repudiandae adipisci fuga vel, asperiores iste hic repellat pariatur.
            
            </p>
        </div>
    </div>

</template>

<style scoped>

    .blog__detail-description{
        color: black;
        text-align: justify;
    }

</style>