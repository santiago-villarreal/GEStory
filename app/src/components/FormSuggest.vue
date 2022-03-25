<template>
<div id="formSuggest">
  <h1>Suggest a GES </h1>
    <p>Thank you for collaborating with us</p>
<div id="formDiv">
    <form id="fSuggestion" action class="form" @submit.prevent="GESinfo" v-if="!sentSuggestion">
        <h2 >About you</h2>
      <label class="form-label" for="#personName">Your Name</label>&#9;
      <input
        v-model="personName"
        class="form-input"
        type="text"
        id="personName"
        required
        placeholder="Santiago Villarreal-Narvaez"
      >      &Tab;  &#9;  &#x9;
      <label class="form-label" for="#emailP">Email</label>&#9;
      <input
        v-model="emailP"
        class="form-input"
        type="email"
        id="emailP"
        required
        placeholder="santiago.villarreal@uclouvain.be"
      >
      <h2 >About GES</h2>
      <table class="details" >
			<tr><td class="detail"><label class="form-label" for="#GESName">GES Name</label></td>
      <td class="detail"><input
        v-model="GESName"
        class="form-input"
        type="text"
        id="GESName"
        required
        placeholder="Title of GES"
      ></td></tr>
    <tr><td class="detail"><label class="form-label" for="#authors">Authors</label></td>
       <td class="detail" id='listAuthors'><input
        v-model="author"
        class="form-input"
        type="text"
        id="author"
        required
        placeholder="Taralle, Florent and Paljic, Alexis and Manitsaris, Sotiris"
      >&#9; Use 'and' to separate authors</td></tr>
       <tr><td class="detail"><label class="form-label" for="#published">Published</label></td>
      <td class="detail"><input
        v-model="published"
        class="form-input"
        type="text"
        id="published"
        required
        placeholder="ACM"
      ></td></tr>
       <tr><td class="detail"><label class="form-label" for="#year">Year</label></td>
      <td class="detail"><input
        v-model="year"
        class="form-input"
        type="number"
        id="year"
        required
        placeholder="2022"
      ></td></tr>
      <tr><td class="detail"><label class="form-label" for="#urlGES">URL</label></td>
      <td class="detail"><input
        v-model="urlGES"
        class="form-input"
        type="text"
        id="urlGES"
        required
        placeholder="http://doi.acm.org/10.1145/2702613.2702971"
      ></td></tr>
      <tr><td class="detail"><label class="form-label" for="#user">User</label></td>
      <td class="detail"><input
        v-model="user"
        class="form-input"
        type="text"
        id="user"
        required
        placeholder="adult, children, elderly, old"
      >&#9; Use ',' to separate users</td></tr>
      </table>
      <h2 >Gesture</h2>
      <table class="details" >
        <tr><td class="detail"><label class="form-label" for="#gesture">Gesture name</label></td>
      <td class="detail"><input
        v-model="gesture"
        class="form-input"
        type="text"
        id="gesture"
        required
        placeholder="Thumb up, fist, tap, etc"
      ></td></tr>
			<tr><td class="detail"><label class="form-label" for="#bodyPart">Body part</label></td>
      <td class="detail"><input
        v-model="bodyPart"
        class="form-input"
        type="text"
        id="bodyPart"
        required
        placeholder="Full-body, finger, hand, wrist, arm, etc."
      ></td></tr>
      <tr><td class="detail"><label class="form-label" for="#device">Device</label></td>
      <td class="detail"><input
        v-model="device"
        class="form-input"
        type="text"
        id="device"
        required
        placeholder="No-device, Kinect, Leap Motion, etc"
      ></td></tr>
      <tr><td class="detail"><label class="form-label" for="#environment">Environment</label></td>
      <td class="detail"><input
        v-model="environment"
        class="form-input"
        type="text"
        id="environment"
        required
        placeholder="Tv, Unmanned Aerial Vehicle (UAV), smartcar, IoT, etc"
      ></td></tr>
      <tr><td class="detail"><label class="form-label" for="#referent">Referent</label></td>
      <td class="detail"><input
        v-model="referent"
        class="form-input"
        type="text"
        id="referent"
        required
        placeholder="Roll rotation, increase octave, delete, move, etc"
      >&#9; Use ',' to separate referents</td></tr>
      <tr><td class="detail"><label class="form-label" for="#typeG">Gesture Type</label></td>
      <td class="detail">
       <select v-model="typeG" class="form-input" id="typeG" required>
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
      <tr><td class="detail"><label class="form-label" for="#formG">Form</label></td>
      <td class="detail">
        <select v-model="formG" class="form-input" id="formG" required>
        <option>Static Gesture</option>
        <option>Dynamic Gesture</option>
       </select>
      </td></tr>
      <tr><td class="detail"><label class="form-label" for="#nature">Nature</label></td>
      <td class="detail">
        <select v-model="nature" class="form-input" id="nature" required>
        <option>Deictic</option>
        <option>Iconic</option>
        <option>Miming</option>
        <option>Physical</option>
       </select>
        </td></tr>
      <tr><td class="detail"><label class="form-label" for="#symmetry">Symmetry</label></td>
      <td class="detail">
        <select v-model="symmetry" class="form-input" id="symmetry" required>
        <option>Unilateral</option>
        <option>Bilateral-Symmetric</option>
        <option>Bilateral-Asymmetric</option>
       </select>
        </td></tr>
      <tr><td class="detail"><label class="form-label" for="#localeG">Locale Gesture</label></td>
      <td class="detail">
        <select v-model="localeG" class="form-input" id="localeG" required>
        <option>On-the-object</option>
        <option>In-the-air</option>
        <option>Mixed</option>
       </select>
      </td></tr>
      <tr><td class="detail"><label class="form-label" for="#agreement">Agreement</label></td>
      <td class="detail"><input
        v-model="agreement"
        class="form-input"
        type="number"
        step="0.01"
        id="agreement"
        placeholder="0.81"
      ></td></tr>
        </table>
      <p><input class="form-submit" type="submit" value="Send Gesture"></p>
    </form>

<p v-if="sentSuggestion">Your suggestion has been sent, thank you. <a v-on:click.once="otherSuggestion">Send another Gesture</a></p>
</div>
<div id="classificationHelp">
<p>To help the classification</p>
<p>Gesture type from Aignes et al., "Understanding Mid-Air Hand Gestures: A Study of Human Preferences in Usage of Gesture Types for HCI"  : </p>
<p>This classification is more oriented to gestures made with the hands, 
  so we opted that the parts of the body that performed the gesture were 
  taken into account as if it were the hand, for example in Lee et al. 
  in "Bodily input for wearables: an elicitation study" and there are gestures 
  that perform it with feet or Yan et al. in "Gesture-based target acquisition 
  in virtual and augmented
reality" with head</p>
<img src="img/TypeG.png" width="70%" alt="">
<p>Gesture Taxonomy</p>
<img src="img/ClassG.png" width="90%" alt="">

</div>

</div>
  
</template>

<script>
export default {
    name: "FormSuggest",
    data: () => ({
    personName: "",
    emailP: "",
    GESName: "",
    author:'',
    published:'',
    year:'',
    urlGES: "",
    user:'',
    gesture:'',
    bodyPart:'',
    device:'',
    environment:'',
    referent:'',
    typeG:'',
    formG:'',
    nature:'',
    symmetry:'',
    localeG:'',
    agreement:'',
    sentSuggestion: false,
    newGesture:[],
    listGestures:[],
     urlJson:"./data/GESlist.json",
     
  }),
  created() {
			fetch(this.urlJson)
			.then(res => res.json())
			.then(res => this.listGestures = res)
			.catch(error => console.log(error));
      
		},
  methods: {
    GESinfo() {
      this.newGesture='{'+
      '"name":"'+this.gesture+'",'+
      '"title":"'+this.GESName+'",'+
      '"authors":'+this.toAuthors(this.author)+
      '"published":"'+this.published+'",'+
      '"year":'+this.year+','+
      '"url":"'+this.urlGES+'",'+
      '"user":'+this.toComma(this.user)+
      '"location":"'+this.bodyPart+'",'+
      '"body":"'+this.bodyPart+'",'+
      '"device":"'+this.device+'",'+
      '"environment":"'+this.environment+'",'+
      '"referent":'+this.toComma(this.referent)+
      '"type":"'+this.typeG+'",'+
      '"form":"'+this.formG+'",'+
      '"nature":"'+this.nature+'",'+
      '"symmetry":"'+this.symmetry+'",'+
      '"locale":"'+this.localeG+'",';
      if(this.agreement){this.newGesture+='"agreement":'+this.agreement+',';}
      this.newGesture+='"namePerso":"'+this.personName+'",'+
      '"emailP":"'+this.emailP+'",'+
      '"checked":"noChecked"'+
      '}';
      //console.log(this.newGesture);
      this.listGestures.push(JSON.parse(this.newGesture));
      // send JSON,  for Cli Vue, sent to localhost:8080
      (async () => {
        //var rawResponse = await fetch('http://localhost:8080/newGestureSug', {
          var rawResponse = await fetch('/newGestureSug', {
          method: 'POST', 
          body: JSON.stringify(this.listGestures),
          //body: this.listGestures,
          headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              }});
             const content = await rawResponse.json();
             console.log(content.message); 
            
            })();
      console.log("Send JSON")
      //console.log(this.listGestures)
      this.sentSuggestion=true
    },
    otherSuggestion() {
    this.gesture='',
    this.bodyPart='',
    this.device='',
    this.environment='',
    this.referent='',
    this.typeG='',
    this.formG='',
    this.nature='',
    this.symmetry='',
    this.localeG='',
    this.agreement='',
    this.newGesture='',
    this.sentSuggestion= false
    
  },
  toAuthors(xw){
    if(xw.includes(' and ')){xw=xw.replaceAll(' and ','","')}
    return '["'+xw+'"],';
  },
  toComma(xw){ 
    if(xw.includes(', '|| ' , '||', '||',')){xw=xw.replaceAll(', '|| ' , '||', '||',','","')}
    return '["'+xw+'"],';
  }
  //cotinue methode
}
}
</script>

<style>
#formSuggest{
  width: 100%;
 
}
#formDiv{
  width: 45%;
  position: fixed;
		top:150px;
		left:3%;
  overflow-y: auto;
	max-height: 77%;
}
#classificationHelp{
  width: 50%;
  top: 90px;
	right: 0%;
	position: fixed;
  overflow-y: auto;
	max-height: 85%;
}


</style>