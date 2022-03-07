<template>
<div id="formSuggest">
    
    <form id="fSuggestion" action class="form" @submit.prevent="GESinfo" v-if="!sentSuggestion">
        <h2 >About you</h2>
      <label class="form-label" for="#personName">Your Name</label>
      <input
        v-model="personName"
        class="form-input"
        type="text"
        id="personName"
        required
        placeholder="Santiago Villarreal-Narvaez"
      >
      <label class="form-label" for="#email">Email</label>
      <input
        v-model="email"
        class="form-input"
        type="email"
        id="email"
        placeholder="santiago.villarreal@uclouvain.be"
      >
      <h2 >About GES</h2>
      
      <label class="form-label" for="#GESName">GES Name</label>
      <input
        v-model="GESName"
        class="form-input"
        type="text"
        id="GESName"
        required
        placeholder="Title of GES"
      >
    <label class="form-label" for="#authors">Authors</label>
      <input
        v-model="authors"
        class="form-input"
        type="text"
        id="authors"
        required
        placeholder="Leng, Hoo Yong and Norowi, Noris Mohd and Jantan, Azrul Hazri"
      >
      <label class="form-label" for="#urlGES">URL</label>
      <input
        v-model="urlGES"
        class="form-input"
        type="text"
        id="urlGES"
        required
        placeholder="http://doi.acm.org/10.1145/2702613.2702971"
      >
      <input class="form-submit" type="submit" value="Send suggestion">
    </form>

<p v-if="sentSuggestion">Your suggestion has been sent, thank you. <a v-on:click.once="otherSuggestion">Send another</a></p>

</div>
  
</template>

<script>
export default {
    name: "FormSuggest",
    data: () => ({
    personName: "",
    email: "",
    GESName: "",
    authors: "",
    urlGES: "",
    sentSuggestion: false

  }),
  methods: {
    GESinfo() {
      console.log(this.personName);
      console.log(this.email);
      console.log(this.GESName);
      console.log(this.authors);
      console.log(this.urlGES);
        this.sentSuggestion=true
    },
    otherSuggestion() {
       this.personName="",
    this.email= "",
    this.GESName= "",
    this.authors= "",
    this.urlGES= "",
    this.sentSuggestion= false
  }
}
}
</script>

<style>
	@media (max-width: 300px) {
    #contentSug{
      margin-top: 32%;
      position : absolute;  
    }
  }
    

</style>