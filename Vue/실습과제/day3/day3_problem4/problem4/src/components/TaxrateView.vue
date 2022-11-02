<template>
  <div>
    <h2>산출세액: {{ calTex }} 만원</h2>
    <h2>세액감면:(-) {{ texMoney }} 만원</h2>

    <FinaltaxView :cal-tex="calTex" :tex-money="texMoney"/>

  </div>
</template>

<script>
import FinaltaxView from '@/components/FinaltaxView'

export default {
  name: 'TexrateView',
  props:{
    texSt: Number,
    texMoney: Number,
  },
  components:{
    FinaltaxView
  },
  computed: {
    calTex: function() {
      if (this.texSt <= 1200) {
        return Math.round(this.texSt * 0.06)
      } else if (1200 < this.texSt <= 4600){
        return Math.round(this.texSt * 0.15-108)
      } else if (4600 < this.texSt <= 8800) {
        return Math.round(this.texSt *0.24-522)
      } else if (8800 < this.texSt <= 15000) {
        return Math.round(this.texSt *0.35-1490)
      } else if (15000 < this.texSt <= 30000) {
        return Math.round(this.texSt *0.38-1940)
      } else if (30000 < this.texSt <= 50000) {
        return Math.round(this.texSt *0.40-2540)
      } else if (50000 < this.texSt <= 10000) {
        return Math.round(this.texSt *0.42-3540)
      }else {
        return Math.round(this.texSt *0.45-6540)
      }
    }
  }
  
}
</script>

<style>

</style>