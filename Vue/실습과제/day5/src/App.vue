<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <MenuList/>
    <SizeList/>
    <OptionList/>
    <OrderList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OptionList from '@/components/OptionList'
import OrderList from '@/components/OrderList'
export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OptionList,
    OrderList
  },
}

</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>
