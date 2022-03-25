<template>
  <div id="adminGEStory">
    <div id="header"><img src="img/UCL_logo.png" height="40" alt=""><a href="adminGEStory.html"><img src="img/GEStoryLogo.png" height="40" alt=""></a><img src="img/LouRIM.png" height="40" alt=""></div>
    <div id="contentLog">
      
      <FormSuggest v-if="titlePage=='SuggestGES'"></FormSuggest>
      <LogGEStory v-if="titlePage!='SuggestGES'"></LogGEStory>
      <ListGESuggest v-if="loggedIn"></ListGESuggest>
      <SuggestDisplay v-if="loggedIn"></SuggestDisplay>
    
    
<p><a href="/"> Go to GEStory</a></p>
    </div>
  </div>
</template>

<script>
import LogGEStory from '@/components/LogGEStory.vue'
import ListGESuggest from '@/components/ListGESuggest.vue';
import FormSuggest from '@/components/FormSuggest.vue';
import SuggestDisplay from '@/components/SuggestDisplay.vue';
 export default {
    name: "AdminPage",
    components: {
      LogGEStory:LogGEStory,
      ListGESuggest:ListGESuggest,
      FormSuggest:FormSuggest,
        SuggestDisplay:SuggestDisplay
      
    },
     data: () => ({
       loggedIn: false,
       titlePage:''
     }),
    mounted() {
      this.titlePage= document.getElementById('pageTitle').innerHTML
      this.$root.$on('logIn-ok',() => {
            this.loggedIn=true;
      });
      this.$root.$on('logOut-ok',() => {
            this.loggedIn=false;
      });

    }
  };

 
</script>

<style>
#adminGEStory {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width:100%;
}
a {
  text-decoration: none;
  color: #D99100;
}
#header {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  padding: 5px;
  background-color:  #c7b062;
  color: white;
  text-align: right;
}
#contentLog {
  position: fixed;
  left: 15px;
  top: 0px;
  width: 90%;
}
</style>
