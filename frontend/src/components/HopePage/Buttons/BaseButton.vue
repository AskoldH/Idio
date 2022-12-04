<template>
  <div class="duolingo_button_container">
    <div class="duolingo_button">
      {{ buttonLabel }}
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseButton",
  props: {
    buttonLabel: {
      type: String
    }
  }
}
</script>