<template>
	<div id="app">
		<div>
			<router-view/>
		</div>
	</div>
</template>

<script>
import "./router.js";
//import axios from 'axios';
//import router from "./router.js";
//import Autorisation from './components/Autorisation.vue'
//import room from './components/Room.vue'
//import axios from 'axios'
export default {
	name: 'App',
	//created(){
	//	const path = 'http://localhost:5000/'
	//	axios.get(path);
	//}

		//router.push({name: 'Autorisation'})
	
	//components: {
	//	Autorisation,
		//room
	//},
};
</script>
