<template>
  <li @click="selectedVideo" class='list-group-item my-3'>
      <img :src="video.snippet.thumbnails.high.url" :alt="video.snippet.title">
      <hr>
      <h3>{{video.snippet.title}}</h3>
      <p class="text-left m-3">{{video.snippet.description}}</p>
  </li>
</template>

<script>
export default {
    name: "VideoListItem",
    props: {
        video: {
            type: Object,
            required: true
        }
    },
    methods: {
        selectedVideo() {
            // video-select-event $emit
            // 자식컴포넌트에서는 이벤트 발생(값 전달)
            this.$emit('video-select-event', this.video)
        }
    }
}
</script>

<style scoped>
/* scoped: 해당 컴포넌트에서만 사용되는 style */
div {
    margin: 50px
}
img {
    width: 50%;
    height: 50%;
}
li {
    cursor: pointer
}
li:hover {
    background-color:rgb(255, 249, 241);
}
</style>