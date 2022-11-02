<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model = 'appParent' @keyup.enter="AppParentInput">
    <h3>appData: {{ appData }}</h3>
    <h3>childData: {{ ChildData }}</h3>

    <AppChild 
    :app-data='appData' 
    :app-parent='appParent'
    />

  </div>
</template>

<script>
  import AppChild from "@/components/AppChild"
export default {
  name: 'AppParent',
  components: {
    AppChild
  },
  props: {
    appData: String,
  },
  data: function() {
    return {
      appParent:null,
      ChildData:null
    }
  },
  methods: {
    AppParentInput: function() {
      this.$emit('app-parent-input', this.appParent)
    },

  }
}
</script>

<style>

</style>