<template>
  <header class="nav-menu">
    <b-navbar toggleable="sm" type="light" variant="light" fixed="top">
      <b-navbar variant="faded" type="light">
        <img width="30px" src="../assets/logo.png" class="d-inline-block align-top" alt="Kitten">
        <b-navbar-brand>
          <router-link to="/">Jobfinder</router-link>
        </b-navbar-brand>
      </b-navbar>

      <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="nav-cen">
        <b-nav-item><router-link to="/">Home</router-link></b-nav-item>
        <b-nav-item><router-link to="/job-list">Job</router-link></b-nav-item>
      </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template #button-content>
              <b-avatar class="avatar"></b-avatar>
              <em v-if="candidate">candidate@screel.in</em>
              <em v-if="recruiter">recruiter@screel.in</em>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data () {
    return {
      candidate: true,
      recruiter: false,
      page: this.$route.name,
      value: 'Job'
    }
  },
  mounted () {
    if (this.page === this.value) {
      this.candidate = false
      this.recruiter = true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.nav-menu {
  width: 100%;
  height: 63px;
}
.fixed-top {
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.13);
}
.navbar-brand a {
  color: #42b983!important;
}
.navbar-brand {
  margin-left: 10px;
}
.black {
  color: black;
}
.avatar {
  margin-right: 10px;
  width: 35px!important;
  height: 35px!important;
}
.nav-item a {
  color: rgba(0, 0, 0, 0.5);
}
</style>
