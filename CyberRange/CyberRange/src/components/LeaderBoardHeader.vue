<template>
  <header class="bg-light">
    <div class="container">
      <h1 class="text-center text-success">{{ msg }}</h1>
      <nav class="navbar navbar-expand-lg navbar-light justify-content-center">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="#" @click.prevent="navigateTo('leaderboard')">Leaderboard</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" @click.prevent="navigateTo('history')">History</a>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
h1 {
  font-size: 2.6rem;
}

.nav-link {
  font-size: 1.2rem;
}
</style>
