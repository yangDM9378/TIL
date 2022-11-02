<template>
  <div id="app">
    <h1>APP</h1>
    <input type="text" v-model = 'appData' >
    <h3>parentData: {{ parentData }}</h3>
    <h3>childData: {{}}</h3>
    <AppParent 
    :app-data="appData"
     @app-parent-input="getParentData"
     />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  components: {
    AppParent
  },
  data: function() {
    return {
      appData: null,
      parentData: null,
    }
  },
  methods: {
    getParentData: function(appParent) {
      this.parentData = appParent
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
