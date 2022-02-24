<template>
<div id="logGEStory">
    
    <form id="fLog" action class="form" @submit.prevent="loginAdmin" v-if="!loggedIn">
        <h2 >Login</h2>
      <p><label class="form-label" for="#userName">Username</label>
      <input
        v-model="userName"
        class="form-input"
        type="text"
        id="username"
        required
        placeholder="Type your username"
      ></p>
      <p><label class="form-label" for="#passwordU">Password</label>
      <input
        v-model="passwordU"
        class="form-input"
        type="password"
        id="passwordU"
        placeholder="Type your password"
      ></p>
      
      <input class="form-submit" type="submit" value="LOGIN">
    </form>

<p v-if="loggedIn">Welcome {{ userName }}. <a v-on:click.once="logOutAdmin">Log out</a></p>

</div>
  
</template>

<script>
export default {
    name: "LogGEStory",
    data: () => ({
    userName: "",
    passwordU: "",
    loggedIn: false

  }),
  methods: {
    loginAdmin() {
      console.log(this.userName);
      console.log(this.passwordU);
        this.loggedIn=true
    },
    logOutAdmin() {
       this.userName="",
        this.passwordU= "",
        this.loggedIn= false
  }
}
}
</script>

<style>

    

</style>