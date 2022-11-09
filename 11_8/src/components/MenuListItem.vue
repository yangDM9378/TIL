<template>
  <div>
    <button
      @click='updateMenu'
      :class="{'select_menu': !menu.selected}"
    >
      <img :src="menu.image" width="100px">
      {{ menu.title }}
      {{ menu.price }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    updateMenu: function() {
      this.$store.dispatch('updateMenu', this.menu)
    }
  }
}
</script>

<style>
  .select_menu {
   background-color: red; 
  }
</style>