//import Vue from 'vue'
//import Router from 'vue-router'
//import Profile from '../views/Profile.vue'
//import history from '../views/History.vue'
//import finance from '../views/Finance.vue'
//import services from '../views/Services.vue'
//
//Vue.use(Router)
//
//
//
//export default new Router({
//  routes: [
//  {name: 'Profile', path: '/Profile', component: Profile},
//  {name: 'History', path: '/history', component: history},
//  {name: 'Finance', path: '/finance', component: finance},
//  {name: 'Services', path: '/services', component: services}
//  ]
//})
import Vue from "vue";
import Router from "vue-router";
import Autorisation from "../components/Autorisation.vue"
import Room from "../components/Room.vue"
import Profile from '../views/Profile.vue'
import history from '../views/History.vue'
import finance from '../views/Finance.vue'
import services from '../views/Services.vue'

Vue.use(Router);

export default new Router({
  routes: [
  {path: "/Autorisation", name: "Autorisation", component: Autorisation},
  {path: "/Room", name: "Room", component: Room, 
  children: [
    {name: 'Profile', path: 'Profile', component: Profile},
    {name: 'History', path: 'history', component: history},
    {name: 'Finance', path: 'finance', component: finance},
    {name: 'Services', path: 'services', component: services}
    ]},
  ],
});