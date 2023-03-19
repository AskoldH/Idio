<template>
    <div class="info_about_container">
        <TextContainer class="info_about_title" v-bind:text="info_about_title"></TextContainer>
        <TextContainer class="info_about_text" v-bind:text="info_about_text"></TextContainer>
    </div>
</template>
  
<script>
import TextContainer from "./../HopePage/EduVideoTile/TextContainer.vue";

export default {
    components: { TextContainer },
    name: "About",

    data() {
        return {
            info_about_title: "Informace o projektu",
            info_about_text: "Tento projekt je dlouhodobou maturitní prací Askolda Horčičky, studenta na SPŠE Olomouc. Při vývoji této webové aplikace jsem se zaměřil na jednoduchost používání, přehlednost a jednolitý, nenarušující, ne extra výrazný design, který je ale příjemný a očekávaný u tohoto typu aplikace."
        }   
    },
    methods: {    

    }
}
</script>