<template>
	<div class="app">
		<nav class="navbar">
			<h3>Здесь будет название проекта</h3>
			<div class="links">
				<a type="button" class="btn btn-light" href="https://127.0.0.1:5000/login">Вход</a>
			</div>
		</nav>
		<div class="container">
			<div class="row text-center justify-content-center">
				<div class="d-flex flex-column">
					<div  class="p-2">
						<h1 class="title">Добро пожаловать в "тестовое задание"</h1>
					</div>
					<div class="p-2">
						<h4 class="site-description">Здесь будет описание сайта</h4>
					</div>
					<div class="p-2">
						<a type="button" class="btn btn-success" href="https://127.0.0.1:5000/login">Вход</a>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<script>

import axios from 'axios';
import router from "../router.js";
export default {
	methods: {
		Login() {
			const path = 'http://localhost:5000/Login';
			if (this.LoginData.login == '' || this.LoginData.password == '') {
				this.message = 'Введите логин и пароль';
			} else {
				axios.post(path, this.LoginData)
					.then((res) => {
						if (res.data.message) {
							this.message = res.data.message;
						} else {
							this.hideModalLogin();
							this.Signin();
						}
					})
			}
			
		},
		Signin: () => {
			router.push({name: 'Profile'});
		},
		
		showModalLogin() {
			this.$refs['modal-login'].show();
		},
		hideModalLogin() {
			this.$refs['modal-login'].hide();
			this.message = '';
			this.LoginData.login = '';
			this.LoginData.password = '';
		},
		showModalRegister() {
			this.$refs['modal-register'].show();

		},
		hideModalRegister() {
			this.$refs['modal-register'].hide();
			this.message = '';
		},
		clearForm() {
			this.RegisterData.name = "";
			this.RegisterData.login = "";
			this.RegisterData.email = "";
			this.RegisterData.password1 = "";
			this.RegisterData.password2 = "";
		},
		postData() {
			const path = 'http://localhost:5000/Register';
			axios.post(path, this.RegisterData)
				.then((res) => {
					console.log(res.data);
					if (res.data.message) {
						this.message = res.data.message;
					} else {
						this.hideModalRegister();
						this.clearForm();
					}
				})

		},
		validPasswiord() {
			if (this.RegisterData.password1 != this.RegisterData.password2) {
				this.message = 'Пароли не соответствуют';
			} else {
				this.postData();
				
			}
		},
		Register() {
			if (this.RegisterData.name == '' || this.RegisterData.login == '' || this.RegisterData.email == '' || this.RegisterData.password1 == '' || this.RegisterData.password2 == '') {
				this.message = "Не все поля заполнены";
			} else {
				this.validPasswiord();


			}
		},
	},
};
</script>

<style>
.btn {
	margin: 5px;
}
.row {
	margin: 20% 0 0 0;
}
label {
 margin-bottom: 10px;
}
input {
	width: 300px;
	padding-top: 3px;
	margin-bottom: 20px; 
}
</style>
