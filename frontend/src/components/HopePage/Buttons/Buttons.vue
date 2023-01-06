<template>
  <BaseButton v-if="propsData.eduVideo.id" @click="sendLoadDataToParent('back'); backButtonDisableEnable(true);"
    v-bind:buttonInfo="buttonBackInfo" class="back_button" />
  <BaseButton v-if="propsData.eduVideo.id" @click="sendLoadDataToParent('learned'); patchLastEduVideo();"
    v-bind:buttonInfo="buttonSkipInfo" class="learned_button" />
  <BaseButton v-if="propsData.eduVideo.id" @click="sendLoadDataToParent('skip'); patchLastEduVideo();"
    v-bind:buttonInfo="buttonLearnedInfo" class="skip_button" />
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
      backButtonDisabled: false,

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
      console.log('edudfsdf', this.propsData.lastEduVideo)
      console.log(this.propsData.eduVideo.id, "vs", this.propsData.lastEduVideo)
      if (this.propsData.lastEduVideo == null || clicked ) { 
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
    sendLoadDataToParent(buttonType) {
      this.propsData.buttonType = buttonType
      if (this.buttonBackInfo.isDisabled) { return }
      this.$emit('send-message-to-parent', this.propsData)
    },
  }
}
</script>