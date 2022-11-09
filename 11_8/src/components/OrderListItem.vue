<template>
  <li>
    <img :src="order.pickMenu[0].image" width="100px">
    <p>{{ order.pickMenu[0].title }}</p>
    <p>사이즈:{{ order.pickSize[0].name }}</p>
    <p v-for='(option,index) in order.pickoption'
    :key='index'>{{ option.type }} {{ option.count }}</p>

  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    // totalPrice: function () {
    // },
  },
}
</script>

<style>
</style>