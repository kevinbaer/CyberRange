<template>
  <header style="background-color: #004F59; padding: 20px 0;">
    <div class="container d-flex justify-content-between align-items-center">
      <!-- Logo -->
      <h1 class="logo">CyberRange</h1>
      <!-- Navigation -->
      <!--<nav class="navbar navbar-expand-lg navbar-light">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
               Use router-link to navigate to the main page
              <router-link to="/" class="nav-link text-white">Leaderboard</router-link>
            </li> 
          </ul>
        </div>
      </nav>-->
    </div>
  </header>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
  msg: {
    type: String,
    required: true
  }
});
</script>

<style scoped>
header {
  margin-top: 0;
  height: 10%;
}

.logo {
  font-family: 'GlitchGoblin', sans-serif;
  font-size: 3rem; /* Adjust the size as needed */
  color: #fff; /* Adjust the color as needed */
  margin: 0; /* Remove default margin */
  border-left: 5px solid #00BA31;
  padding-left: 10px;
}

@font-face {
  font-family: 'GlitchGoblin';
  src: url('fonts/GlitchGoblin-2O87v.ttf') format('truetype');
}


.nav-link {
  font-size: 1.5rem;
  text-decoration: none;
}

.nav-link:hover {
  text-decoration: underline;
}
</style>
