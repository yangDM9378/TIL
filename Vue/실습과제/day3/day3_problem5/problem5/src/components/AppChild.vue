<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" v-model = 'appChild' @input="AppChildInput">
      <h3>appData: {{ appData }}</h3>
      <h3>parentData: {{ appParent }}</h3>
      <h3>childData: {{ appChild }}</h3>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appData: String,
    appParent: String,
  },
  data: function() {
    return {
      appChild: null,
      }
  },
  methods: {
    AppChildInput: function (){
      this.$emit('app-child-input', this.appChild)
    }
  }
}
</script>

<style>

</style>