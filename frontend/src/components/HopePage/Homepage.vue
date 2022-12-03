<template>
  <Buttons v-bind:cookie_value="cookie_value" />
  <EduVideoTile v-bind:cookie_value="cookie_value" />
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
      cookie_value: '',
    }
  },
  created() {
    this.cookie_value = this.getCookie("id")
  },
  methods: {
    getCookie(name) {
      // gets cookie value by cookie name
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    }
  }
}
</script>