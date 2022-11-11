<template>
  <div>
    <button
      @click='addorder'
      >
      장바구니 담기
    </button>
    <div>
    <OrderListItem
    v-for='(order,index) in orderList'
    :key='index'
    :order='order'
    />
      <h3>주문 내역: </h3>
      <p>총 갯수건:{{ totalOrderCount }}건 전체 가격원 {{ totalOrderPrice }} </p>
    </div>
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'
export default {
  name: 'OrderList',
  components:{
    OrderListItem
  },
  computed: {
    orderList: function () {
      return this.$store.state.orderList
    },
    totalOrderCount: function () {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice: function () {
      return this.$store.getters.totalOrderPrice
    },
  },
  methods: {
    addorder: function() {
      this.$store.dispatch('addorder')
    }
  }
}
</script>

<style>
</style>