<template>
  <div>
    <div>
      {{ option.type }}
      <button @click='decrease'>-</button>
      {{ option.count }}
      <button @click='increase'>+</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.dispatch('increase', this.option)
    },
    decrease(){
      this.$store.dispatch('decrease', this.option)
    }

  },
}
</script>

<style>
</style>