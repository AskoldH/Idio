<template>
  <div class="video__container" @click="playPauseVideo(); sendRequest()">
    <div class="video_cover_layer">
      <div v-if="!playing" class="play_button"/>
      <video :class="{ video: true, video_stopped: !playing}" ref="video" @ended="playing = false" playsinline>
        <source src="http://localhost:8000/videos/himym_1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
  </div>
</template>

<script>
export default {
  name: "Video",
  data() {
    return {
      eduVideo: null,
      playing: false,
    }
  },
  methods: {
    sendRequest() {
      this.$axios.get("http://localhost:8000/api/edu-videos").then((response) => {
        this.eduVideo = response.data
      }, (error) => {
          console.log(error);
      })
      console.log(this.eduVideo)
    },
    playPauseVideo() {
      console.log("Hi")
      if (this.playing) {
        this.$refs.video.pause();
        this.playing = false;
        return
      }
      this.$refs.video.play();
      this.playing = true;
    },
  }
}
</script>