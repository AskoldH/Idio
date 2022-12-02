<template>
  <div class="text_container">
    <div class="text">{{ text }}</div>
  </div>
</template>
  
<script>
export default {
  name: "TextContainer",
  data() {
    return {
    }
  },
  props: {
    text: {
      type: String
    }
  }
}
</script>