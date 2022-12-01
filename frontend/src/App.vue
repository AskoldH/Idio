<script setup>
import axios from 'axios';
import BackGround from "./components/Backgroud/Background.vue";
const API_URL = 'http://localhost:8000';
</script>

<template>
    <BackGround/>
    <router-view/>
    <!--  <notifications/>-->
</template>