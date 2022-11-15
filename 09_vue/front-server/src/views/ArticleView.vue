<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
    <button v-if='isLogin' @click="Logout">Logout</button>
    <hr>
    <ArticleList/>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'
export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인 필요')
        this.$router.push({ name: 'LogInView' })
      }
    },
    Logout() {
      console.log('로그아웃')
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style>

</style>
