<template>
  <div class="video__container">
    <div class="video_cover_layer">
      <div v-if="!playing" class="play_button" @click="playPauseVideo">
        <img v-if="!ended" class="play_triangle" src="../../../assets/images/play_triangle.png">
        <img v-else class="play_again_icon" src="https://htmlacademy.ru/assets/icons/reload-6x-white.png">
      </div>
      <video @click="playPauseVideo" :class="{ video: true, video_stopped_opacity_80: !playing }" :src="video_file"
        ref="video" @ended="videoEnded" playsinline>
        <source :src="eduVideo.video_file" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </div>
    <div v-if="!playing" class="edu_video_info_container">
      <TextContainer class="title_text" v-bind:text=eduVideo.name />
      <TextContainer class="source_info_text" v-bind:text=eduVideo.source_info />
    </div>
    <div class="switch_container">
      <label class="switch">
        <input type="checkbox" @click="toggleLanguage">
        <div class="slider round">
          <div v-if="!languageToggle" class="slider_text_cs">CS</div>
          <div v-else class="slider_text_en">EN</div>
        </div>
      </label>
    </div>
    <div>
      <div v-if="!languageToggle" class="subtitles_text">
        <TextContainer v-bind:text=subtitlesCS />
      </div>
      <div v-else class="subtitles_text">
        <TextContainer v-bind:text=subtitlesEN />
      </div>
    </div>
  </div>
</template>

<script>
import TextContainer from "./TextContainer.vue";

export default {
  components: { TextContainer },
  name: "Video",
  data() {
    return {
      eduVideo: null,
      subtitlesInfo: [],
      subtitlesCS: "",
      subtitlesEN: "",
      languageToggle: true,

      subtitles: [],
      playing: false,
      ended: false,
      userID: '',
    }
  },
  created() {
    this.fetchVideoWithSubtitles()
    //this.setUserIDCookie()
  },
  mounted() {
    console.log("Hello world")
    let element = this.subtitlesInfo[0]
    this.$refs.video.addEventListener('timeupdate', () => {
      element = this.subtitlesInfo.find(i => i.time == Math.round(this.$refs.video.currentTime * 4) / 4 && !i.triggered)
      if (element) {
        this.subtitlesCS = element.cs
        this.subtitlesEN = element.en
        element.triggered = true
      }
    })
  },
  methods: {
    fetchVideoWithSubtitles() {
      this.$axios.get("http://localhost:8000/api/edu-video/?cookie-value=" + this.getCookie("id")).then((response) => {
        console.log(response.data)
        this.eduVideo = response.data[0]
        console.log(this.eduVideo)
        this.fetchSubtitles()
      }, (error) => {
        console.log(error);
      })
    },
    fetchSubtitles() {
      this.$axios.get("http://localhost:8000/api/subtitles-info/?edu-video-id=" + this.eduVideo.id).then((response) => {
        this.subtitles = response.data
        this.subtitlesCS = this.subtitles[0].translation
        this.subtitlesEN = this.subtitles[0].original
        this.setSubtitlesEndTimes()
        console.log("tohle jsou:", this.subtitlesInfo)
      }, (error) => {
        console.log(error);
      })
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
      console.log(this.subtitlesInfo)
      this.subtitlesInfo.forEach(element => { element.triggered = false })
      console.log(this.subtitlesInfo)
      // setTimeout(this.playPauseVideo, 1000)
    },
    setSubtitlesEndTimes() {
      console.log(this.subtitles)
      this.subtitles.forEach(element => this.subtitlesInfo.push({
        time: element.start_time, triggered: false, cs: element.translation, en: element.original
      }))
    },

    toggleLanguage() {
      console.log(this.languageToggle)
      this.languageToggle = !this.languageToggle
      this.$emit('setCheckboxVal', this.languageToggle)
    },
    setUserIDCookie() {
      this.userID = new Date().getTime()
      document.cookie = "id=" + this.userID + "; expires=Thu, 18 Dec 2022 12:00:00 UTC";
    },
    getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    }
  },
}
</script>