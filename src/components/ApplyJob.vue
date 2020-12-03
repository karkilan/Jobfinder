<template>
    <div>
        <b-jumbotron>
            <div class="job-title">
              <h2>Apply for job</h2>
              <div class="title-icon">
              </div>
            </div>
            <div class="apply container">
                <b-list-group-item class="flex-column align-items-start apply-form">
                    <div>
                        <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                          <b-form-group id="input-group-1" label="Name" label-for="input-0">
                            <b-form-input
                              id="input-0"
                              v-model="form.name"
                              type="text"
                              required
                            ></b-form-input>
                          </b-form-group>

                          <b-form-group id="input-group-2" label="Department" label-for="input-0">
                            <b-form-input
                              id="input-0"
                              v-model="form.dept"
                              type="text"
                              required
                            ></b-form-input>
                          </b-form-group>

                          <b-form-group id="input-group-3" label="Email" label-for="input-0">
                            <b-form-input
                              id="input-0"
                              v-model="form.email"
                              type="email"
                              required
                            ></b-form-input>
                          </b-form-group>

                          <b-form-group id="input-group-4" label="Mobile" label-for="input-4">
                            <b-form-input
                              id="input-4"
                              v-model="form.mobile"
                              type="text"
                              required
                            ></b-form-input>
                          </b-form-group>

                          <b-form-group id="input-group-5" label="Name of College" label-for="input-5">
                            <b-form-input
                              id="input-5"
                              v-model="form.college"
                              type="text"
                              required
                            ></b-form-input>
                          </b-form-group>

                          <b-form-group id="input-group-6" label="Year of Passing" label-for="input-6">
                            <b-form-select
                              id="input-6"
                              v-model="form.passing"
                              :options="pass"
                              required
                            ></b-form-select>
                          </b-form-group>

                          <b-form-group id="input-group-7" label="Experiance" label-for="input-7">
                            <b-form-select
                              id="input-7"
                              v-model="form.experiance"
                              :options="exp"
                              required
                            ></b-form-select>
                          </b-form-group>

                          <b-form-group id="input-group-8" label="Notice Period" label-for="input-8">
                            <b-form-select
                              id="input-8"
                              v-model="form.notice"
                              :options="not"
                              required
                            ></b-form-select>
                          </b-form-group>

                          <div class="button">
                          <b-button type="submit" variant="dark">Submit</b-button>
                          <b-button type="reset" variant="danger">Reset</b-button>
                          </div>
                        </b-form>
                    </div>
                </b-list-group-item>
            </div>
        </b-jumbotron>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ApplyJob',
  data () {
    return {
      form: {
        name: '',
        dept: '',
        email: '',
        mobile: '',
        college: '',
        passing: null,
        experiance: null,
        notice: null
      },
      pass: [{ text: 'Select One', value: null }, '2020', '2019', '2018', '2017', '2016'],
      exp: [{ text: 'Select One', value: null }, '0', '1', '2', '3', '4'],
      not: [{ text: 'Select One', value: null }, 'Immediate', '1 Month', '2 Month', '3 Month'],
      show: true
    }
  },
  methods: {
    onSubmit () {
      console.log(this.$route.params.id)
      let applyJob = {
        name: this.form.name,
        dept: this.form.dept,
        email: this.form.email,
        mobile: this.form.mobile,
        college: this.form.college,
        passing: this.form.passing,
        experiance: this.form.experiance,
        notice: this.form.notice
      }
      axios.post('http://localhost:8000/jobs/' + this.$route.params.id + '/apply/', applyJob)
        .then((response) => {
          console.log(response)
        }).catch((err) => {
          console.log(err)
        })
    },
    onReset (evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.name = ''
      this.form.dept = ''
      this.form.email = ''
      this.form.mobile = ''
      this.form.college = ''
      this.form.passing = null
      this.form.experiance = null
      this.form.notice = null
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style>
.job-title {
  height: 57px;
}
.apply {
    border-radius: 5px;
    margin-top: 50px;
    width: 600px;
    margin-left: 350px;
}
.apply-form {
    box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.13);
    text-align: left;
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
.button {
  margin-top: 40px;
}
.btn-danger {
  margin-left: 20px;
}
</style>
