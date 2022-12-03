<script setup>
import axios from 'axios';
import BackGround from "./components/Backgroud/Background.vue";
import UserAuthentication from "./components/UserAuthentication/UserAuthentication.vue";
const API_URL = 'http://localhost:8000';
</script>

<template>
    <BackGround/>
    <UserAuthentication/>
    <img style="height: 5rem; transform: rotate(-5deg);" src="./assets/images/idio_logo_close.png">
    <router-view/>
    <!--  <notifications/>-->
</template>