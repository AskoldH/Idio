<template>
</template>
  
<script>
export default {
    name: "UserAuthentication",
    created() {
        this.checkCookies()
    },
    methods: {
        checkCookies() {
            // gets cookie for "id"
            const cookieValue = this.getCookie("id")

            // if cookie is undefined set cookie and create user
            if (!cookieValue) {
                const userCookieValue = new Date().getTime().toString()
                this.setUserIDCookie(userCookieValue)
                this.createIdioUser(userCookieValue)
            }
        },
        getCookie(name) {
            // gets cookie value by cookie given name
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
        },
        setUserIDCookie(userCookieValue) {
            // sets cookie value for name id = given argument
            let date = new Date();
            date.setTime(date.getTime() + (30 * 24 * 60 * 60 * 1000)); // 30 days in milliseconds
            let expires = "expires=" + date.toUTCString();
            document.cookie = "id=" + userCookieValue + ";" + expires + ";";
        },
        createIdioUser(userCookieValue) {
            // requests creating user with given userCookieValue (user id)
            this.$axios.post("http://localhost:8000/api/idio-user", { "user_cookie_value": userCookieValue }).then((response) => console.log(response))
                .catch(error => console.log(error))
        },
    }
}
</script>