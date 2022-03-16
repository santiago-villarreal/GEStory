<template>
	<div id="itemDisplay">
		<h1 class="itemName">{{this.item.name| capitalize}}</h1>
		<h1 class="itemTitle">{{this.item.title}}</h1>
		<ul v-for="(author,index) in item.authors" 
			:key="index"
			id="authorList">
			<li class="author">{{author}}</li> 
		</ul>
		<figure v-if="item.image">
			<a :href="imageUrlForItem(item)" target="_blank" >
			<img 
			:src="item.image"
			:key="item.name"
			id="thumbnail" >
			</a>
			<figcaption>Image source: {{imageSourceForItem(item)}}</figcaption>
		</figure>
		<table class="details" v-if="item.name">
			<tr>
				<td class="detail">Published</td>
				<td>{{item.published}}</td>
			</tr>
			<tr>
				<td class="detail">Year</td>
				<td>{{item.year}}</td>
			</tr>
			<tr>
				<td class="detail">URL</td>
				<td><a :href="item.url" target="_blank">{{item.url}}</a></td>
			</tr>
			<tr v-if="item.user">
				<td class="detail">User type</td>
				<td><span v-for="(userT, index) in item.user" :key="index"><span v-if="index>0">, </span> {{userT | capitalize}}</span></td>
			</tr>
			<tr v-if="item.replication">
				<td class="detail">Replication</td>
				<td><p v-for="(repE, index) in item.replication" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></td>
			</tr>
			<tr v-if="item.replicationOf">
				<td class="detail">Is the replication of </td>
				<td><p v-for="(repE, index) in item.replicationOf" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></td>
			</tr>
			<tr v-if="item.generalization">
				<td class="detail">Generalization</td>
				<td><p v-for="(repE, index) in item.generalization" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></td>
			</tr>
			<tr v-if="item.generalizationOf">
				<td class="detail">Is the generalization of </td>
				<td><p v-for="(repE, index) in item.generalizationOf" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></td>
			</tr>
			<tr v-if="item.repurposing">
				<td class="detail">Repurposing</td>
				<td><p v-for="(repE, index) in item.repurposing" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></td>
			</tr>
			<tr v-if="item.repurposingOf">
				<td class="detail">Is the repurposing of </td>
				<td><p v-for="(repE, index) in item.repurposingOf" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></td>
			</tr>
			<tr v-if="item.body">
				<td class="detail">Body part</td>
				<td v-if="Array.isArray(item.body)"><span v-for="(userB, index) in item.body" :key="index"><span v-if="index>0">, </span> {{userB | capitalize}}</span></td>
				<td v-if="!Array.isArray(item.body)"> {{item.body | capitalize}}</td>
			</tr>
			<tr>
				<td class="detail">Device</td>
				<td>{{item.device | capitalize}}</td>
			</tr>
			<tr>
				<td class="detail">Environment</td>
				<td>{{item.environment | capitalize}}</td>
			</tr>
			<tr>
				<td class="detail" >Referent</td>
				<td>{{item.referent | capitalize}}</td>
			</tr>
			<tr>
				<td class="detail">Type</td>
				<td>{{item.type | capitalize}}</td>
			</tr>
			<tr>
				<td class="detail">Form</td>
				<td>{{item.form | capitalize}}</td>
			</tr>
			<tr>
				<td class="detail"> Nature</td>
				<td>{{item.nature | capitalize}}</td>
			</tr>
			<tr>
				<td class="detail">Symmetry</td>
				<td>{{item.symmetry | capitalize }}</td>
			</tr>
			<tr>
				<td class="detail">Locale gesture</td>
				<td>{{item.locale | capitalize}}</td>
			</tr>
			<tr v-if="item.perspective">
				<td class="detail">Perspective</td>
				<td><span v-for="(userP, index) in item.perspective" :key="index"><span v-if="index>0">, </span> {{userP | capitalize}}</span></td>
			</tr>
			<tr v-if="item.frame">
				<td class="detail">Frame</td>
				<td><span v-for="(userF, index) in item.frame" :key="index"><span v-if="index>0">, </span> {{userF | capitalize}}</span></td>
			</tr>
			<tr v-if="item.body_context">
				<td class="detail">Body context</td>
				<td><span v-for="(userBC, index) in item.body_context" :key="index"><span v-if="index>0">, </span> {{userBC | capitalize}}</span></td>
			</tr>
			<tr v-if="item.environmental_context">
				<td class="detail">Envrionmental context</td>
				<td><span v-for="(userE, index) in item.environmental_context" :key="index"><span v-if="index>0">, </span> {{userE | capitalize}}</span></td>
			</tr>
			<tr>
				<td class="detail"> Color</td>
				<td>{{item.color | capitalize}}</td>
			</tr>
			<tr v-if="item.gesture_elements">
				<td class="detail">Gesture elements</td>
				<td><span v-for="(userG, index) in item.gesture_elements" :key="index"><span v-if="index>0">, </span> {{userG | capitalize}}</span></td>
			</tr>
			<tr v-if="item.agreement">
				<td class="detail">Agreement</td>
				<td>{{item.agreement}}<div class="bar" :style="'--bar-value:'+(item.agreement*100)+'%;'" :title="'Agreement: '+item.agreement"></div></td>
			</tr>
			<tr>
				<td class="detail">Credibility</td>
				<td>{{item.credibility}}<div class="bar" :style="'--bar-value:'+(item.credibility*100)+'%;'" :title="'Credibility: '+item.credibility"></div></td>
			</tr>
		</table>
	</div>
</template>

<script>
	export default {
	name: "ItemDisplay",
	data: function() {
		return {
			item: {}
		};
	},
	mounted() {
		this.$root.$on('did-select-item', (i) => { this.item = i; 
		});
	},
	methods: {
		imageSourceForItem: function(item) {
			return  (item.imageSourceTitle) ? item.imageSourceTitle : item.url
		},
		imageUrlForItem: function(item) {
			return  (item.imageSource) ? item.imageSource : item.url
		}
	}
	}; //End export
</script>


<style scoped>
	#itemDisplay {
		width: 30%;
		position: fixed;
		top:55px;
		right:0;
		overflow-y: scroll;
		max-height: 95%;
		background-color: white;
		border-left: solid 2px black;
		margin-top : 5px;
		z-index : -1;
	}
	#authorList {
		display: inline table;
		list-style-type: none;
		margin: 0.25em 1em;
		padding: 0;
	}
	#author {
		display: table-cell;
		padding: 0;
	}

	h1.itemName {
		font-size: 1.5rem;
		font-weight: bold;
		margin: 0;
	}
	h1.itemTitle {
		font-size: 1rem;
		font-weight: bold;
		margin: 0;
	}

	table.details {
		margin:1em;
		text-align: left;
	}
	td.detail {
		font-weight: bold;
	}
	#thumbnail {
		display: block;
		width: 40%;
		margin: 1em auto 0 auto;
	}
	figcaption {
		font-size: 0.6rem;
		width: 75%;
		margin: 0 auto 0 auto;
	}
	/*bar*/
.bar {
    background-color:#05386b;
    width:var(--bar-value);
    height: 15px;
    align-self:flex-end;
    margin-left: 0px;
    border-radius:3px 3px 0 0;
	color: #fff;
	font-size: 80%;
	word-break:break-all;
	text-align: center;
    }
	.bar:hover{
		background-color: #F00;
		content: attr(title);
		font-size: 60%;

	}


@media (max-width: 700px) {
	#itemDisplay{
		width: 100%;
		height: 100%;
		margin-top : 2%;
	}

	table.details{
		margin-bottom : 25px;
	}
}

@media (max-width: 300px) {
	#itemDisplay{
		width: 100%;
		height: 100%;
		margin-top : 20%;
	}

	table.details{
		margin-bottom : 100px;
	}
}
</style>
