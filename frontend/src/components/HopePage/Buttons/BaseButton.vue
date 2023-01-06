<template>
  <div v-bind:class="{ duolingo_button_container: !buttonInfo.isDisabled, duolingo_button_container_disabled: buttonInfo.isDisabled }">
    <div
      v-bind:class="{ duolingo_button: !buttonInfo.isDisabled, duolingo_button_disabled: buttonInfo.isDisabled }">
      {{ buttonInfo.label }}
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseButton",
  props: {
    buttonInfo: {
      type: Object
    }
  },
  created () {
    console.log(this.buttonInfo)
  }
}
</script>