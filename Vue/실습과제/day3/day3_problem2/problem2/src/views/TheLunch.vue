<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click='menupick'>Pick Lunch</button>
    <p>{{ pick_menu }}</p>
    <h1>로또를 뽑아보자</h1>
    <button @click="golotto">Pick Lotto</button>
  </div>
</template>

<script>
import _ from "lodash"
export default {
  name: 'TheLunch',
  data: function() {
    return {
      menu: ['국밥','한방족발','평동애호박찌개'],
      pick_menu: null
    }  
  },
  methods: {
    menupick: function () {
      this.pick_menu = _.sample(this.menu)
    },
    golotto: function() {
      this.$router.push("/lotto/6")
    }
  }
}
</script>
