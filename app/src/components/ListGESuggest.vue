<template>

<div id="listGESuggest">
    <ul class="listGES">
        <li
        v-for="(gesture, index) in this.ges"
        :key="index"
        :item="gesture"
        class="gesStyle"
        >
        
          <h2 class="title">{{ gesture.name | capitalize}}</h2>
          <span class="language">{{ gesture.title | capitalize}}</span>
          <span class="language">{{ gesture.authors | capitalize}}</span>
          <span class="language"><a :href="gesture.url" target="_blank">{{ gesture.url }}</a></span>
          <span class="language">Recommended by: {{ gesture.namePerso | capitalize}}, <a :href="'mailto:'+gesture.emailP" target="_blank">{{gesture.emailP}}</a></span>
          <button id="bDelete" v-on:click="deleteGes(index)">Delete</button>
          <button  v-on:click="showDetail(index)">Detail</button>
          <div :class="gesture.checked"  v-on:click="changeChecked(index)"></div>
          
        </li>
  </ul>
  <button id="buttonSave" v-on:click="saveChanges">Save Checked</button>
</div>

</template>

<script>


export default {
    name: "ListGESuggest",
    data: () => ({
    urlJson:"./data/GESlist.json",
    ges:[]
  }),
  created() {
			fetch(this.urlJson)
			.then(res => res.json())
			.then(res => this.ges = res)
			.catch(error => console.log(error));
		},
        methods: {
            changeChecked(index){
                if(this.ges[index].checked=="checked"){this.ges[index].checked="noChecked" }
                else{this.ges[index].checked="checked"}
            },
            saveChanges(){
                (async () => {
            var rawResponse = await fetch('http://localhost:8080/newGestureSug', {
            //var rawResponse = await fetch('/newGestureSug', {
                 method: 'POST', 
                 body: JSON.stringify(this.ges),         
                 headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
                   }});
                  const content = await rawResponse.json();
                  console.log(content.message); 
            
            })();
               console.log("Send JSON")
              },
              deleteGes(index){
                this.ges.splice(index,1);
              },
              showDetail(index){
              this.$root.$emit('detail-item', this.ges[index])
              }

        }

}
</script>

<style>
#listGESuggest{
width: 45%;
position: fixed;
top:150px;
left:3%;
overflow-y: auto;
max-height: 75%
}
#buttonSave{
position: fixed;
bottom:1%;
left:2.5%;

}
#bDelete{
position:absolute;
bottom:5%;
right:2.5%;
}

.listGES {
  list-style-type: none;
  padding: 2%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  flex-direction: row;
}

.gesStyle{
  position: relative;
  padding: 10px;
  margin: 1% 0;
  border: 1px solid rgb(3, 12, 92);
  border-radius: 3px;
  width: 80%;
  
  
}
.checked{
  transform: rotateZ(180deg);
  transition:all .5s ease-in-out;
  position: absolute;
  width: 5%;
  height: 20%;
  background-color: greenyellow;
  top: 10%;
  right: 3%;
  padding: 10px;
  margin: 1% 0;
  border: 1px solid #ddd;
  border-radius: 3px;
  
}
.noChecked{

  transition:all .5s ease-in-out;
  position: absolute;
  padding: 10px;
  margin: 1% 0;
  border: 1px solid #ddd;
  border-radius: 3px;
  width: 5%;
  height: 20%;
  text-align: left;
  background-color: red;
  top: 10%;
  right: 3%;
  
}

h2.title {
  font-size: 1.3rem;
  font-weight: bold;
  margin: 0;
  width: 80%;
}
.language {
  display: block;
  font-size: 0.9rem;
  width: 80%;
}

</style>