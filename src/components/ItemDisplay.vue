<template>
	<div id="itemDisplay" v-if="Object.entries(item).length !== 0">

		<div>
			<b-card
				no-body
				:header-bg-variant="switchBodyPart(item.body)"
				:border-variant="switchBodyPart(item.body)"
			>
				<template #header>
					<center style="    position: relative; left: 15px;">About the gesture<img v-if="window_Width" src="../../public/img/window-close-regular-24.png" height="15px" style="position : relative;top: -12px;left: 15%;" @click="gestureClose($event)"></center>
				</template>

				<b-card-body>
				<b-card-title>{{this.item.name| capitalize}}</b-card-title>
				<b-card-sub-title class="mb-2">By : 		
					<ul v-for="(author,index) in item.authors" 
						:key="index"
						id="authorList">
					<li class="author">{{author}}</li> 
					</ul>
				</b-card-sub-title>
				<b-card-text>
					{{this.item.title}}
				</b-card-text>
				<b-card-img :src="item.image" v-if="item.image" bottom></b-card-img>
				<b-list-group flush>
				<b-list-group-item v-if="item.image" style="justify-content : center"><b-button :href="imageSourceForItem(item)" variant="primary">Source of image</b-button></b-list-group-item>
				<b-list-group-item style="justify-content : center"><b-button :href="item.url" variant="primary">Gesture's study</b-button></b-list-group-item>
				
				<b-list-group-item><span>Year :</span><span>{{item.year}}</span></b-list-group-item>
				
				<b-list-group-item v-if="item.published"><span>Published :</span><span>{{item.published}}</span></b-list-group-item>

				<b-list-group-item><span>User type :</span><span v-for="(userT, index) in item.user" :key="index"><span v-if="index>0">, </span> {{userT | capitalize}}</span></b-list-group-item>

				<b-list-group-item v-if="item.replication"><span>Replication :</span><p v-for="(repE, index) in item.replication" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></b-list-group-item>

				<b-list-group-item v-if="item.replicationOf"><span>Replication of :</span><span><p v-for="(repE, index) in item.replicationOf" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></span></b-list-group-item>

				<b-list-group-item v-if="item.generalization"><span>Generalization :</span><p v-for="(repE, index) in item.generalization" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></b-list-group-item>

				<b-list-group-item v-if="item.generalizationOf"><span>Generalization of :</span><p v-for="(repE, index) in item.generalizationOf" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></b-list-group-item>

				<b-list-group-item v-if="item.repurposing"><span>Repurposing :</span><p v-for="(repE, index) in item.repurposing" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></b-list-group-item>

				<b-list-group-item v-if="item.repurposingOf"><span>Repurposing of :</span><p v-for="(repE, index) in item.repurposingOf" :key="index"> <a :href="repE[1]" target="_blank"> {{repE[0] | capitalize}} </a></p></b-list-group-item>

				<b-list-group-item><span>Body part :</span>
					<span v-if="Array.isArray(item.body)"><span v-for="(userB, index) in item.body" :key="index"><span v-if="index>0">, </span> {{userB | capitalize}}</span></span> 
					<span v-if="!Array.isArray(item.body)"> {{item.body | capitalize}}</span>

				</b-list-group-item>

				<b-list-group-item><span>Device :</span><span>{{item.device | capitalize}}</span></b-list-group-item>

				<b-list-group-item><span>Environment :</span><span>{{item.environment | capitalize}}</span></b-list-group-item>

				<b-list-group-item><span>Referent :</span><span>{{item.referent | capitalize}}</span></b-list-group-item>

				<b-list-group-item><span>Type :</span><span>{{item.type | capitalize}}</span></b-list-group-item>

				<b-list-group-item><span>Form :</span><span>{{item.form | capitalize}}</span></b-list-group-item>

				<b-list-group-item><span>Nature :</span><span>{{item.nature | capitalize}}</span></b-list-group-item>

				<b-list-group-item><span>Symmetry :</span><span>{{item.symmetry | capitalize }}</span></b-list-group-item>

				<b-list-group-item><span>Locale gesture :</span><span>{{item.locale | capitalize}}</span></b-list-group-item>

				<b-list-group-item v-if="item.perspective"><span>Perspective :</span><span v-for="(userP, index) in item.perspective" :key="index"><span v-if="index>0">, </span> {{userP | capitalize}}</span></b-list-group-item>

				<b-list-group-item v-if="item.frame"><span>Frame :</span><span v-for="(userF, index) in item.frame" :key="index"><span v-if="index>0">, </span> {{userF | capitalize}}</span></b-list-group-item>

				<b-list-group-item v-if="item.body_context"><span>Body context :</span><span v-for="(userBC, index) in item.body_context" :key="index"><span v-if="index>0">, </span> {{userBC | capitalize}}</span></b-list-group-item>

				<b-list-group-item v-if="item.environmental_context"><span>Envrionmental context :</span><span v-for="(userE, index) in item.environmental_context" :key="index"><span v-if="index>0">, </span> {{userE | capitalize}}</span></b-list-group-item>

				<b-list-group-item><span>Color :</span><span>{{item.color | capitalize}}</span></b-list-group-item>

				<b-list-group-item v-if="item.gesture_elements"><span>Gesture elements :</span><span v-for="(userG, index) in item.gesture_elements" :key="index" style="width:100%"> {{userG | capitalize}}</span></b-list-group-item>

				</b-list-group>

				</b-card-body>


				<b-card-footer>
					Credibility : {{item.credibility}}<div class="bar" :style="'--bar-value:'+(item.credibility*100)+'%;'" :title="'Credibility: '+item.credibility"></div>
				</b-card-footer>

				<b-card-footer v-if="item.agreement">
					Agreement : {{item.agreement}}<div class="bar" :style="'--bar-value:'+(item.agreement*100)+'%;'" :title="'Agreement: '+item.agreement"></div>
				</b-card-footer>

			</b-card>
		</div>
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
		},
		gestureClose: function(event) {
			this.$root.$emit("close-item", this.item);
			this.item = {};
			console.log(event)
			return 0;
		},
		switchBodyPart: function(area){
				switch(area){
					case("arm"):
						return "primary"
					case("wrist"):
						return "primary"
					case("finger"):
						return "success"
					case("torso"):
						return "info"
					case("head"):
						return "info"
					case("shoulder"):
						return "info"
					case("full-body"):
						return "warning"
					case("hand"):
						return "danger"
					default:
						return "secondary"
				}
			}
		},
		window_Width: function(){
			return window.innerWidth > 500;
		}
	}; //End export
</script>


<style scoped>

	.card{
		max-width: 20rem; 
		margin-bottom : 50px
	}

	.list-group-item{
		display: flex;
		justify-content: space-between;
		flex-wrap: wrap;
	}

	.list-group-item span{
		font-size: 14px;
	}

	#itemDisplay {
		width: 30%;
		position: fixed;
		top:55px;
		right:0;
		overflow-y: scroll;
		max-height: 95%;
		background-color: white;
		margin-top : 5px;
		z-index: 1;
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

}

@media (max-width: 300px) {
	#itemDisplay{
		width: 100%;
		height: 100%;
		margin-top : 20%;
	}

	.card{
		margin-bottom: 100px;
		margin-top : 60px;
		width: 95%;
		margin-left: 2.5%;
	}
}
</style>
