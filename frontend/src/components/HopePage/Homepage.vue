<template>
  <Buttons/>
  <EduVideoTile/>
</template>

<script>
import "./../../../src/assets/style/edu-video-tile.scss";
import "./../../../src/assets/style/buttons.scss";
import EduVideoTile from "./EduVideoTile/EduVideoTile.vue";
import Buttons from "./Buttons/Buttons.vue";
export default {
  name: "Homepage",
  components: {EduVideoTile, Buttons},
}
</script>