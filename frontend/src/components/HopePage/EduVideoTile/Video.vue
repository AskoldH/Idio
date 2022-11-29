<template>
  <div class="video__container">
    <div class="video_cover_layer">
      <div v-if="!playing" class="play_button" @click="playPauseVideo">
        <img v-if="!ended" class="play_triangle" src="../../../assets/images/play_triangle.png">
        <img v-else class="play_again_icon" src="https://htmlacademy.ru/assets/icons/reload-6x-white.png">
      </div>
      <video @click="playPauseVideo" :class="{ video: true, video_stopped: !playing}" :src="video_file" ref="video"
             @ended="videoEnded" playsinline>
        <source :src="eduVideo.video_file" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
    <!--      <div class="titles_container">-->
    <!--        <div class="video_name">-->
    <!--          {{ eduVideo.name }}-->
    <!--        </div>-->
    <!--        <div class="video_source_info">-->
    <!--          Zdroj: {{ eduVideo.source_info }}-->
    <!--        </div>-->
    <!--      </div>-->
  </div>
</template>

<script>
export default {
  name: "Video",
  data() {
    return {
      subtitlesInfo: null,
      eduVideo: null,
      playing: false,
      ended: false,
    }
  },
  created() {
    this.$axios.get("http://localhost:8000/api/edu-videos").then((response) => {
      this.eduVideo = response.data[0]
      console.log(this.eduVideo)
    }, (error) => {
      console.log(error);
    })
  },
  methods: {
    fetchVideo() {
      this.$axios.get("http://localhost:8000/api/edu-videos").then((response) => {
        this.eduVideo = response.data[0]
      }, (error) => {
        console.log(error);
      })
      this.video_file = this.eduVideo.video_file
      console.log(this.eduVideo.video_file)
      console.log(this.eduVideo)
      console.log(this.video_file)
    },
    sendRequest2() {
      this.$axios.get("http://localhost:8000/api/subtitles-info/?eduvideo-id=" + this.eduVideo.id).then((response) => {
        this.subtitlesInfo = response.data
      }, (error) => {
        console.log(error);
      })
      console.log(this.subtitlesInfo)
    },
    playPauseVideo() {
      if (this.playing) {
        this.$refs.video.pause();
        this.playing = false;
        return
      }
      this.$refs.video.play();
      this.playing = true;
      this.ended = false;
    },
    videoEnded() {
      this.ended = true
      this.playing = false
      // setTimeout(this.playPauseVideo, 1000)
    },
  }
}
</script>