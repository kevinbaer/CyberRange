<template>
  <div class="container">
    <div class="mb-4">
      <h1>Challenges</h1>
    </div>
    <div class="row">
      <div v-for="(challengeTeams, challenge) in challenges" :key="challenge" class="col-md-4 mb-4">
        <div class="card">
          <div class="challenge">
            <img :src="`/assets/icons/challenges/${mapping[challenge]}.svg`" alt="" class="card-img-top">
            <!-- Only display team sticker if there's a winning team -->
            <img v-if="challengeTeams.length > 0" :src="`/assets/icons/school_logos/${challengeTeams[0]}.svg`" alt="Top Team Logo" class="team-logo rounded-border">
          </div>
          <div class="card-body">
            <h5 class="card-title">{{ challenge }}</h5>
            <p>Winning Teams:</p>
            <!-- Bootstrap dropdown -->
            <div class="dropdown">
              <button class="btn dropdown-toggle w-100 dropdown-btn" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                {{ challengeTeams.length > 0 ? challengeTeams[0] : 'No Winning Team' }}
              </button>
              <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <!-- Display the top team first, then the rest of the teams -->
                <li v-if="challengeTeams.length > 0" :key="0">
                  <a class="dropdown-item" href="#">
                    {{ '#' + 1 + ' ' + (challengeTeams[0] ? challengeTeams[0] : 'No Winning Team') }}
                  </a>
                </li>
                <li v-for="(team, index) in challengeTeams.slice(1)" :key="index + 1">
                  <a class="dropdown-item" href="#">
                    {{ '#' + (index + 2) + ' ' + (team ? team : 'No Winning Team') }}
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
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
        // const response = await axios.get('http://localhost:5000/api/mapping');
        const response = await axios.get('https://leaderboarded.club/api/mapping');
        this.mapping = response.data;
      } catch (error) {
        console.error('Error fetching mapping data:', error);
      }
    },
    async fetchChallengesData() {
      try {
        const response = await fetch('https://leaderboarded.club/api/challenge_state');
        // const response = await fetch('http://localhost:5000/api/challenge_state');
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

.rounded-border {
  border: 2px solid #00BA31;
}

.dropdown-btn {
  color: white;
  border: 2px solid #00BA31;
  border-radius: 0px;
  background-color: #004F59;
}

.dropdown-btn:hover{
  background-color: white;
  color: black;
}
</style>
