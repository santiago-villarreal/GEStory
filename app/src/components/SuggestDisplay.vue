<template>
<div id="suggestDisplay" v-if="item.name!=null">

<table class="detailTable" >
     <tr><td class="detailSugLa"><label class="form-label" for="#gesture">Gesture name</label></td>
      <td class="detailSug"><input
        v-model="item.name"
        class="form-inputSug"
        type="text"
        id="gesture"
        required
        
      ></td></tr>
			<tr><td class="detailSugLa"><label class="form-label" for="#GESName">GES Name</label></td>
      <td class="detailSug"><input
        v-model="item.title"
        class="form-inputSug"
        type="text"
        id="GESName"
        required
       
      ></td></tr>
    <tr><td class="detailSugLa"><label class="form-label" for="#authors">Authors</label></td>
       <td class="detailSug" id='listAuthors'><input
        v-model="item.authors"
        class="form-inputSug"
        type="text"
        id="author"
        required
       
      ></td></tr>
       <tr><td class="detailSugLa"><label class="form-label" for="#published">Published</label></td>
      <td class="detailSug"><input
        v-model="item.published"
        class="form-inputSug"
        type="text"
        id="published"
        required
        
      ></td></tr>
       <tr><td class="detailSugLa"><label class="form-label" for="#year">Year</label></td>
      <td class="detailSug"><input
        v-model="item.year"
        class="form-inputSug"
        type="number"
        id="year"
        required
       
      ></td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#urlGES">URL</label></td>
      <td class="detailSug"><input
        v-model="item.url"
        class="form-inputSug"
        type="text"
        id="urlGES"
        required
        
      ></td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#user">User</label></td>
      <td class="detailSug"><input
        v-model="item.user"
        class="form-inputSug"
        type="text"
        id="user"
        required
        
      ></td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#location">Location</label></td>
      <td class="detailSug"><input
        v-model="item.location"
        class="form-inputSug"
        type="text"
        id="bodyPart"
        required
       ></td></tr>
       
			<tr><td class="detailSugLa"><label class="form-label" for="#bodyPart">Body part</label></td>
      <td class="detailSug"><input
        v-model="item.body"
        class="form-inputSug"
        type="text"
        id="bodyPart"
        required
       ></td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#device">Device</label></td>
      <td class="detailSug"><input
        v-model="item.device"
        class="form-inputSug"
        type="text"
        id="device"
        required
        
      ></td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#environment">Environment</label></td>
      <td class="detailSug"><input
        v-model="item.environment"
        class="form-inputSug"
        type="text"
        id="environment"
        required
       
      ></td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#referent">Referent</label></td>
      <td class="detailSug"><input
        v-model="item.referent"
        class="form-inputSug"
        type="text"
        id="referent"
        required
        
      ></td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#typeG">Gesture Type</label></td>
      <td class="detailSug">
       <select v-model="item.type" class="form-inputSug" id="typeG" required>
        <option>Pointing</option>
        <option>Semaphoric Static</option>
        <option>Semaphoric Dynamic</option>
        <option>Semaphoric Stroke</option>
        <option>Pantomimic</option>
        <option>Iconic Static</option>
        <option>Iconic Dynamic</option>
        <option>Manipulation</option>
       </select>
        </td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#formG">Form</label></td>
      <td class="detailSug">
        <select v-model="item.form" class="form-inputSug" id="formG" required>
        <option>Static Gesture</option>
        <option>Dynamic Gesture</option>
       </select>
      </td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#nature">Nature</label></td>
      <td class="detailSug">
        <select v-model="item.nature" class="form-inputSug" id="nature" required>
        <option>Deictic</option>
        <option>Iconic</option>
        <option>Miming</option>
        <option>Physical</option>
       </select>
        </td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#symmetry">Symmetry</label></td>
      <td class="detailSug">
        <select v-model="item.symmetry" class="form-inputSug" id="symmetry" required>
        <option>Unilateral</option>
        <option>Bilateral-Symmetric</option>
        <option>Bilateral-Asymmetric</option>
       </select>
        </td></tr>
      <tr><td class="detailSugLa"><label class="form-label" for="#localeG">Locale Gesture</label></td>
      <td class="detailSug">
        <select v-model="item.locale" class="form-inputSug" id="localeG" required>
        <option>On-the-object</option>
        <option>In-the-air</option>
        <option>Mixed</option>
       </select>
      </td></tr>
      <tr v-if="item.agreement"><td class="detailSugLa"><label class="form-label" for="#agreement">Agreement</label></td>
      <td class="detailSug"><input
        v-model="item.agreement"
        class="form-inputSug"
        type="number"
        step="0.01"
        id="agreement"
       
      ></td></tr>
     <tr>
         <td ><button  v-on:click="downloadJSON()">Download JSON</button></td>
          <td class="detailSug"><button  v-on:click="sendGesture()">Send Gesture to Final list</button></td>
     </tr>


      
    </table>
        


</div>
  
</template>

<script>
	export default {
	name: "SuggestDisplay",
	data: function() {
		return {
			item: {}


		};
	},
	mounted() {
		this.$root.$on('detail-item', (i) => { this.item = i
		});
	},
	methods: {
        downloadJSON(){

            var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(this.item, null, 2));
            var downloadFile = document.createElement('a');
            downloadFile.setAttribute("href",     dataStr);
            downloadFile.setAttribute("download", this.item.name+this.item.title+this.item.year + ".json");
            downloadFile.click();
            downloadFile.remove();

        },
        sendGesture(){
            var gestureGEStory=require("@/../public/data/data.json");

            
            if(gestureGEStory.length!=0){
        //gestureGEStory.push(JSON.parse(this.item));
        gestureGEStory.push(this.item);
      // send JSON,  for Cli Vue, sent to localhost:8080
      (async () => {
        //var rawResponse = await fetch('http://localhost:8080/newGestureGEStory', {
          var rawResponse = await fetch('/newGestureGEStory', {
          method: 'POST', 
          body: JSON.stringify(gestureGEStory),
          headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              }});
             const content = await rawResponse.json();
             console.log(content.message); 
            
            })();
      console.log("New gesture in GEStory")
        }
        }
		
	}
	};
</script>

<style>
#suggestDisplay {
		width: 45%;
		position: fixed;
		top:100px;
		right:0;
		overflow-y: auto;
		max-height: 95%;
}
.detailSugLa{
width: 30%;
}
.detailSug{
width: 50%;
}
.form-inputSug{ 
width: 100%;
}
.detailTable{
   width: 80%; 
}

</style>