<template>
  <div class="about">
    <img alt="Vue logo" src="../assets/logo.png">
    <hello-world/>
    <h1>첫번째 페이지 입니다</h1>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld'

export default {
  name: 'FirstView',
  components: {
    HelloWorld
  }
}
</script>
