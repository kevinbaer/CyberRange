<template>
  <header>
    <LeaderBoardHeader />
  </header>
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-4 mb-4">
        <main>
          <LeaderBoard />
        </main>
      </div>
      <div class="col-md-8 mb-4">
        <main>
          <Challenges />
        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
  import LeaderBoard from './components/LeaderBoard.vue'
  import LeaderBoardHeader from './components/LeaderBoardHeader.vue'
  import Challenges from './components/Challenges.vue'
</script>
