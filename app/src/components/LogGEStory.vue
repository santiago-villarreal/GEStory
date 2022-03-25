<template>
<div id="logGEStory">
    <h1> Manage GEStory</h1>
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
      
      <input class="form-submit" type="submit" value="LOG IN">
    </form>
<p class="logError" v-if="loginFails">Incorrect username and/or password, please try again</p>
<p v-if="loggedIn">Welcome {{ userName | capitalize }}. <a v-on:click.once="logOutAdmin">Log out</a></p>

</div>
  
</template>

<script>
export default {
    name: "LogGEStory",
    data: () => ({
    userName: "",
    passwordU: "",
    loggedIn: false,
    loginFails: false,
    users:[]

  }),
  methods: {
    loginAdmin() {
      var foundUser=false;
       this.users=require("@/assets/users.json")
      for (var i=0; i<this.users.length;i++){
          if((this.users[i].nameUser==this.userName)&&(this.users[i].password==btoa(this.passwordU))){
            foundUser=true
          }}
      if(foundUser)this.$root.$emit('logIn-ok');else this.loginFails=true;
    },
    logOutAdmin() {
       this.userName="";
        this.passwordU= "";
        this.$root.$emit('logOut-ok')
      
  }
},
 mounted() {
      this.$root.$on('logIn-ok',() => {
            this.loggedIn=true;
            this.loginFails=false;
      });
      this.$root.$on('logOut-ok',() => {
            this.loggedIn=false;
      });
    }
}
</script>

<style>
p.logError {
 color: red;
}

    

</style>