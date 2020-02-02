<template>
  <div id="q-app">
		<q-list>
			<q-item v-for="cereal in this.cereals">
					<q-item-section>{{cereal.path}}</q-item-section>
			</q-item>
		</q-list>
  </div>
</template>

<script>
	import {ipcRenderer} from 'electron'

	export default {
	  name: 'App',
		data: function() {
			return {
				selectedPort:
			};
		},
		mounted: function() {
			ipcRenderer.send('get-cereals');
			ipcRenderer.on('got-milk', (event, arg) =>{
				this.cereals = arg;
			})
		}
	}
</script>
