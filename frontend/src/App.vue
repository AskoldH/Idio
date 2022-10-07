<script setup>
import axios from 'axios'
const API_URL = 'http://localhost:8000'
import EduVideoTile from "./components/EduVideoTile/EduVideoTile.vue";
</script>

<template>
  <EduVideoTile/>
  <notifications/>
</template>
