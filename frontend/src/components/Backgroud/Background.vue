<template>
  <ul class="background">
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
  </ul>
</template>

<script>
export default {
  name: "background"
}
</script>

<style scoped>
@keyframes animate {
    0%{
        transform: translateY(0) rotate(0deg);
        opacity: 1;
        border-radius: 0;
    }
    100%{
        transform: translateY(-1000px) rotate(720deg);
        opacity: 0;
        border-radius: 50%;
    }
}

.background {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    margin: 0;
    padding: 0;
    background: #e8ceb0;/*#e8ceb0;*/
    overflow: hidden;
}
.background li {
    position: absolute;
    display: block;
    list-style: none;
    width: 20px;
    height: 20px;
    background: rgba(205, 126, 29, 0.4);
    animation: animate 31s linear infinite;
}




.background li:nth-child(0) {
    left: 66%;
    width: 116px;
    height: 116px;
    bottom: -116px;
    animation-delay: 1s;
}
.background li:nth-child(1) {
    left: 3%;
    width: 143px;
    height: 143px;
    bottom: -143px;
    animation-delay: 3s;
}
.background li:nth-child(2) {
    left: 78%;
    width: 82px;
    height: 82px;
    bottom: -82px;
    animation-delay: 7s;
}
.background li:nth-child(3) {
    left: 27%;
    width: 118px;
    height: 118px;
    bottom: -118px;
    animation-delay: 15s;
}
.background li:nth-child(4) {
    left: 21%;
    width: 112px;
    height: 112px;
    bottom: -112px;
    animation-delay: 10s;
}
.background li:nth-child(5) {
    left: 43%;
    width: 126px;
    height: 126px;
    bottom: -126px;
    animation-delay: 14s;
}
.background li:nth-child(6) {
    left: 87%;
    width: 88px;
    height: 88px;
    bottom: -88px;
    animation-delay: 16s;
}
.background li:nth-child(7) {
    left: 6%;
    width: 141px;
    height: 141px;
    bottom: -141px;
    animation-delay: 26s;
}
.background li:nth-child(8) {
    left: 48%;
    width: 75px;
    height: 75px;
    bottom: -75px;
    animation-delay: 16s;
}
.background li:nth-child(9) {
    left: 77%;
    width: 70px;
    height: 70px;
    bottom: -70px;
    animation-delay: 27s;
}
.background li:nth-child(10) {
    left: 44%;
    width: 133px;
    height: 133px;
    bottom: -133px;
    animation-delay: 41s;
}
.background li:nth-child(11) {
    left: 34%;
    width: 116px;
    height: 116px;
    bottom: -116px;
    animation-delay: 25s;
}
.background li:nth-child(12) {
    left: 34%;
    width: 108px;
    height: 108px;
    bottom: -108px;
    animation-delay: 30s;
}
.background li:nth-child(13) {
    left: 17%;
    width: 113px;
    height: 113px;
    bottom: -113px;
    animation-delay: 55s;
}
.background li:nth-child(14) {
    left: 56%;
    width: 72px;
    height: 72px;
    bottom: -72px;
    animation-delay: 44s;
}
.background li:nth-child(15) {
    left: 51%;
    width: 139px;
    height: 139px;
    bottom: -139px;
    animation-delay: 65s;
}
.background li:nth-child(16) {
    left: 5%;
    width: 92px;
    height: 92px;
    bottom: -92px;
    animation-delay: 4s;
}
.background li:nth-child(17) {
    left: 87%;
    width: 76px;
    height: 76px;
    bottom: -76px;
    animation-delay: 35s;
}
.background li:nth-child(18) {
    left: 24%;
    width: 91px;
    height: 91px;
    bottom: -91px;
    animation-delay: 75s;
}
.background li:nth-child(19) {
    left: 47%;
    width: 144px;
    height: 144px;
    bottom: -144px;
    animation-delay: 25s;
}
.background li:nth-child(20) {
    left: 26%;
    width: 66px;
    height: 66px;
    bottom: -66px;
    animation-delay: 51s;
}
.background li:nth-child(21) {
    left: 26%;
    width: 68px;
    height: 68px;
    bottom: -68px;
    animation-delay: 61s;
}
.background li:nth-child(22) {
    left: 54%;
    width: 72px;
    height: 72px;
    bottom: -72px;
    animation-delay: 50s;
}
.background li:nth-child(23) {
    left: 6%;
    width: 93px;
    height: 93px;
    bottom: -93px;
    animation-delay: 75s;
}
.background li:nth-child(24) {
    left: 88%;
    width: 76px;
    height: 76px;
    bottom: -76px;
    animation-delay: 92s;
}
.background li:nth-child(25) {
    left: 15%;
    width: 86px;
    height: 86px;
    bottom: -86px;
    animation-delay: 96s;
}
.background li:nth-child(26) {
    left: 28%;
    width: 89px;
    height: 89px;
    bottom: -89px;
    animation-delay: 60s;
}
.background li:nth-child(27) {
    left: 80%;
    width: 95px;
    height: 95px;
    bottom: -95px;
    animation-delay: 3s;
}
.background li:nth-child(28) {
    left: 35%;
    width: 104px;
    height: 104px;
    bottom: -104px;
    animation-delay: 75s;
}
.background li:nth-child(29) {
    left: 53%;
    width: 139px;
    height: 139px;
    bottom: -139px;
    animation-delay: 57s;
}
.background li:nth-child(30) {
    left: 45%;
    width: 70px;
    height: 70px;
    bottom: -70px;
    animation-delay: 36s;
}
.background li:nth-child(31) {
    left: 10%;
    width: 98px;
    height: 98px;
    bottom: -98px;
    animation-delay: 100s;
}
.background li:nth-child(32) {
    left: 12%;
    width: 99px;
    height: 99px;
    bottom: -99px;
    animation-delay: 94s;
}
.background li:nth-child(33) {
    left: 65%;
    width: 79px;
    height: 79px;
    bottom: -79px;
    animation-delay: 80s;
}
.background li:nth-child(34) {
    left: 35%;
    width: 96px;
    height: 96px;
    bottom: -96px;
    animation-delay: 154s;
}
.background li:nth-child(35) {
    left: 17%;
    width: 108px;
    height: 108px;
    bottom: -108px;
    animation-delay: 90s;
}
.background li:nth-child(36) {
    left: 52%;
    width: 134px;
    height: 134px;
    bottom: -134px;
    animation-delay: 111s;
}
.background li:nth-child(37) {
    left: 89%;
    width: 98px;
    height: 98px;
    bottom: -98px;
    animation-delay: 93s;
}
.background li:nth-child(38) {
    left: 79%;
    width: 139px;
    height: 139px;
    bottom: -139px;
    animation-delay: 52s;
}
.background li:nth-child(39) {
    left: 4%;
    width: 67px;
    height: 67px;
    bottom: -67px;
    animation-delay: 60s;
}
.background li:nth-child(40) {
    left: 23%;
    width: 118px;
    height: 118px;
    bottom: -118px;
    animation-delay: 132s;
}
.background li:nth-child(41) {
    left: 44%;
    width: 125px;
    height: 125px;
    bottom: -125px;
    animation-delay: 72s;
}
.background li:nth-child(42) {
    left: 43%;
    width: 130px;
    height: 130px;
    bottom: -130px;
    animation-delay: 101s;
}
.background li:nth-child(43) {
    left: 39%;
    width: 99px;
    height: 99px;
    bottom: -99px;
    animation-delay: 14s;
}
.background li:nth-child(44) {
    left: 1%;
    width: 126px;
    height: 126px;
    bottom: -126px;
    animation-delay: 193s;
}
.background li:nth-child(45) {
    left: 39%;
    width: 132px;
    height: 132px;
    bottom: -132px;
    animation-delay: 169s;
}
.background li:nth-child(46) {
    left: 53%;
    width: 66px;
    height: 66px;
    bottom: -66px;
    animation-delay: 139s;
}
.background li:nth-child(47) {
    left: 60%;
    width: 127px;
    height: 127px;
    bottom: -127px;
    animation-delay: 38s;
}
.background li:nth-child(48) {
    left: 12%;
    width: 135px;
    height: 135px;
    bottom: -135px;
    animation-delay: 105s;
}
.background li:nth-child(49) {
    left: 65%;
    width: 68px;
    height: 68px;
    bottom: -68px;
    animation-delay: 118s;
}
</style>