<template>
  <div>
    <h2>Challenges</h2>
  </div>
  <div class="container mt-5">
    <div class="row">
      <div class="col-md-4 mb-4" v-for="(challengeTeams, challenge) in challenges" :key="challenge">
        <div class="card">

          <img :src="getChallengeImage(challenge)" class="card-img-top" alt="Challenge Image">
          
          <!--<img v-if="challengeTeams[0]" :src="getTeamLogo(challengeTeams[0])" class="team-logo" alt="Top Team Logo">-->
          <img src="../assets/school_logos/cwi.png" class="team-logo" alt="Top Team Logo">
          
          <div class="card-body">
            <h5 class="card-title">{{ challenge }}</h5>
            <p>Winning Teams:</p>
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton-{{index}}" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                {{ challengeTeams[0] }}
              </button>
              <div class="dropdown-menu" aria-labelledby="dropdownMenuButton-{{index}}">
                <a class="dropdown-item" href="#" v-for="(team, index) in challengeTeams" :key="index">{{ team }}</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      challenges: {},
      teams: ["BSU", "CEI", "CSI", "CWI", "ISU", "ICSC", "NIC", "UI"],
      school_logo_mapping: {
        "BSU": "bsu.jpg",
        "CEI": "cei.png",
        "CSI": "csi.png",
        "CWI": "cwi.png",
        "ISU": "isu.png",
        "ICSC": "Icsc.png",
        "NIC": "nic.png",
        "UI": "ui.jpg"
      }
    };
  },
  created() {
    this.fetchChallenges();
  },
  methods: {
    async fetchChallenges() {
      try {
        const response = await fetch('http://localhost:5000/update');
        const data = await response.json();
        this.challenges = data;
      } catch (error) {
        console.error('Error fetching challenges:', error);
      }
    },
    getChallengeImage(challenge) {

      return `https://placehold.co/200`;
    },
    getTeamLogo(team) {

      if (this.school_logo_mapping.hasOwnProperty(team)) {
        return `/assets/school_logos/${this.school_logo_mapping[team]}`;
      } else {
        return '';
      }
    }
  }
};
</script>

<style scoped>
.team-logo {
  position: absolute;
  top: 10px;
  left: 10px;
  height: 50px;
  z-index: 1;
}
</style>
