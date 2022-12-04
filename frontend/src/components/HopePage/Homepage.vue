<template>
  <Buttons v-bind:propsData="propsData" />
  <EduVideoTile v-bind:propsData="propsData" />
</template>

<script>
import "./../../../src/assets/style/edu-video-tile.scss";
import "./../../../src/assets/style/buttons.scss";
import "./../../../src/assets/style/text-containers.scss";
import EduVideoTile from "./EduVideoTile/EduVideoTile.vue";
import Buttons from "./Buttons/Buttons.vue";
export default {
  name: "Homepage",
  components: { EduVideoTile, Buttons },
  data() {
    return {
      propsData:
      {
        cookieValue: '',
        eduVideo: {
          video_file: null,
          name: null,
          source_info: null,
        },
      },
    }
  },
  created() {
    this.propsData.cookieValue = this.getCookie("id")
    this.fetchVideo()
  },
  methods: {
    getCookie(name) {
      // gets cookie value by cookie name
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    },
    fetchVideo() {
      this.$axios.get("http://localhost:8000/api/edu-video?user-cookie-value=" + this.propsData.cookieValue).then((response) => {
        this.propsData.eduVideo = response.data
        this.propsData.eduVideo.video_file = "http://localhost:8000" + this.propsData.eduVideo.video_file
      }, (error) => {
        console.log(error);
      })
    },
  }
}
</script>