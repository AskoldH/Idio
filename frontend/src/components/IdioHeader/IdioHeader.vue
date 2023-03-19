<template>
    <div class="header_container">
        <a class="hearder_logo_link" href="/#/home">
            <img class="header_logo" src="./../../assets/images/idio_logo_close.png" alt="Idio">
        </a>
        <div class="header_burger_container">
            <div class="burger-menu" :class="{ active: isActive }" @click="toggleActive()">
                <div class="bar"></div>
                <div class="bar"></div>
                <div class="bar"></div>
            </div>
            <div class="header_links_container" v-if="isActive">
            <TextContainer @click="goHome(); toggleActive()" class="header_home_button" v-bind:text="home_title"></TextContainer>
            <TextContainer @click="goGetCode(); toggleActive()" class="header_get_code_button" v-bind:text="get_code_title"></TextContainer>
            <TextContainer @click="goAbout(); toggleActive()" class="header_about_button" v-bind:text="about_title"></TextContainer>
            </div> 
        </div>
    </div>
</template>
  
<script>
import TextContainer from "./../HopePage/EduVideoTile/TextContainer.vue";

export default {
    components: { TextContainer },
    name: "IdioHeader",

    data() {
        return {
            home_title: "Hlavní okno",
            about_title: "O projektu",
            get_code_title: "Přihlášení",

            isActive: false,
        }   
    },
    methods: {    
        goHome() {
            this.$router.push('/home');
        },
        goGetCode() {
            this.$router.push('/get_use_code');
        },
        goAbout() {
            this.$router.push('/about');
        },
        toggleActive() {
            this.isActive = !this.isActive;
        }
    }
}
</script>