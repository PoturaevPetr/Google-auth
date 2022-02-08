<template>
	<div class="app">
		<nav class="navbar">
			<h3>Личный кабинет</h3>
			<div class="links">
				<a type="button" class="btn btn-danger" href="https://localhost:5000/logout">Выйти</a>
				<button type="button" class="btn btn-danger" @click='logout'>Выйти</button>
			</div>
		</nav>
		<div class="container">
			<div class="text-center ">
				<ul class="links row text-center d-flex flex-fill">
					<li class="col list-group-item">
						<router-link to='/Room/profile'>Профиль
							<a href="https://127.0.01:5000/user"></a></router-link>
					</li>
					<li class="col list-group-item">
						<router-link to="/Room/history">Платежи</router-link>
					</li>
					<li class="col list-group-item">
						<router-link to="/Room/finance">Баланс</router-link>
					</li>
					<li class="col list-group-item">
						<router-link to="/Room/services">Услуги</router-link>
					</li>
				</ul>
			</div>
		</div>
		<router-view/>
	</div>
</template>

<script>
import axios from 'axios'
import router from "../router.js";

export default {
	methods: {
		signup: () => {
			router.push({ name: "Autorisation" });
		},
		Exit() {
			const path = 'http://localhost:5000/Exit'
			axios.get(path)
				.then(() => {
					router.push({ name: "Autorisation" });
				})
		},
		logout() {
			const path = 'https://localhost:5000/logout'
			axios.get(path)
				.then((res) => {
					console.log(res);
				})
		}
	},
	created() {
		const path = 'https://localhost:5000/'
			axios.get(path)
				.then((res) => {
					console.log(res);
				})
	}
	

};
</script>
<style>
.links {
	margin: 0 0 0 0;
}
</style>