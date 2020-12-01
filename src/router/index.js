import Vue from 'vue'
import Router from 'vue-router'
import List from '@/components/List'
import Create from '@/components/Create'
import Apply from '@/components/Apply'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/job',
      name: 'list',
      component: List
    },
    {
      path: '/job-list',
      name: 'create',
      component: Create
    },
    {
      path: '/job/:id/apply',
      name: 'job',
      component: Apply
    }
  ]
})
