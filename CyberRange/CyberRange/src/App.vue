<template>
  <div>
    <header>
      <LeaderBoardHeader />
    </header>
    <div class="container mt-5">
      <div class="row">
        <div class="col-md-4 mb-4 pr-md-5"  style="background-color: #EDEDED;">
          <main>
            <ScoreLeaderboard />
          </main>
        </div>
        <div class="col-md-8 mb-4 pl-md-5">
          <main>
            <Challenges />
          </main>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import LeaderBoard from './components/LeaderBoard.vue'
import ScoreLeaderboard from './components/ScoreLeaderboard.vue'
import LeaderBoardHeader from './components/LeaderBoardHeader.vue'
import Challenges from './components/Challenges.vue'
</script>

<style scoped>
  /* Default styles for the main element */
  main {
    padding-bottom: 20px; /* Default padding */
  }

  /* Media query for small screens (max-width: 768px) */
  @media only screen and (max-width: 768px) {
    main {
      padding-bottom: 40px; /* Adjust padding for small screens */
      padding-top: 25px;
    }
  }
</style>