<template>
  <div>
    <hr>
    <h2>결정세액: {{ calTex-texMoney }} 만원</h2>
  </div>
</template>

<script>
export default {
  name: 'FinaltaxView',
  props: {
    calTex: Number,
    texMoney: Number,
  }
}
</script>

<style>

</style>