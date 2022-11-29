<script setup>
import axios from 'axios'

const API_URL = 'http://localhost:8000';
import BackGround from "./components/Backgroud/Background.vue";
</script>

<template>
    <BackGround/>
    <router-view/>
    <!--  <notifications/>-->
</template>