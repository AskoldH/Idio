<template>
    <BaseButton v-bind:buttonType="buttonTypes[1]" class="back_button"/>
    <BaseButton v-bind:buttonType="buttonTypes[0]" class="next_button"></BaseButton>
    <BaseButton v-bind:buttonType="buttonTypes[2]" class="skip_button"/>
</template>

<script>

import BaseButton from "@/components/HopePage/Buttons/BaseButton.vue";
import "../../../assets/style/edu-video-tile.scss";

export default {
  name: "Buttons",
  components: {BaseButton},
  props: {
    cookie_value: {
      type: String
    }
  },
  data() {
    return {
      buttonTypes: ["Přeskočit", "Zpět", "Umím"],
    }
  },
  created() {
    
  }
}
</script>