<template>
    <BaseButton v-if="propsData.eduVideo.id" v-bind:buttonLabel="buttonBackLabel" class="back_button" />
    <BaseButton v-if="propsData.eduVideo.id" @click="postLearned(); reloadPage(); patchLastEduVideo();" v-bind:buttonLabel="buttonNextLabel" class="skip_button" />
    <BaseButton v-if="propsData.eduVideo.id" @click="postSkipped(); reloadPage(); patchLastEduVideo();" v-bind:buttonLabel="buttonSpipLabel" class="next_button" />
</template>

<script>

import BaseButton from "@/components/HopePage/Buttons/BaseButton.vue";
import "../../../assets/style/edu-video-tile.scss";
import "../../../assets/style/buttons.scss";

export default {
  name: "Buttons",
  components: { BaseButton },
  props: {
    propsData: {
      type: Object,
      default: () => ({}),
    }
  },
  data() {
    return {
      buttonNextLabel: "Umím",
      buttonSpipLabel: "Přeskočit",
      buttonBackLabel: "Zpět",
    }
  },
  created() {

  },
  methods: {
    postSkipped() {
      this.$axios.post("http://localhost:8000/api/edu-video-skip", { "edu_video_id": this.propsData.eduVideo.id, "cookie_value": this.propsData.cookieValue }).then((response) => console.log(response))
        .catch(error => console.log(error))
    },
    postLearned() {
      this.$axios.post("http://localhost:8000/api/edu-video-learn", { "edu_video_id": this.propsData.eduVideo.id, "cookie_value": this.propsData.cookieValue }).then((response) => console.log(response))
        .catch(error => console.log(error))
    },
    patchLastEduVideo() {
      this.$axios.patch("http://localhost:8000/api/idio-user", { "edu_video_id": this.propsData.eduVideo.id, "cookie_value": this.propsData.cookieValue }).then((response) => console.log(response))
        .catch(error => console.log(error))
    },
    goToLastVideo() {
      
    },
    reloadPage() {
      window.location.reload();
    },
  }
}
</script>