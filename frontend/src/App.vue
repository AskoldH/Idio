<script setup>
import axios from 'axios';
import BackGround from "./components/Backgroud/Background.vue";
import UserAuthentication from "./components/UserAuthentication/UserAuthentication.vue";
import IdioHeader from "./components/IdioHeader/IdioHeader.vue";
import IdioFooter from "./components/IdioFooter/IdioFooter.vue";
const API_URL = 'http://localhost:8000';
</script>

<template>
    <BackGround/>
    <UserAuthentication/>
    <IdioHeader/>
    <router-view/>
    <!-- <IdioFooter/> -->
    <!--  <notifications/>-->
</template>