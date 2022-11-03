<template>
  <div class = "container">
    <div>
      <h1 class="text-primary">SSAFY TUBE</h1>
    </div>

    <section v-if="isSelectedVideo" class="mt-4">
      <div class="ratio ratio-16x9">
        <iframe :src="videoSrc"></iframe>
      </div>
      <div class="video-title shadow-lg p-3 mb-5 bg-body rounded" >
        <h4>{{ selectedVideo.snippet.title }}</h4>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'

const API_URL = "https://www.googleapis.com/youtube/v3/search"
const API_KEY = ""

export default {
  name: 'SaffyTube',
  created() {
    axios.get(API_URL, {
      params: {
        key: API_KEY,
        type: 'video',
        part: 'snippet',
        q: 'SSAFY'
      }
    }).then((response) => {
      this.videos = response.data.items
      this.selectedVideo = this.videos[0]
    }).catch((error) => {
      console.error(error)
    })
  },
  data: function() {
    return {
      videos:[],
      selectedVideo: {}
    }
  },
  computed: {
    videoSrc() {
      const url = 'http://www.youtube.com/embed/'
      return url + this.selectedVideo.id.videoId
    },
    isSelectedVideo() {
      return !!Object.keys(this.selectedVideo).length
    }
  }
}
</script>

<style>
  * {
    font-family: 'Noto Sans KR', sans-serif;
  }

  .video-title {
    border: 1px solid gray;
  }
</style>