<template>
  <div>
    <button
    @click='updateSize'
    :class="{'select_size': !size.selected }"
    >
      {{ size.name }}
      {{ size.price }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods:{
    updateSize:function(){
      this.$store.dispatch('updateSize',this.size)
    }
  }
}
</script>

<style>
.select_size {
   background-color: purple; 
  }
</style>
