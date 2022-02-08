<template>
	<div class="container">
		<table class="table table-hover">
			<thead>
				<tr>
					<th scope="col">Дата</th>
					<th scope="col">Услуга</th>
					<th scope="col">Статус</th>
					<th></th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(payment, index) in PAYMENTS" :key="index">
					<td>{{payment.data}}</td>
					<td>{{payment.service}}</td>
					<td>{{payment.status}}</td>
					<td>
						<button v-if="(payment.status==='Не оплачено')" type="button" class="btn btn-warning btn-sm" @click="defPayment(payment)">Оплатить</button>
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
		return {
			PAYMENTS: [],
		}
	},
	methods: {
		defPayment(postData) {
			const path = 'http://localhost:5000/payments'
			axios.post(path, postData)
				.then((res) => {
					console.log(res.data);
					this.getPayments();
				})
		},
		getPayments(){
			const path = 'http://localhost:5000/payments'
			axios.get(path)
				.then((res) => {
					this.PAYMENTS = res.data.data_payments;
				})
		}
	},
	created() {
		this.getPayments();
	}

};
</script>