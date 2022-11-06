<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div>
      <h2>예약 페이지</h2>
      <h3>선생님 선택</h3>
      <div>
        <button @click="Eric_click" :class="{ 'time_btn_color' : Eric }">Eric</button>
        <button @click="Tony_click" :class="{ 'time_btn_color' : Tony }">Tony</button> 
      </div>
      <h3>시간 선택</h3>
      <a v-for="(time, index) in times" :key="index">
        <button 
        class = "btn"
        @click="attupdate(index)"
        :class="{ 'time_btn_color' : isChecked[index] }"
          >
          {{ time }}
        </button>
      </a>
      <hr>
      <h3>선택 시간 : 
      <a v-for="(a, index) in li" :key="`a-${index}`">{{ a }} </a></h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  data: function() {
    return  {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      isChecked: [
        false,false,false,false,false,false,false,false,false,false,
        false,false,false,false,false,false,false,false,false,false,
        false,false,false,false,false,false,false,false,false,false,
      ],
      times_Tony: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      isChecked_Tony: [
        false,false,false,false,false,false,false,false,false,false,
        false,false,false,false,false,false,false,false,false,false,
        false,false,false,false,false,false,false,false,false,false,
      ],
      cnt: 0,
      cnt_Tony: 0,
      li: [],
      li_Tony: [],
      li_idx: null,
      li_idx_Tony: null,
      Eric: false,
      Tony: false,
    }
  },
  methods: {
    attupdate: function(index) {
      if (this.cnt < 5) {
        if (this.li.includes(this.times[index])) {
          this.li_idx = this.li.indexOf(this.times[index])
          this.li.splice(this.li_idx,1)
        } else {
          this.li.push(this.times[index])
        }
        this.$set(this.isChecked, index, !this.isChecked[index])
        if (this.isChecked[index] == true) {
          this.cnt++
        }
        else {
          this.cnt--
        }
      } else {
        if (this.isChecked[index] == true) {
          this.li_idx = this.li.indexOf(this.times[index])
          this.li.splice(this.li_idx,1)
          this.cnt--
          this.$set(this.isChecked, index, !this.isChecked[index])
        } else{
          alert('5타임까지만 신청할 수 있습니다.')
        }
      }
      this.li.sort()
    },
    Eric_click: function() {
      this.Eric = !this.Eric
      if (this.Tony === true) {
        this.Tony = !this.Tony
      }
    },
    Tony_click: function() {
      this.Tony = !this.Tony
      if (this.Eric === true) {
        this.Eric = !this.Eric
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #424242;
  margin-top: 60px;
}


.btn {
  background-color:transparent;
  border: 0;
  color: rgba(75, 56, 56, 0.544);
  font-weight: bold; 
  
}

.time_btn_color {
  background-color: #1c88e656;
  color: rgba(40, 50, 96, 0.797);
  font-weight: 600; 
}


</style>
<!-- #0F4C81(클릭배경), #658dc63d(글자색?), #84898C(시간글자색), #424242 -->