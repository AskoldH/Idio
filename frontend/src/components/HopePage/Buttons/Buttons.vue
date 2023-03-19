<template>
  <div class="back_button_container">
    <BaseButton v-if="propsData.eduVideo.id" @click="sendLoadDataToParentBack('back'); backButtonDisableEnable(true);"
      v-bind:buttonInfo="buttonBackInfo" class="back_button" />
  </div>
  <div class="learned_skip_buttons_container">
    <BaseButton v-if="propsData.eduVideo.id" @click="sendLoadDataToParentLearned('learned'); backButtonDisableEnable('skipLearned');"
      v-bind:buttonInfo="buttonLearnedInfo" class="learned_button" />

    <BaseButton v-if="propsData.eduVideo.id" @click="sendLoadDataToParentSkip('skip'); backButtonDisableEnable('skipLearned');"
      v-bind:buttonInfo="buttonSkipInfo" class="skip_button" />
  </div>
</template>

<script>

import BaseButton from "@/components/HopePage/Buttons/BaseButton.vue";
import "../../../assets/style/edu-video-tile.scss";
import "../../../assets/style/buttons.scss";

export default {
  name: "Buttons",
  components: { BaseButton },
  props: {
    propsData: {
      type: Object,
      default: () => ({}),
    }
  },
  emits: ['send-message-to-parent'],
  data() {
    return {
      buttonLearnedInfo: {
        label: "Umím",
        isDisabled: false,
      },

      buttonSkipInfo: {
        label: "Přeskočit",
        isDisabled: false,
      },

      buttonBackInfo: {
        label: "Zpět",
        isDisabled: false,
      },
    }
  },
  created() {
    this.backButtonDisableEnable()
    if (this.propsData.lastEduVideo) {
      this.backButtonDisableEnable()
    }
    else {
      const unwatch = this.$watch('propsData.eduVideo.id', () => {
        this.backButtonDisableEnable()
        unwatch()
      })
    }
  },
  methods: {
    backButtonDisableEnable(clicked) {
      console.log('edudfsdf', this.propsData)
      console.log(this.propsData.eduVideo.id, "vs", this.propsData.lastEduVideo)
      if (clicked === 'skipLearned'){
        this.buttonBackInfo.isDisabled = false 
        return
      }
      if (this.propsData.lastEduVideo === null || clicked || this.propsData.eduVideo.id === this.propsData.lastEduVideo ) { 
        this.buttonBackInfo.isDisabled = true 
        console.log("1")
      }
      else { 
        this.buttonBackInfo.isDisabled = false 
        console.log("3")
      }
    },
    /*postSkipped() {
      this.$axios.post("http://localhost:8000/api/edu-video-skip", { "edu_video_id": this.propsData.eduVideo.id, "cookie_value": this.propsData.cookieValue }).then((response) => console.log(response))
        .catch(error => console.log(error))
    },
    postLearned() {
      this.$axios.post("http://localhost:8000/api/edu-video-learn", { "edu_video_id": this.propsData.eduVideo.id, "cookie_value": this.propsData.cookieValue }).then((response) => console.log(response))
        .catch(error => console.log(error))
    },*/
    patchLastEduVideo() {
      this.$axios.patch("http://localhost:8000/api/idio-user", { "edu_video_id": this.propsData.eduVideo.id, "cookie_value": this.propsData.cookieValue }).then((response) => console.log(response))
        .catch(error => console.log(error))
    },
    sendLoadDataToParentBack(buttonType) {
      console.log("posláno snad")
      this.propsData.buttonType = buttonType
      if (this.buttonBackInfo.isDisabled) { return }
      this.$emit('send-message-to-parent', this.propsData)
    },
    sendLoadDataToParentLearned(buttonType) {
      console.log("posláno snad: ", this.propsData)
      this.propsData.buttonType = buttonType
      this.$emit('send-message-to-parent', this.propsData)
      if (this.propsData.checkTest == '3'){
        this.propsData.performTest = 1
        this.propsData.buttonType = false
        this.$emit('send-message-to-parent', this.propsData)
      }
      if (this.buttonLearnedInfo.isDisabled) { return }
      
    },
    sendLoadDataToParentSkip(buttonType) {
      console.log("posláno snad")
      this.propsData.buttonType = buttonType
      if (this.buttonSkipInfo.isDisabled) { return }
      this.$emit('send-message-to-parent', this.propsData)
    },
  }
}
</script>