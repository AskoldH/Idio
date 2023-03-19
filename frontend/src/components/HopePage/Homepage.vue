<template>
    <Buttons v-if="checkPerformTest()" v-bind:propsData="propsData" @send-message-to-parent="refreshVideo" />
    <EduVideoTile v-bind:propsData="propsData" @get-another-test-video="refreshVideo" v-bind:key="uniqueKey" />
</template>

<script>
import "./../../../src/assets/style/edu-video-tile.scss";
import "./../../../src/assets/style/buttons.scss";
import "./../../../src/assets/style/text-containers.scss";
import EduVideoTile from "./EduVideoTile/EduVideoTile.vue";
import Buttons from "./Buttons/Buttons.vue";

export default {
  name: "Homepage",
  components: { EduVideoTile, Buttons },
  data() {
    return {
      uniqueKey: 1,

      propsData:
      {
        cookieValue: '',
        buttonType: false,
        lastEduVideo: '',
        checkTest: '',
        performTest: 0,
        eduVideo: {
          video_file: null,
          name: null,
          source_info: null,
        },
      },
    }
  },
  created() {
    this.propsData.cookieValue = this.getCookie("id")
    this.fetchLastVideo()
    this.fetchVideo()
    console.log("check test je", this.propsData)
  },
  methods: {
    getCookie(name) {
      // gets cookie value by cookie name
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    },
    fetchVideo() {
      this.$axios.get("http://localhost:8000/api/edu-video", {
        params: {
          cookie_value: this.propsData.cookieValue,
          button_type: 'false',
          edu_video_id: 'false',
          perform_test: 0,
        }
      }).then((response) => {
        this.propsData.checkTest = response.data.check_test
        this.propsData.eduVideo = response.data
        this.propsData.eduVideo.video_file = "http://localhost:8000" + this.propsData.eduVideo.video_file
      }, (error) => {
        console.log(error);
      })
    },
    addOneToUniqueKey() {
      this.uniqueKey +=1;
    },
    refreshVideo() {
      if (this.propsData.performTest > 0){
        this.$axios.get("http://localhost:8000/api/edu-video", {
        params: {
          cookie_value: this.propsData.cookieValue,
          button_type: this.propsData.buttonType,
          edu_video_id: this.propsData.eduVideo.id,
          perform_test: this.propsData.performTest,
        }
      }).then((response) => {
        this.propsData.eduVideo = response.data
        this.propsData.checkTest = response.data.check_test
        this.propsData.eduVideo.video_file = "http://localhost:8000" + this.propsData.eduVideo.video_file
        if (this.propsData.performTest == 4){this.propsData.performTest = 0}
      }, (error) => {
        console.log(error);
      })
      setTimeout(this.addOneToUniqueKey, 200)
      }

      console.log("posláno...")
      console.log("perform test: ", this.propsData.performTest)
      this.$axios.get("http://localhost:8000/api/edu-video", {
        params: {
          cookie_value: this.propsData.cookieValue,
          button_type: this.propsData.buttonType,
          edu_video_id: this.propsData.eduVideo.id,
          perform_test: this.propsData.performTest,
        }
      }).then((response) => {
        this.propsData.eduVideo = response.data
        this.propsData.checkTest = response.data.check_test
        this.propsData.eduVideo.video_file = "http://localhost:8000" + this.propsData.eduVideo.video_file
      }, (error) => {
        console.log(error);
      })
      setTimeout(this.addOneToUniqueKey, 200)
      console.log("tohle jsem updatenul: ", this.propsData)
    },
    fetchLastVideo(){
      this.$axios.get("http://localhost:8000/api/idio-user", {
        params: {
          cookie_value: this.propsData.cookieValue,
        }
      }).then((response) => {
        this.propsData.lastEduVideo = response.data.last_edu_video
        console.log(this.propsData.lastEduVideo)
      }, (error) => {
        console.log(error);
      })
    },
    checkPerformTest(){
      console.log("perform test je: ", this.propsData.performTest)
      //debugger;
      if (this.propsData.performTest == 0){ return true }
      else if (this.propsData.performTest > 0) { return false }
    }
  }
}
</script>