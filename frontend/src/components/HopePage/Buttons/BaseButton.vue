<template>
  <div class="duolingo_button_container">
    <div class="duolingo_button">
      {{ buttonType }}
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseButton",
  props: {
    buttonType: {
      type: String
    }
  }
}
</script>