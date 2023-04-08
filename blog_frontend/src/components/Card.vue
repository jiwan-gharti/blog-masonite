<script setup>
import {useStore}  from 'vuex'

    defineProps({
        data: Object
    })

    const store = useStore();

    console.log("name-------store-------",store.state.auth.name)

</script>

<template>
    <main>
        <RouterLink :to='`/blogs/${data.id}`'>
            <div class="blog-container">
                <img src="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg" alt="" />
                <div class="blog-text-section">
                    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Veniam aliquid aperiam, adipisci, unde libero, expedita impedit voluptatibus inventore delectus possimus illo ea! Facere reiciendis provident accusamus aliquam dolorum, veniam deleniti.</p>
                    <p>04/06/2023</p>
                </div>
            </div>
        </RouterLink>
    </main>
</template>


<style scoped>

    main a{
        margin: 10px;
    }

    .blog-container{
        width: 300px;
        margin: 1rem 1rem 1rem 0;
    }
    .blog-container img{
        width: 100%;
    }

    .blog-text-section p:first-child{
        text-align: justify;
    }
    .blog-text-section p:last-child{
        color: gray;
        margin-top: 5px;
    }
    a{
        list-style: none;
        text-decoration: none;
    }
   
</style>