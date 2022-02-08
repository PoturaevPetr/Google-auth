<template>
	<div class="container">
		<table class="table table-hover">
			<thead>
				<tr>
					<th scope="col">Услуга</th>
					<th scope="col">Стоимость</th>
					<th scope="col">Статус</th>
					<th></th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(service, index) in SERVICES" :key="index">
					<td>{{service.service}}</td>
					<td>{{service.price}}</td>
					<td>{{service.status}}</td>
					<td>
						<button v-if="(service.status==='Отключена')" type="button" class="btn btn-warning btn-sm" @click="Activate(service)">Подключить</button>
						<button v-else type="button" class="btn btn-danger btn-sm" @click="Activate(service)">Отключить</button>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	data() {
		return{
			SERVICES: [],
		}
	},
	methods: {
		Activate(postData) {
			const path = 'http://localhost:5000/services'
			axios.post(path, postData)
				.then(() => {
					this.getServices();
				})
		},
		getServices() {
			const path = 'http://localhost:5000/services'
			axios.get(path)
				.then((res) => {
					this.SERVICES = res.data.data_services;
				})
		}
	},
	created() {
		this.getServices();
	}
};
</script>