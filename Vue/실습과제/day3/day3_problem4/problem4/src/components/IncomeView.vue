<template>
  <div>
    <h1>나는 income</h1>
    <input type="number" v-model.number= 'money'>
    <br>
    <input type="number" v-model.number= 'texMoney'>
    <hr>
    <h2>종합소득금액: {{ money }} 만원</h2>
    <h2>종합소득공제: (-) {{ totalTex }} 만원</h2>
    <h2>과세표준: {{ texSt }} </h2>
    <hr>
    <TaxrateView :tex-money = "texMoney" :tex-st = "texSt"/>
  
  </div>
</template>

<script>
import TaxrateView from '@/components/TaxrateView'

export default {
  name: 'IncomeView',
  data: function() {
    return {
      money: null,
      totalTex: 150,
      texMoney: null,
    }
  },
  computed: {
    texSt: function() {
      if (this.money - 150 < 0) {
        return 0
      } else {
        return this.money - 150
      }
    }
  },
  components: {
    TaxrateView
  }
}
</script>

<style>

</style>