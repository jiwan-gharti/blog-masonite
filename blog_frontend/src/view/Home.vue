<script setup>
    import { onMounted, ref} from 'vue';
    import Card from "../components/Card.vue";
    import AxiosInstance from '../axios';


    const cards = ref([]);

    onMounted(()=>{
        AxiosInstance.get('/blogs')
        .then(response => cards.value = response.data)
    })

</script>

<template>
    <main>
        <div class="card__wrapper">
            <Card v-for="(data, key) in cards" :data="data" :key="key" />
        </div>
    </main>
</template>

<style scoped>
    .card__wrapper{
        width: 1000px;
        display: flex;
        flex-wrap: wrap;
        justify-content: start;
    }
</style>