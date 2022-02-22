<template>
  <div id="app">
    <div id="header"><img src="img/UCL_logo.png" height="40" alt=""><img src="img/GEStoryLogo.png" height="40" alt=""><img src="img/LouRIM.png" height="40" alt=""><a href="license.html">License</a></div>
    <BodyMap v-on:body-area-selected="onBodyAreaSelected($event)" :filteredData="filteredData"></BodyMap>
    <DataFilter v-model="filteredData"></DataFilter>
    <ItemDisplay></ItemDisplay>
    
  </div>
</template>

<script>
  import BodyMap from './components/BodyMap.vue'
  import DataFilter from './components/DataFilter.vue'
  import ItemDisplay from './components/ItemDisplay.vue'


  export default {
    name: "DesignSpaceApp",
    components: {
      BodyMap: BodyMap,
      DataFilter: DataFilter,
      ItemDisplay: ItemDisplay
    },
    data: function()  {
      return {
        filteredData: []
      }
    }
  };
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width:100%;
  display:flex;
  justify-content:space-between;
}
#header a {
  color:#2c3e50;
  text-decoration:none;
  margin-right:10px;
}

#footer {
  position: fixed;
  left: 0;
  bottom: 0;
  height: 80px;
  text-align: left;
  padding-bottom: 5px;
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

.logo {
  margin-left: 10px;
  padding: 2px;
}
</style>
