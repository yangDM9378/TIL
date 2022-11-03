<template>
  <div id="app">
    <h1>진화 단계 가이드</h1>
    <button @click='HomeMovie' class='app-btn'>Home</button>
    <button @click='NocolorMovie' class='app-btn'>Start</button>
    <router-view/>
  </div>
</template>

<script>

export default {
    methods: {
      HomeMovie: function () {
        this.$router.push("/").catch(() => {})
      },
      NocolorMovie: function () {
        this.$router.push("/happeed").catch(() => {})
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
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.app-btn {
  margin:5px;
  border-width: 1px;
  border-color: #F1A324;
  background-color: transparent;
}
.app-btn:hover {
  background: #F7E43A
}
</style>
