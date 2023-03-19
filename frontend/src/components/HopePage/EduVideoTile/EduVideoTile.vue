<template>
  <div v-if="eduVideo.id" class="edu_tile_container">
    <div :class="{video__container:!this.propsData.performTest, video__container_test:this.propsData.performTest}">
      <div class="video_cover_layer">
        <!-- <div v-if="!playing" class="image_play_button" @click="playPauseVideo">
            <img class="play_image_from_logo" src="../../../assets/images/idio_page_logo.png">
          </div> -->
        <div v-if="!playing" class="play_button" @click="playPauseVideo">
          <img v-if="!ended" class="play_triangle" src="../../../assets/images/play_triangle.png">
          <img v-else class="play_again_icon" src="https://htmlacademy.ru/assets/icons/reload-6x-white.png">
        </div>
        <video @click="playPauseVideo()" :class="{ video: true, video_stopped_opacity_80: !playing }"
          :src="eduVideo.video_file" type="video/mp4" ref="video" @ended="videoEnded" playsinline>
          Your browser does not support the video tag.
        </video>
      </div>
      <div v-if="!checkPerformTest() && (!playing || screenWidth())" class="test_bubbles_container">
        <TextContainer class="test_title" v-bind:text="test_title" />
        <TextContainer v-for="component in shuffleComponents" @click="revealAnswer(component.key);" :key="component.key" :class="component.class" v-bind:text="component.text" />
      </div>
      <div v-if="(!playing || screenWidth()) && eduVideo.name" class="edu_video_info_container">
        <div class="title_source_container" >
          <div class="divider"></div>
          <TextContainer class="title_text" v-bind:text=eduVideo.name />
          <TextContainer class="source_info_text"
            v-bind:text="eduVideo.source_name_cs + divider + eduVideo.source_season_episode" />
        </div>
    </div>
      <div>
        <div class="switch_container" v-if="subtitles.cs && subtitles.en">
          <label class="switch">
            <input type="checkbox" @click="toggleLanguage">
            <div class="slider round">
              <div v-if="!languageToggle" class="slider_text_cs">CS</div>
              <div v-else class="slider_text_en">EN</div>
            </div>
          </label>
        </div>
        <div>
          <div class="divider_subtitles"></div>
            <div v-if="subtitles.cs && subtitles.en">
              <div v-if="!languageToggle" class="subtitles_text" @click="toggleLanguage">
                <TextContainer v-bind:text=subtitles.cs />
              </div>
              <div v-else class="subtitles_text" @click="toggleLanguage">
                <TextContainer v-bind:text=subtitles.en />
              </div>
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
  emits: ['get-another-test-video'],
  data() {
    return {
      shuffledComponents: [],
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

      test_clicked: [false, false, false],
      class_changed: [false, false, false],

      test_answers_shuffled: false,
      languageToggle: true,
      playing: false,
      ended: false,
      divider: " | ",
      test_title: "Co vyplývá z úryvku?",
      
    }
  },

  computed:{
    shuffleComponents() {
      const components =  [
        {
          key: 'correct',
          class: {'test_text_correct': !this.test_clicked[0], 'test_text_correct_clicked': this.test_clicked[0]},
          text: "• " + this.eduVideo.main_thought 
        },
        {
          key: 'false_1',
          class: {'test_text_false': !this.test_clicked[1], 'test_text_false_clicked': this.test_clicked[1]},
          text: "• " + this.eduVideo.main_thought_false_1 
        },
        {
          key: 'false_2',
          class: {'test_text_false': !this.test_clicked[2], 'test_text_false_clicked': this.test_clicked[2]},
          text: "• " + this.eduVideo.main_thought_false_2
        } ]

      for (let i = components.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [components[i], components[j]] = [components[j], components[i]];
      }

      if (this.test_answers_shuffled){
        console.log("už to bylo shufflednuto", this.shuffledComponents)
        if (this.test_clicked[0] && this.class_changed[0]){
          if (this.shuffledComponents[0].key === 'correct'){
            this.shuffledComponents[0].class = {'test_text_correct': !this.test_clicked[0], 'test_text_correct_clicked': this.test_clicked[0]}
          }
          else if (this.shuffledComponents[1].key === 'correct'){
            this.shuffledComponents[1].class = {'test_text_correct': !this.test_clicked[0], 'test_text_correct_clicked': this.test_clicked[0]}
          }
          else if (this.shuffledComponents[2].key === 'correct'){
            this.shuffledComponents[2].class = {'test_text_correct': !this.test_clicked[0], 'test_text_correct_clicked': this.test_clicked[0]}
          }
          this.class_changed[0] = false
        }
        else if (this.test_clicked[1] && this.class_changed[1]){
          if (this.shuffledComponents[0].key === 'false_1'){
            this.shuffledComponents[0].class = {'test_text_false': !this.test_clicked[1], 'test_text_false_clicked': this.test_clicked[1]}
          }
          else if (this.shuffledComponents[1].key === 'false_1'){
            this.shuffledComponents[1].class = {'test_text_false': !this.test_clicked[1], 'test_text_false_clicked': this.test_clicked[1]}
          }
          else if (this.shuffledComponents[2].key === 'false_1'){
            this.shuffledComponents[2].class = {'test_text_false': !this.test_clicked[1], 'test_text_false_clicked': this.test_clicked[1]}
          }
          this.class_changed[1] = false
        }
        else if (this.test_clicked[2] && this.class_changed[2]){
          if (this.shuffledComponents[0].key === 'false_2'){
            this.shuffledComponents[0].class = {'test_text_false': !this.test_clicked[2], 'test_text_false_clicked': this.test_clicked[2]}
          }
          else if (this.shuffledComponents[1].key === 'false_2'){
            this.shuffledComponents[1].class = {'test_text_false': !this.test_clicked[2], 'test_text_false_clicked': this.test_clicked[2]}
          }
          else if (this.shuffledComponents[2].key === 'false_2'){
            this.shuffledComponents[2].class = {'test_text_false': !this.test_clicked[2], 'test_text_false_clicked': this.test_clicked[2]}
          }
          this.class_changed[2] = false
        }
        return this.shuffledComponents
      }

      this.test_answers_shuffled = true
      console.log("komponenty: ", components)
      this.shuffledComponents = components
      return components
    },
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
    screenWidth() {
      if (window.innerWidth < 768) { return true}
      else { return false }  
    },

    sendLoadDataToParentCorrect() {
      this.propsData.performTest = this.propsData.performTest + 1
      console.log("posláno snad: ", this.propsData)
      this.$emit('get-another-test-video', this.propsData)
    },
    resetTestInfo(){
      console.log(this.propsData.cookieValue)
      this.$axios.patch("http://localhost:8000/api/idio-user?cookie-value=" + this.propsData.cookieValue
      ).then((response) => {
        console.log(response.status)
      }, (error) => {
        console.log(error);
      })
    },
    revealAnswer(answerBubble){
      console.log("sranda", answerBubble)
      if (answerBubble === 'correct' && !this.test_clicked[0]){
        this.test_clicked[0] = true
        this.class_changed[0] = true

        if (this.propsData.performTest == 3){ this.resetTestInfo(); }
        console.log(this.test_clicked[0])
        setTimeout(() => {
          this.sendLoadDataToParentCorrect();
          }, 1000); // delay of 1 second
      }
      else if (answerBubble === 'false_1' && !this.test_clicked[1]){
        this.test_clicked[1] = true
        this.class_changed[1] = true
      }
      else if (answerBubble === 'false_2' && !this.test_clicked[2]){
        this.test_clicked[2] = true
        this.class_changed[2] = true
      }
    },
    checkPerformTest(){
      console.log("perform test je: ", this.propsData.performTest)
      //debugger;
      if (this.propsData.performTest == 0){ return true }
      else if (this.propsData.performTest > 0) { return false }
    },
    fetchSubtitles() {
      this.$axios.get("http://localhost:8000/api/subtitles-info?edu-video-id=" 
      + this.eduVideo.id).then((response) => {
        this.setSubtitlesTimes(response.data)
        console.log(response.data)
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
    },
  },
}
</script>