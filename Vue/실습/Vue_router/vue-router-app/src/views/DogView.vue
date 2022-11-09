<template>
  <div>
    <p v-if="!imgSrc">{{ message }}</p>
    <img :src="imgSrc">
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: '로딩한다.',
    }
  },
  methods: {
    getDogImage() {
    const breed = this.$route.params.breed
    const dogImgeUrl =`https://dog.ceo/api/breed/${breed}/images/random`
      axios({
        method: 'get',
        url: dogImgeUrl
      })
      .then((response) => {
        const imgSrc = response.data.message
        this.imgSrc = imgSrc
      })
      .catch((error) => {
        // this.message = `${this.$route.params.breed}은 없는 품종 입니다.`
        this.$router.push('/404')
        console.log(error)
      })
    }
  },
  created() {
    this.getDogImage()
  }

}
</script>

<style>

</style>