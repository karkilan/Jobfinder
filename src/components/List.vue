<template>
  <div class="container">
    <b-jumbotron class="header-title">
      <div class="job-title">
        <h2>Find your jobs</h2>
        <div class="title-icon"></div>
      </div>

      <div class="jobs-list">
        <div class="jobs">
          <b-list-group>
            <b-list-group-item class="flex-column align-items-start stop" v-for="job in job_list" v-bind:key="job.id">
              <div class="job">
                <b-container class="bv-example-row">
                  <b-row class="job-top">
                    <b-col>
                      <b-media left-align vertical-align="center">
                        <template >
                          <b-img blank blank-color="#ccc" width="80" alt="placeholder"></b-img>
                        </template>
                      </b-media>
                    </b-col>
                    <b-col>
                      <h5>{{ job.job_name}}</h5>
                      <p>{{ job.company_name }}</p>
                    </b-col>
                    <b-col><p>{{ job.location }}</p></b-col>
                    <b-col><p>₹{{ job.salary }}/m</p></b-col>
                    <b-col><p>{{ job.job_type }}</p></b-col>
                  </b-row>

                  <b-row class="job-bottom">
                    <b-col cols="6" md="3"><p><span class="mw-e">Experience :</span> {{ job.experiance }}</p></b-col>
                    <b-col cols="6" md="7"><p><span class="mw-e">Note : {{ job.notes }}</span></p></b-col>
                    <b-col cols="6" md="2"><router-link :to="{ name: 'Apply', params: { id: job.id } }">Apply Job</router-link></b-col>
                  </b-row>
                </b-container>
              </div>
            </b-list-group-item>
          </b-list-group>
        </div>
      </div>
    </b-jumbotron>
  </div>
</template>

<script>
export default {
  name: 'List',
  props: {
  },
  data () {
    return {
      job_list: ''
    }
  },
  mounted () {
    this.axios.get('http://localhost:8000/jobs/')
      .then((response) => {
        console.log(response.data)
        this.job_list = response.data
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  width: 100%;
  height: 100%;
}
.header-title {
  margin-top: 40px;
}
.mb-0 {
  color: #fafafa;
}
.title-icon {
  position: relative;
  margin-top: 25px;
}
.title-icon::before {
  content: "";
  position: absolute;
  width: 80px;
  height: 2px;
  background: #42b983;
  left: 0px;
  right: 0px;
  top: 50%;
  -webkit-transform: translateY(-50%);
  transform: translateY(-50%);
  margin: 0px auto;
}
.rt-s {
  background-color: #f8f9fa;
}
.job-list {
  padding-top: 50px;
}
.job {
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.13);
  border-radius: 5px;
}
.stop {
  padding: 0!important;
  margin-top: 40px;
}
.bv-example-row p {
  font-size: 14px;
  color: #6c757d;
}
.job-bottom {
  background-color: #f8f9fa!important;
  padding: 1rem;
  margin-top: 35px;
  text-align: left;
}
.col-6 a {
  color: #42b983;
}
.job-top {
  padding-top: 50px;
}
.mw-e {
  color: black;
  font-size: 15px;
  font-weight: 400;
}
</style>
