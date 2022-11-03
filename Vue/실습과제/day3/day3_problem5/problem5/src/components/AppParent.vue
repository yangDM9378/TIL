<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model='appParent' @input="AppParentInput">
    <h3>appData: {{ appData }}</h3>
    <h3>childData: {{ ChildData }}</h3>

    <AppChild 
    :app-data='appData' 
    :app-parent='appParent'
    @app-child-input='appChild'
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
    appChild: function(appChild) {
      this.ChildData=appChild
      this.$emit("app-child-input", this.ChildData)
    },
  }
}
</script>

<style>

</style>