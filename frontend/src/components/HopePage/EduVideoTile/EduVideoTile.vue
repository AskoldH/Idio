<template>
  <div v-if="eduVideo.id">
    <div class="video__container">
      <div class="video_cover_layer">
        <!-- <div v-if="!playing" class="image_play_button" @click="playPauseVideo">
            <img class="play_image_from_logo" src="../../../assets/images/idio_page_logo.png">
          </div> -->
        <div v-if="!playing" class="play_button" @click="playPauseVideo">
          <img v-if="!ended" class="play_triangle" src="../../../assets/images/play_triangle.png">
          <img v-else class="play_again_icon" src="https://htmlacademy.ru/assets/icons/reload-6x-white.png">
        </div>
        <video @click="playPauseVideo" :class="{ video: true, video_stopped_opacity_80: !playing }"
          :src="eduVideo.video_file" type="video/mp4" ref="video" @ended="videoEnded" playsinline>
          Your browser does not support the video tag.
        </video>
      </div>
      <div v-if="!playing && eduVideo.name" class="edu_video_info_container">
        <TextContainer class="title_text" v-bind:text=eduVideo.name />
        <TextContainer class="source_info_text" v-bind:text="eduVideo.source_name + divider + eduVideo.source_season_episode" />
      </div>
      <div v-if="subtitles.cs && subtitles.en">
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
            <TextContainer v-bind:text=subtitles.cs />
          </div>
          <div v-else class="subtitles_text">
            <TextContainer v-bind:text=subtitles.en />
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-if="!eduVideo.id && hasLoaded">
    <TextContainer class="error_messsage_text" v-bind:text=errorMessage />
  </div>
</template>

<script>
import TextContainer from "./TextContainer.vue";

export default {
  components: { TextContainer },
  name: "EduVideoTile",
  props: {
    propsData: {
      type: Object,
      default: () => ({}),
    }
  },
  data() {
    return {
      errorMessage: "Všechna video zobrazena.",
      hasLoaded: false,

      eduVideo: {
        video_file: '',
        name: '',
        source_info: '',
      },

      subtitlesInfo: [{
        time: '',
        triggered: false,
        cs: '',
        en: ''
      }],
      subtitles: {
        cs: '',
        en: '',
      },

      languageToggle: true,
      playing: false,
      ended: false,
      divider: " | ",
    }
  },

  created() {
    setTimeout(() => {
      this.toggleHasLoaded();
    }, "500")

    if (this.propsData.eduVideo.id) {
      this.eduVideo = this.propsData.eduVideo
      this.fetchSubtitles()
    }
    else {
      const unwatch = this.$watch('propsData.eduVideo.video_file', () => {
        this.eduVideo = this.propsData.eduVideo
        this.fetchSubtitles()
        unwatch()
      })
    }
  },

  methods: {
    fetchSubtitles() {
      this.$axios.get("http://localhost:8000/api/subtitles-info?edu-video-id=" + this.eduVideo.id).then((response) => {
        this.setSubtitlesTimes(response.data)
        this.setVideoListener()
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

      // sets triggered = false for subtitles elements in subtitlesInfo list 
      this.subtitlesInfo.forEach(element => { element.triggered = false })
    },

    setSubtitlesTimes(responseData) {
      // sets fisrt values to subtitles if get subtitles
      if (this.subtitles.cs) {
      this.subtitles.cs = responseData[0].translation
      }
      if (this.subtitles.en) {
      this.subtitles.en = responseData[0].original
      }

      // prepares list subtitlesInfo with times
      this.subtitlesInfo = []
      responseData.forEach(element =>
        this.subtitlesInfo.push(
          {
            time: element.start_time,
            triggered: false,
            cs: element.translation,
            en: element.original
          }
        ))
    },

    setVideoListener() {
      let element = this.subtitlesInfo[0]
      this.$refs.video.addEventListener('timeupdate', () => {
        element = this.subtitlesInfo.find(i => i.time == Math.round(this.$refs.video.currentTime * 4) / 4 && !i.triggered)
        if (element) {
          this.subtitles.cs = element.cs
          this.subtitles.en = element.en
          element.triggered = true
        }
      })
    },

    toggleLanguage() {
      // true = en, false = cs
      this.languageToggle = !this.languageToggle

      // changes value in checkbox
      this.$emit('setCheckboxVal', this.languageToggle)
    },

    toggleHasLoaded() {
      this.hasLoaded = !this.hasLoaded
    }
  },
}
</script>