<template>
  <div id="adminGEStory">
    <div id="header"><img src="img/UCL_logo.png" height="40" alt=""><img src="img/GEStoryLogo.png" height="40" alt=""><img src="img/LouRIM.png" height="40" alt=""></div>
    <div id="contentSug">
      <h1> Manage GEStory</h1>
      <LogGEStory></LogGEStory>
    
    
<p><a href="index.html"> Go to GEStory</a></p>
    </div>
  </div>
</template>

<script>
import LogGEStory from '@/components/LogGEStory.vue'
 export default {
    name: "AdminPage",
    components: {
      LogGEStory:LogGEStory,
      
    },
  };
</script>

<style>
#suggest {
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
#contentSug {
  position: fixed;
  left: 15px;
  top: 0px;
  width: 90%;
}
</style>
