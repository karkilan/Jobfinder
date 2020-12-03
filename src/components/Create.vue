<template>
  <div class="create">
    <b-jumbotron class="create-list">
      <div class="job-title">
        <h2>Job List</h2>
        <div class="title-icon">
        </div>
      </div>
      <div class="add-btn">
        <div>
          <b-dropdown split id="dropdown-1" text="Select" class="m-md-2" variant="dark">
            <b-dropdown-item @click="add=true">Add</b-dropdown-item>
            <b-dropdown-item @click="getUpdateData" :disabled="Disabled">Edit</b-dropdown-item>
            <b-dropdown-item @click="show=true" :disabled="Disabled">Delete</b-dropdown-item>
          </b-dropdown>
        </div>
      </div>
      <div class="job-list">
        <v-table
          class="blueTable"
          :data="data"
          selectionMode="single"
          selectedClass="table-info"
          @selectionChanged="selectedRows = $event"
        >
          <thead slot="head">
          <th>Job Name</th>
          <th>Company Name</th>
          <th>Location</th>
          <th>Salary</th>
          <th>Job Type</th>
          <th>Experiance</th>
          <th>Notes</th>
          </thead>
          <tbody slot="body" @click="Change">
          <v-tr
            v-for="i in items"
            :key="i.id"
            :row="i.id"
          >
            <td>{{ i.job_name }}</td>
            <td>{{ i.company_name }}</td>
            <td>{{ i.location }}</td>
            <td>{{ i.salary }}</td>
            <td>{{ i.job_type }}</td>
            <td>{{ i.experiance }}</td>
            <td>{{ i.notes }}</td>
          </v-tr>
          </tbody>
        </v-table>
      </div>

      <div>
        <b-modal id="my-modal" v-model="add" title="Create Job" :header-bg-variant="headerBgVariant" :header-text-variant="headerTextVariant" hide-footer>
          <b-form @submit="Create">
            <div class="two-field">
              <b-form-group id="input-group-1" label="Job Name" label-for="input-1">
                <b-form-input
                  id="input-1"
                  v-model="value.job_name"
                  type="text"
                  required
                ></b-form-input>
              </b-form-group>
              <b-form-group id="input-group-2" class="space" label="Company Name" label-for="input-2">
                <b-form-input
                  id="input-2"
                  v-model="value.company_name"
                  required
                ></b-form-input>
              </b-form-group>
            </div>

            <b-form-group id="input-group-3" label="Location" label-for="input-3">
              <b-form-input
                id="input-3"
                v-model="value.location"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-4" label="Salary" label-for="input-4">
              <b-form-input
                id="input-4"
                v-model="value.salary"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-5" label="Job Type" label-for="input-5">
              <b-form-select
                id="input-5"
                v-model="value.job_type"
                :options="type"
                required
              ></b-form-select>
            </b-form-group>

            <b-form-group id="input-group-6" label="Experiance" label-for="input-6">
              <b-form-input
                id="input-6"
                v-model="value.experiance"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-7" label="Notes" label-for="input-7">
              <b-form-input
                id="input-7"
                v-model="value.notes"
              ></b-form-input>
            </b-form-group>
            <b-button type="submit" class="float-right" variant="dark">Submit</b-button>
          </b-form>
        </b-modal>
      </div>

      <div>
        <b-modal id="my-modal" v-model="edit" title="Update Job" :header-bg-variant="headerBgVariant" :header-text-variant="headerTextVariant" hide-footer>
          <b-form @submit="Update">
            <div class="two-field">
              <b-form-group id="input-group-1" label="Job Name" label-for="input-1">
                <b-form-input
                  id="input-1"
                  v-model="update.job_name"
                  type="text"
                  required
                ></b-form-input>
              </b-form-group>
              <b-form-group id="input-group-2" class="space" label="Company Name" label-for="input-2">
                <b-form-input
                  id="input-2"
                  v-model="update.company_name"
                  required
                ></b-form-input>
              </b-form-group>
            </div>

            <b-form-group id="input-group-3" label="Location" label-for="input-3">
              <b-form-input
                id="input-3"
                v-model="update.location"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-4" label="Salary" label-for="input-4">
              <b-form-input
                id="input-4"
                type="text"
                v-model="update.salary"
                required
              ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-5" label="Job Type" label-for="input-5">
              <b-form-select
                id="input-5"
                v-model="update.job_type"
                :options="Jobtype"
                required
              ></b-form-select>
            </b-form-group>

            <b-form-group id="input-group-6" label="Experiance" label-for="input-6">
              <b-form-input
                id="input-6"
                type="text"
                v-model="update.experiance"
                required
              ></b-form-input>

            </b-form-group>
            <b-form-group id="input-group-7" label="Notes" label-for="input-7">
              <b-form-input
                id="input-7"
                type="text"
                v-model="update.notes"
              ></b-form-input>
            </b-form-group>
            <b-button type="submit" class="float-right" variant="dark">Update</b-button>
          </b-form>
        </b-modal>

        <b-modal id="modal-sm" v-model="show" centered size="sm" title="Please Confirm" hide-footer>
          <p>Please confirm that you want to delete</p>
            <b-button type="submit" class="float-right" @click="Delete" variant="dark">Confirm</b-button>
        </b-modal>
      </div>
    </b-jumbotron>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Create',
  data () {
    return {
      Disabled: true,
      data: [],
      selectedRows: '',
      allowSelection: false,
      items: [],
      value: {
        job_name: '',
        company_name: '',
        location: '',
        salary: '',
        job_type: null,
        experiance: '',
        notes: ''
      },
      headerTextVariant: 'light',
      headerBgVariant: 'dark',
      type: [{text: 'Select Option', value: null}, 'Full Time', 'Part Time'],
      add: false,
      update: {
        job_name: '',
        company_name: '',
        location: '',
        salary: '',
        job_type: '',
        experiance: '',
        notes: ''
      },
      Jobtype: [{ text: 'Select One', value: null }, 'Full Time', 'Part Time'],
      edit: false,
      show: false,
      delete: '',
      up: ''
    }
  },
  mounted () {
    axios.get('http://localhost:8000/jobs/')
      .then((response) => {
        this.items = response.data
      })
  },
  methods: {
    Create () {
      let newJob = {
        company_name: this.value.company_name,
        job_name: this.value.job_name,
        location: this.value.location,
        salary: this.value.salary,
        job_type: this.value.job_type,
        experiance: this.value.experiance,
        notes: this.value.notes
      }
      axios.post('http://localhost:8000/jobs/', newJob)
        .then((response) => {
          console.log(response)
        })
      this.add = false
    },
    Update () {
      let updateJob = {
        company_name: this.update.company_name,
        job_name: this.update.job_name,
        location: this.update.location,
        salary: this.update.salary,
        job_type: this.update.job_type,
        experiance: this.update.experiance,
        notes: this.update.notes
      }
      this.up = this.selectedRows[0]
      axios.put('http://localhost:8000/job/' + this.up, updateJob)
        .then((response) => {
          console.log(response)
        })
      this.edit = false
    },
    getUpdateData () {
      var select = this.selectedRows[0]
      var url = 'http://localhost:8000/job/'
      let passid = url + select
      console.log(passid)
      axios.get(passid)
        .then((response) => {
          this.update = response.data
          // console.log(this.update)
        })
      this.edit = true
    },
    Delete () {
      this.delete = this.selectedRows[0]
      axios.delete('http://localhost:8000/jobs/' + this.delete)
        .then((response) => {
          console.log(response)
        })
      this.show = false
    },
    Change () {
      this.Disabled = false
    }
  }
}
</script>

<style scoped>
.create {
  height: 100%;
}
.create-list {
  margin-bottom: 0;
  height: 1000px;
}
.job-title {
  height: 57px;
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
.add-btn {
  float: right;
  margin-bottom: 20px;
}
#input-1, #input-2 {
  width: 225px;
}
.space {
  margin-left: 20px;
}
.two-field {
  display: flex;
  display: -webkit-box;
}
.blueTable {
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.13);
}
table.blueTable {
  border: 1px solid #212529;
  background-color: #EEEEEE;
  width: 100%;
  text-align: center;
  border-collapse: collapse;
}
table.blueTable th {
  border-color: #454d55;
  padding: 3px 2px;
}
table.blueTable td {
  border: 1px solid #dee2e6;
  padding: 3px 2px;
}
table.blueTable tbody td {
  font-size: 13px;
}
table.blueTable tr:nth-child(even) {
  background: #EEEEEE;
}
table.blueTable thead {
  background: #212529;
}
table.blueTable thead th {
  font-size: 15px;
  font-weight: bold;
  color: #FFFFFF;
  border-left: 1px solid #454d55;
  height: 50px;
}
table.blueTable tbody tr {
  height: 45px;
}
.table-info, .table-info > th, .table-info > td {
  background-color: rgba(0,0,0,.075)!important;
}
</style>
