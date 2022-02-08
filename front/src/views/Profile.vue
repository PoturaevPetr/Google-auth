<template>
	<div class="container">
		<div class="info row">
			<img class="avatar" src="@/assets/avatar.jpg">
			<div class="col">
				<p>Ф.И.О: {{USER.name}}</p> 
				
				<p>Дата регистрации: {{USER.register}}</p>
				<p>E-mail: {{USER.email}}</p>
				<div>
					<p>Текущий баланс: {{USER.balance}} руб.</p>
					<button class="btn btn-warning btn-sm" @click="showModalBalance">Пополнить баланс</button>
				</div>
			</div>
		</div>
		<b-modal ref="modal-balance" title="Пополнить баланс"  hide-footer>
			<div class="container">
				<div class="user row">
					<div>
						<div class="credit-card-div">
							<div class="panel panel-default" >
								<div class="panel-heading">
									<div class="user row">
										<div class="col">
											<input type="text" class="form-control" placeholder="Введите номер карты"/>
										</div>
									</div>
									<div class="user row">
										<div class="col-md-3 col-sm-3 col-xs-3">
											<span class="help-block text-muted small-font" > Expiry Month</span>
											<input type="text" class="form-control" placeholder="MM" />
										</div>
										<div class="col-md-3 col-sm-3 col-xs-3">
											<span class="help-block text-muted small-font" > Expiry Year</span>
											<input type="text" class="form-control" placeholder="YY"/>
										</div>
										<div class="col-md-3 col-sm-3 col-xs-3">
											<span class="help-block text-muted small-font" > CCV</span>
											<input type="text" class="form-control" placeholder="CCV" />
										</div>
										<div class="col-md-3 col-sm-3 col-xs-3">
											<img src="https://bootstraptema.ru/snippets/form/2016/form-card/card.png" class="img-rounded" />
										</div>
									</div>
									<div class="user row">
										<div class="col-md-12 pad-adjust">
											<input type="text" class="form-control" placeholder="Ваши имя и фамилия" />
										</div>
									</div>
									<div class="user row">
										<div class="col-md-12 pad-adjust">
											<div class="checkbox">
												<label>
													Сумма оплаты (руб.)
													<input type="text" class="form-control"> 
												</label>
											</div>
										</div>
									</div>
									<div class="user row">
										<div class="col-md-6 col-sm-6 col-xs-6 pad-adjust">
											<button type="button" class="btn btn-danger" @click="hideModalBalance">ОТМЕНА</button>
										</div>
										<div class="col-md-6 col-sm-6 col-xs-6 pad-adjust">
											<button type="submit" class="btn btn-warning btn-block" @click="hideModalBalance">ОПЛАТИТЬ</button>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div> 
				</div>
			</div>
		</b-modal>
	</div>
</template>
<script>
import axios from "axios"
export default {
	data () {
		return {
			USER: [],
		}
	},
	methods: {
		showModalBalance() {
			this.$refs['modal-balance'].show();
		},
		hideModalBalance() {
			this.$refs['modal-balance'].hide();
		},
		getUser() {
			const path = 'https://127.0.0.1:5000/user'
			axios.get(path)
				.then((res) => {
					this.USER = res.data.data_user;
					console.log(this.USER);
				})
		}

	},
	created() {
		this.getUser();
	}
};
</script>

<style scoped>
.info {
	margin: 50px 0 0 0;
}
.user {
	margin: 0 0 0 0;
}
.avatar {
	height: 200px;
}
.credit-card-div span {
 padding-top:10px;
 }
.credit-card-div img {
 padding-top:30px;
}
.credit-card-div .small-font {
 font-size:9px;
}
.credit-card-div .pad-adjust {
 padding-top:10px;
}
</style>