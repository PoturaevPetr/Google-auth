<template>
	<div class="container">
		<button  type="button" class="btn btn-secondary" @click="showModalDetails">Отправить детализацию</button>
		<br><br>
		<table class="table table-hover">
			<thead>
				<tr>
					<th scope="col">Дата</th>
					<th scope="col">Услуга</th>
					<th scope="col">Списание</th>
					<th scope="col">Баланс</th>
					<th></th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(hist, index) in HISTORY" :key="index">
					<td>{{hist.date}}</td>
					<td>{{hist.service}}</td>
					<td>-{{hist.price}} руб.</td>
					<td>{{hist.balance}} руб.</td>
				</tr>
			</tbody>
		</table>
		<b-modal ref="modal-details" hide-footer title="Детализация">
			<alert v-if="message" :message="message"></alert>
			<div class="container">
				<div class="row justify-content-center">
					<div>
						<div>
							<label for="email">Ваш E-mail</label>
						</div>
						<div>
							<input type="email" name="email" placeholder="Введите email" v-model="sender.email">
						</div>
						<div>
							<label for="time" class="cols-sm-2 control-label">Период отчетности</label> 
							<select name="time" class="form-control form-control-sm">
								<option>-</option>
								<option>За день</option>
								<option>За неделю</option>
								<option>За две недели</option>
								<option>За месяц</option>
							</select>
						</div>
						<div>
							<label for="name" class="cols-sm-2 control-label">Логин </label> 
						</div>
						<div>
							<input type="text" name="login"  placeholder="Введите ваш логин" v-model="sender.login">
						</div>
						<div>
							<label for="pass1">Пароль</label>
						</div>
						<div>
							<input type="password" name="pass1" placeholder="Введите пароль" v-model="sender.password">
						</div>
						<div class="p-2 text-center">
							<button tupe="button" class="btn btn-success" @click="sendDetails(sender)">Отправить</button>
						</div>
					</div>
				</div>
			</div>
		</b-modal>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			message: '',
			HISTORY: [],
			USER: [],
			sender: {
				email: '',
				login: '',
				password: '',
				period: ''
			}
		}
	},
	methods: {
		sendDetails(sender) {
			const path = 'http://localhost:5000/sendDetails'
			axios.post(path, sender)
				.then(() => {
					this.hideModalDetails();
				})
		},
		getUser() {
			const path = 'http://localhost:5000/user'
			axios.get(path)
				.then((res) => {
					this.USER = res.data.data_user;
					this.sender.email = this.USER.email;
					console.log(this.USER.email);
				})
		},
		showModalDetails() {
			this.$refs['modal-details'].show();
			this.getUser();
		},
		hideModalDetails() {
			this.$refs['modal-details'].hide();
		},
		getHistory() {
			const path = 'http://localhost:5000/history'
			axios.get(path)
				.then((res) => {
					this.HISTORY = res.data.data_history;
					console.log(this.HISTORY);
				})
		},
	},
	created() {
		this.getHistory();
	}
};
</script>
