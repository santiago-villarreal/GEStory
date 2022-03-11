<template>
  <div id="suggest">
    <div id="header"><img src="img/UCL_logo.png" height="40" alt=""><img src="img/GEStoryLogo.png" height="40" alt=""><img src="img/LouRIM.png" height="40" alt=""></div>
    <div id="contentSug">
      <h1>Suggest a GES </h1>
    <p>Thank you for collaborating with us</p>
    <FormSuggest></FormSuggest>
    
<p><a href="javascript:history.back()"> Return</a></p>
    </div>
  </div>
</template>

<script>
import FormSuggest from '@/components/FormSuggest.vue'
 export default {
    name: "FormSuggestPage",
    components: {
      FormSuggest:FormSuggest,
      
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
  display: flex;
  align-items: center;
}
#contentSug {
  position: fixed;
  left: 15px;
  top: 0px;
  width: 90%;
  z-index : -1;
}

@media (max-width: 300px) {
  #contentSug{
    margin-top: 32%;
    position : absolute;  
  }

  #header {
    justify-content: space-between;
    flex-wrap: wrap;
  }
}
</style>
