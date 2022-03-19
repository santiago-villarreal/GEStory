<template>
  <div id="app">
    <div id="header">
      <img src="img/UCL_logo.png" height="30" alt="">
      <img src="img/GEStoryLogo.png" height="25" alt="">
      <img src="img/LouRIM.png" height="30" alt="" class="endLogo">
      <input type="search" class="button searchbar" placeholder="Recherche..." @change="searchedWord($event)">
      <a class="button button1" href="license.html" v-if="window_Width">About</a>
      <a class="button button2" href="suggest.html" v-if="window_Width">Suggest a GES</a>
      <b-dropdown text="Block Level Dropdown" block variant="primary" class="m-2" v-if="!window_Width" size="sm">
        <b-dropdown-item href="license.html">About</b-dropdown-item>
        <b-dropdown-item href="suggest.html">Suggest a GES</b-dropdown-item>
      </b-dropdown>
    </div>
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
    },
    methods: {
      searchedWord : function (words){
        this.$root.$emit("searched-words", words.target.value)
      }
    },
    computed: {
      window_Width: function(){
				return window.innerWidth > 500;
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
.button {
  display: flex;
  text-decoration: none;
  margin-right: 10px;
  align-items: center;
  height: 27px;
  justify-content: center;
  border-radius: 10px;
}

.button1 {
  background-color: white;
  color: #c7b062;
  width: 65px;
}

.button2 {
  background-color: rgb(52, 51, 48);
  color: white;
  width: 135px;
}

.searchbar{
  padding: 1px;
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
  display: flex;
  align-items: center;
  z-index: 10;
}

.logo {
  margin-left: 10px;
  padding: 2px;
}

.endLogo{
  margin-right:auto
}

@media (max-width: 500px) {
	#header {
    justify-content: center;
    flex-wrap: wrap;
    align-items: center;
  }

  .searchbar{
    width: 175px;
  }

  .endLogo{
    margin-right:0px;
  }
}
</style>
