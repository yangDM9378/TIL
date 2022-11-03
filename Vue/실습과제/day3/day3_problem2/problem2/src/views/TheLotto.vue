<template>
  <div>
    <h1>로또</h1>
    <button @click='getnum'>Get Lucky Numbers</button>
    <p>{{ lottopick }}</p>
  </div>
</template>

<script>
import _ from "lodash"
 
export default {
  name: 'TheLotto',
  data: function () {
    return {
      lottopick: null
    }
  },
  methods: {
    getnum: function() {
      this.lottopick=_.sampleSize(_.range(1, 45), 6);
    }
  }
}
</script>