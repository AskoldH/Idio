<template>
  <div class="navbar" :style="{ width: navbarWidth}">
    <span class="collapse-icon" @click="toggleNavbar">
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<script>
import { collapsed, toggleNavbar, navbarWidth} from "./state";

export default {
  setup() {
    return { collapsed, toggleNavbar, navbarWidth}
  }
}
</script>

<style>
:root {
  --navbar-bg-color: #2f855a;
  --navbar-item-hover: #38a169;
  --navbar-item-active: #276749;
}
</style>

<style scoped>
.navbar {
  color: white;
  background-color: var(--navbar-bg-color);

  float: left;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;

  transition: 0.3s ease;

  display: flex;
  flex-direction: column;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;
}
</style>
