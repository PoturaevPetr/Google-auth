<template>
	<div>
		<b-alert variant="success" show>{{ message }}</b-alert>
	</div>
</template>

<script>
export default {
  props: ['message'],
};
</script>

<style scoped>
b-alert {
	color: red;
}
.alert {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	border-radius: 10px;
}
</style>