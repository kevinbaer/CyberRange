<template>
  <div>
    <h2>Challenges</h2>
  </div>
  <div class="container mt-5">
    <div class="row">
      <div v-for="(challengeTeams, challenge) in challenges" :key="challenge" class="col-md-4 mb-4">
        <div class="card">

          <div class="challenge">
            <img :src="`/assets/icons/challenges/${mapping[challenge]}.png`" alt="" class="card-img-top">
            <img :src="`/assets/icons/school_logos/${challengeTeams[0]}.png`" alt="Top Team Logo" class="team-logo">
<!--            <div class="university-stickers">-->
<!--              <div v-for="(team, index) in challengeTeams" :key="index" class="sticker-container">-->
<!--                <img :class="{'big-sticker': index === 0, 'small-sticker': index !== 0}"-->
<!--                     :src="`/assets/icons/school_logos/${team}.png`" alt="">-->
<!--              </div>-->
<!--            </div>-->
          </div>
          <div class="card-body">
            <h5 class="card-title">{{ challenge }}</h5>
            <p>Winning Teams:</p>
            <div class="dropdown">
              <Dropdown variant="outline-danger">
                <template #toggle> {{ challengeTeams[0]}}</template>
                <a v-for="(team, index) in challengeTeams" :key="index" class="dropdown-item" href="#">{{ team }} </a>
              </Dropdown>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Dropdown from "@/components/Dropdown.vue";

export default {
  components: {
    Dropdown,
  },
  data() {
    return {
      challenges: [],
      mapping: {}
    };
  },
  created() {
    this.fetchMappingData();
    this.fetchChallengesData();
    setInterval(this.fetchChallengesData, 10000);
  },
  methods: {
    async fetchMappingData() {
      try {
        // const response = await axios.get('https://leaderboarded.club/api/mapping');
        const response = await axios.get('http://localhost:5000/api/mapping');
        this.mapping = response.data;
      } catch (error) {
        console.error('Error fetching mapping data:', error);
      }
    },
    async fetchChallengesData() {
      try {
        // const response = await fetch('https://leaderboarded.club/api/challenge_state');
        const response = await fetch('http://localhost:5000/api/challenge_state');
        const data = await response.json();
        this.challenges = data;
      } catch (error) {
        console.error('Error fetching challenges:', error);
      }
    }
  }
}
</script>

<style scoped>
.team-logo {
  position: absolute;
  top: 10px;
  left: 10px;
  height: 50px;
  z-index: 1;
}


.university-stickers {
  position: absolute;
  top: 50%; /* shift the stickers up */
  transform: translateY(-50%); /* center the stickers vertically */
  width: 100%;
  display: flex;
  justify-content: center;
}

.sticker-container {
  transform: rotate(30deg); /* rotate the sticker container */
}

.big-sticker {
  width: 60%;
  border: 2px solid black;
  opacity: 0; /* make the sticker initially invisible */
  animation: slap-on 0.5s ease forwards; /* animate the sticker */
  transform: scale(0); /* initially scale the sticker down */
}

@keyframes slap-on {
  to {
    opacity: 1; /* make the sticker fully visible at the end of the animation */
    transform: scale(1); /* scale the sticker up to its original size */
  }
}

</style>
