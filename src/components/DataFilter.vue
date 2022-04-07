
<template>
<div id="DataFilter" :class="mainClass()" >
	<div class="flex-container">
		<div id="filters" >

			<div
			v-for="(filter, index) in filters"
			v-bind:key="index"
			>
				<fieldset
				:id="'filter-'+index"
				v-bind:class="{ active: isFilterActive(filter) }"
				>
				<legend @click="toggleOpen(index)" :class="filter.open ?'open' : '' " :style="isFilterActive(filter) ? 'background-color: rgb(228, 206, 129);border-radius: 20px;padding: 5px;' : ''">{{filter.key | capitalize }}</legend>
          <div :class="filter.open ?'input-field-open' : 'input-field'" style="width: 93%;">
			<b-list-group>
				<b-list-group-item v-for="(value, vindex) in filter.values" :key="vindex">                
					<input :id="index+vindex+value" v-bind:type="filter.multipleSelection ?  'checkbox' : 'radio'"  :value="value" v-model="filter.filterValues" class="segmented-control__input" v-on:click="setPage(1)">
					<label class="segmented-control__label" :for="index+vindex+value">{{value | capitalize}}</label>
				</b-list-group-item>
			</b-list-group>
          </div>
		<!-- 			<div>{{subFiltersForFilter(filter)}}</div> -->
				</fieldset>
			</div>
			<div v-if="window_Width" style="display:flex; flex-direction:row;font-size: 14px;align-items: center;padding: 0px 10px;">
				<div id="enable" @click="toggleBody()">
					<div id="background"  :class="returnClass(0)">
						<div id="buttonSlide" :class="returnClass(1)"></div>
					</div>
				</div>
				<div>Toggle the Body Map</div>
				<div @click="resetFilters()" class="buttonReset">Reset filters</div>
			</div>
		</div>

	<!-- <span>Active filters: {{ activeFilters }}</span>
	<ul class="userWrap" v-if="tableView===false">-->

		<div>
			<!--<div>Number of gesture per page : <input type="number" min="20" max="80" :value="itemsPerPages" @change="updateItemPage($event)"></div>-->
			<div v-if="pageNumber>=1">
				<input id="slide" :style="'--number-page:' + Math.max(100/pageNumber, 10) + '%'" type="range" min="1" :max="pageNumber" step="1" v-model.number="page">
				<div><input type="number" :value="page" min="1" :max="pageNumber" @change="setPage($event)">/{{pageNumber}}</div>
			</div>
			<ul class="userWrap">
				<b-card-group columns
				v-for="(entry, index) in filteredDataPage"
				:key="index"
				:item="entry"
				class="user"
				:style="reduce && window_Width ? 'width:45%' : ''"
				v-on:click="$root.$emit('did-select-item',entry);"
				>
				<b-card
				no-body
				:header="entry.body"
				:header-bg-variant="switchBodyPart(entry.body)"
				tag="article"
				class="mb-2 card"
				>
					<b-card-body>
						<b-card-title>{{entry.name}}</b-card-title>
						<b-card-text>
						{{ entry.title | capitalize}}
						</b-card-text>
					</b-card-body>
					<b-list-group flush>
						<b-list-group-item>{{entry.year}}</b-list-group-item>
					</b-list-group>
					<template #footer>
						<div class="bar" :style="'--bar-value:'+(entry.credibility*100)+'%;'" :title="'Credibility: '+entry.credibility">{{entry.credibility}}</div>
					</template>
				</b-card>
				</b-card-group>
			</ul>
			<div v-if="pageNumber>=1">
				<input id="slide" :style="'--number-page:' + Math.max(100/pageNumber, 10) + '%'" type="range" min="1" :max="pageNumber" step="1" v-model.number="page">
				<div><input type="number" :value="page" min="1" :max="pageNumber" @change="setPage($event)">/{{pageNumber}}</div>
			</div>
		</div>
	</div>
</div>
</template>

<script>
	// The URL with the data to be shown and filtered
	// Will be fetched asynchronously which might fail (CORB)
	// Place the file in the public directory of your Vue.js project to be served locally
	const apiURL = "./data/data.json";

	/* A filter has the following structure:
	 * filter {
		key: String, 		// The field in the dataset which will be used to filter
		values: [],  		// the possible values for this key
		filterValues: [],	// the  values that are allowed for this key.
		multipleSelection: bool, // if multiple values are allowed, these will be connected through OR
	 }
	 */



	const gestureFilters = [
		{
		'key': 'body',
		'values': ["full-body", "finger", "hand", "wrist", "arm", "shoulder", "head", "foot", "torso"],
		'filterValues': [],
		'multipleSelection': true,
    'open': false,
		},
		{
		'key': 'device',
		'values': ["smart-phone","touch-surface","smart-ring","smart-watch","prototype", "no-device"],
		'filterValues': [],
		'multipleSelection': true,
    'open': false,
		},
		{
		'key': 'user',
		'values': ["Children","Teenagers","Adult","Elderly","Old"],
		'filterValues': [],
		'multipleSelection': true,
		'open': false,
    },
		{
		'key': 'task',
		'values': ["perform action", "scale", "next", "previous", "draw object", "rotate", "increase", "decrease", "deactivate", "activate", "ok", "cancel"],
		'filterValues': [],
		'multipleSelection': true,
		'open': false,
    },
		{
		'key': 'type',
		'values': ["Pointing", "Semaphoric\nStatic", "Semaphoric\nDynamic", "Semaphoric\nStroke", "Pantomimic", "Iconic\nStatic", "Iconic\nDynamic", "Manipulation"],
		'filterValues': [],
		'multipleSelection': true,
		'open': false,
    },
		{
		'key': 'form',
		'values': ["Static Gesture", "Dynamic Gesture"],
		'filterValues': [],
		'multipleSelection': true,
		'open': false,
    },
		{
		'key': 'nature',
		'values': ["Deictic", "Iconic", "Miming", "Physical"],
		'filterValues': [],
		'multipleSelection': true,
		'open': false,
    },
		{
		'key': 'symmetry',
		'values': ["Unilateral", "Bilateral-Symmetric", "Bilateral-Asymmetric"],
		'filterValues': [],
		'multipleSelection': true,
		'open': false,
    },
		{
		'key': 'locale',
		'values': ["On-the-object", "In-the-air", "Mixed"],
		'filterValues': [],
		'multipleSelection': true,
		'open': false,
    },
		{
		'key': 'year',
		'values': ["1999","2006","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"],
		'filterValues': [],
		'multipleSelection': true,
		'open': false,
    }

		/*{
		'key': 'Gesture type',
		'values': ["Poiting", "Semaphoric", "Pantomimic", "Iconic", "Manipulation"],
		'filterValues': [],
		'multipleSelection': false,
		'subfilters': []
		'open': false,
		},*/
	];

	/*{
		'key': 'type',
		'values': ["Accessories", "Clothing", "Skin & Body"],
		'filterValues': [],
		'multipleSelection': false,
		'subfilters': [] // Subfilters only work with multipleSelection: false
		'open': false,
		},*/

	//End gestureFilters

const subFilters = [];


/*
	const subFilters = [
	{
		'parent': 'Gesture type',
		'parentValue': 'Semaphoric',
		'key': 'subtype',
		'values': ["Static", "Dynamic", "Stroke"],
		'filterValues': [],
		'multipleSelection': false
	},
	{
		'parent': 'Gesture type',
		'parentValue': 'Iconic',
		'key': 'subtype',
		'values': ["Static", "Dynamic"],
		'filterValues': [],
		'multipleSelection': false
	}];
	*/
	// Alternative check https://gist.github.com/jherax/f11d669ba286f21b7a2dcff69621eb72
	// Based on https://stackoverflow.com/questions/44590352/filter-by-multiple-keys-and-values-javascript
	const useConditions = search => a => Object.keys(search).every(
		k => a[k] === search[k] ||
		Array.isArray(search[k]) && search[k].includes(a[k]) ||
		Array.isArray(search[k]) && Array.isArray(a[k]) && search[k].some(r => a[k].includes(r)) ||
		typeof search[k] === 'object' && +search[k].min <= a[k] &&  a[k] <= +search[k].max ||
		typeof search[k] === 'function' && search[k](a[k])
		);

	export default {
		name: "DataFilter",
		data: function() {
			return {
				filters: gestureFilters,		// The list of all possible filters, will be used later when the user can dynamically create a filter set
				activeFilters: [],  // The active filters
				data: [],			// The data this component works on
				page: 1,
				displayedFilter: 0,
				filter_page: [],
				reduce : "",
				enable : true,
				animate : 0,
				timer : false,
				searchedWord : "",
				itemsPerPages : 40
			};
		},
		created() {
			fetch(apiURL)
			.then(res => res.json())
			.then(res => (this.data = res, this.$root.$emit('data-is-loaded', this.data)))
			// eslint-disable-next-line no-console
			.catch(error => console.log(error));
		},
		mounted() {
			this.$root.$emit('body-filter', gestureFilters[0]);

			this.$root.$on('body-area-selected', (a) => {
				// Get the ID of the area filter
				let filter = this.filters.find(element => element.key == 'location');	//  Just make sure we only filter stuff that we know how to handle
				let area = a; // a is immutable
				if (area == "left-arm" || area == "right-arm") { // Arms have to be consolidated
					area = "arm"
				}
				if (filter) {
					// We want to toggle the filtervalues just as with the controls from this component
					let i = filter['filterValues'].indexOf(area);
					if (i>0) {
						filter['filterValues'].splice(i, 1);
					}
					// If we remove the last element, deactivate the filter alltogether
					else if (i==0) {
						filter['filterValues'].splice(i, 1);
						this.activeFilters.splice(this.filters.indexOf(filter), 1);
					}
					else {
						filter['filterValues'].push(area);
						this.activeFilters.push(this.filters.indexOf(filter));
					}
				}
			});
			this.$root.$on('input', (a)=>{
				this.page = 1;
				a;
			});
			this.$root.$on('did-select-item',(entry)=>{
				this.reduce = "reduce";
				return entry;
			});
			this.$root.$on("close-item", (event)=>{
				this.reduce = ""
				return event
			})
			this.$root.$on("searched-words", (words) =>{
				console.log(words)
				this.page = 1
				this.searchedWord = words
			})
		},
		watch: {
			filteredData: {
				handler: function (value) {
					this.$emit("input", value);
				},
				immediate: true
			},
			filteredDataPage: {
				handler: function (value) {
					this.$emit("input", value);
				},
				immediate: true
			},
			pageNumber : {
				handler: function (value) {
					this.$emit("input", value);
				},
				immediate: true
			},
			window_Width: {
				handler: function (value) {
					this.$emit("input", value);
				},
				immediate: true
			}
		},
		methods: {
      // eslint-disable-next-line no-mixed-spaces-and-tabs
		  toggleOpen: function (index){this.filters = this.filters.map((filter, i) => {if(index === i){filter.open = !filter.open;}return filter;});
      },
			subFiltersForFilter(filter) {
				return subFilters.filter( f => f.parent == filter.key && filter.filterValues.length > 0 && f.parentValue == filter.filterValues)
			},
			isFilterActive: function(filter) {
				console.warn(filter)
				console.log(this.filters)
				return this.filters[this.filters.indexOf(filter)].filterValues.length > 0;
			},
			isActive: function (number){
				return number - 1 == this.page ? "activePage" : ""
			},
			isSelected: function (id){
				return id == this.select || this.window_Width;
			},
			setPage: function (newPage){
				// https://attacomsian.com/blog/javascript-check-variable-is-object#:~:text=Unlike%20Array.isArray%20%28%29%20method%20which%20we%20used%20for,object%20is%20by%20using%20the%20Object.prototype.toString%20%28%29%20method.
				try{
					newPage = parseInt(newPage.target.value)
				}
				catch{
					console.log(newPage)
				}
				if (newPage <= this.pageNumber){
					this.page = newPage;
				}
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
			},
			toggleBody: function(){
				console.log(this.activeFilters)
				if (this.timer) return 0
				this.timer = true
				if (!this.enable){
					this.animate = -1
				}else{
					this.animate = 1
				}
				setTimeout(()=>{
					this.enable = !this.enable
					this.$root.$emit("enabled-body-map", this.enable)
					this.animate = 0
					this.timer = false
					const temp = this.page
					this.setPage(this.pageNumber)
					setTimeout(()=>{
						this.setPage(temp)
					}, 100)
				}, 500)

			},
			returnClass: function(x){
				let ret = ""
				if (x===1){  // slider button
					if (this.animate<0){
						ret += 'slideRight'
					}else if (this.animate>0){
						ret += 'slideLeft'
					}
					if (this.enable){
						ret += ' right'
					}
				} else{    // slider background
					if (this.animate<0){
						ret += 'slideWide'
					}else if (this.animate>0){
						ret += 'slideThin'
					}
					if (this.enable){
						ret += ' wide'
					}else{
						ret += " thin"
					}
				}
				return ret
			},
			mainClass: function(){
				let ret = this.reduce + " "
				if (!this.enable){
					ret += "margin-left-none"
				}else{
					ret += "margin-left-20"
				}
				return ret
			},
			updateItemPage : function (event){
				this.itemsPerPages = event.target.value
			},
			resetFilters : function (){
				for (let item of this.filters) {
					item.filterValues = []
				}
				return 0;
			}
		},
		computed: {
			filteredData: function () {
				// Collect all filterkeys, and their possible values
				let filterList = {};
				for (let item of this.filters) {
					if (item.filterValues.length>0){
						filterList[item['key']] = item['filterValues'];
					}
				}
				let temp = this.data
				for (let word of this.searchedWord.trim().split(" ")){
					temp = temp.filter( (item)=> item.name.toLowerCase().includes(word.toLowerCase()))
				}
				return temp
				.filter(useConditions(filterList))
				.sort((a,b)=>{return b.credibility - a.credibility});
			},
			filteredDataPage : function () {
				if (!this.filteredData){
					return [];
				}
				console.log(this.activeFilters)
				this.$root.$emit('pageNumber', this.filteredData.slice(this.page*this.itemsPerPages, (this.page+1)*this.itemsPerPages))
				return this.filteredData.slice((this.page-1)*this.itemsPerPages, this.page*this.itemsPerPages)
			},
			pageNumber : function (){
				let mod = (this.filteredData.length % this.itemsPerPages)
				return ((this.filteredData.length - mod)/this.itemsPerPages) + (mod != 0 ? 1 : 0)
			},
			window_Width: function(){
				return window.innerWidth > 500;
			}
		},
	};
</script>

<style scoped>
@keyframes slide{
	from {width: 20px;}
	to {width: 40px;}
}

@keyframes slide2{
	from {left: 0px;}
	to {left: 20px;}
}

.right{
	left: 20px;
}

.wide{
	width: 40px;
}

.thin{
	width: 20px;
}
.slideRight{
	animation-name: slide2;
	animation-duration: 0.5s;
	animation-timing-function: ease;
}

.slideLeft{
	animation-name: slide2;
	animation-duration: 0.5s;
	animation-timing-function: ease;
	animation-direction: reverse;
}

.slideWide{
	height: 20px;
	animation-name: slide;
	animation-duration: 0.5s;
	animation-timing-function: ease;
}

.slideThin{
	height: 20px;
	animation-name: slide;
	animation-duration: 0.5s;
	animation-timing-function: ease;
	animation-direction: reverse;
}

#enable{
	width: 40px;
	height: 20px;
	background-color: #656565;
	border-radius: 10px;
	display: inline-block;
    position: relative;
	z-index: 1;
}

#buttonSlide{
	position: relative;
	height: 20px;
	width: 20px;
	background-color: rgb(255, 255, 255);
	border-radius: 10px;
	border: 1px solid #a78a8a;
}

#background{
	height: 20px;
	background-color: rgb(63, 157, 159);
	position: relative;
	border-radius: 10px;
}

.reduce{
	margin-right:30%;
}

#DataFilter {
	margin-top:8%;
	width: 100%;
}

.margin-left-none{
	margin-left: 0px;
}

.margin-left-20{
	margin-left:20%;
}

.flex-container{
	display: flex;
	flex-direction: row;
}

.buttonReset{
	background-color: #c7b062;
    color: white;
    padding: 5px;
    border-radius: 17px;
    cursor: pointer;
	margin-left: auto;
}

.buttonReset:hover{
	background-color: #d0bf83;
}

/* The filter part */
[type="radio"]{
  display: none;
  z-index: 5;
  position: relative;
}

fieldset {
	padding: 0px 1em;
	text-align: left;
	display : flex;
	flex-wrap: wrap;
}

fieldset legend{
  position: relative;
  transition: all 0.4s;
}

fieldset legend::after{
  content: '';
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%) rotate(0deg);

  width: 30px;
  height: 30px;
  background-image:url("plus-symbol-button-svgrepo-com.svg");
  background-position: center;
  background-size: contain;
  background-repeat: no-repeat;
  transition: all 0.4s linear;
}
fieldset legend.open{
  margin-bottom: 10px;
}
fieldset legend.open::after{
  transform: translateY(-50%) rotate(135deg);
}

.active {
	border-color: #F00 ;
}

.input-field{
  opacity: 0;
  max-height: 15px;
  overflow-y: hidden;
  transition: all 1s;
}

.input-field-open{
  opacity: 1;
  max-height: 1000px;
  margin-bottom : 12px
}


.segmented-control {
  display: flex;
  width: 90%;
  margin: 0.25em 1em;
  padding: 0;
	flex-wrap: wrap;
	margin-bottom: 15px;
}

.segmented-control__item {
    display: table-cell;
    margin: 0;
    padding: 0;
    list-style-type: none;
	width : 33%;
}

.segmented-control__input {
    position: absolute;
    visibility: hidden;
}

.segmented-control__label {
    display: block;
    margin: 0 -1px -1px 0; /* -1px margin removes double-thickness borders between items */
    padding: 1em .25em;

    border: 1px solid #ddd;

    font: 14px/1.5 sans-serif;
    text-align: center;

    cursor: pointer;
	height: 40px;
}

.segmented-control__label:hover {
    background: #fafafa;
}

.segmented-control__input:checked + .segmented-control__label {
    background: #eee;
    color: #333;
}

/* Data UL */
.userWrap {
  list-style-type: none;
  padding: 2%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  flex-direction: row;
  justify-content: center;
}
.user {
  margin: 1% 1%;
  flex: 1 0 30%;
  text-align: left;
  cursor: pointer;
  min-width: 175px;
  max-width: 215px;
}
h2.title {
  font-size: 1.3rem;
  font-weight: bold;
  margin: 0;
}
.language {
  display: block;
  font-size: 0.9rem;
}
/*credibility bar*/
.bar {
    background-color:#05386b;
    width:var(--bar-value);
    align-self:flex-end;
    margin-left: 0px;
	color: #fff;
	font-size: 80%;
	word-break:break-all;
	text-align: center;
	height: 20px;
    border-radius: 5px;
    }
.bar:hover{
	background-color: #F00;
	content: attr(title);
	font-size: 60%;

}

.card{
	z-index:-1;
	height: 100%;
	display: flex;
}

.card-header{
	text-transform: capitalize;
}

.card-title{
	font-size: 14px;
	font-weight: bold;

}

.card-text{
	font-size: 12px;
}

#filters{
	flex: 0 0 35%;
}

input[type=number]{
	height: 18px;
}


@media (max-width: 700px) {
	#DataFilter{
		width: 90%;
		margin-top: 30%;
		margin-left: 5%;
		margin-right: 0%;
		padding-right: 0%;
	}

	#filters{
		width: 100%;
	}

	.segmented-control__item {
	width : 50%;
	}

	.user{
		width : 40%;
	}

	.flex-container{
		flex-direction: column;
	}

	input[type=number]{
		height: 30px;;
	}
}

@media (max-width: 500px) {
	.user{
		width : 100%;
		min-width: none;
	}
}

@media (max-width: 300px) {
	#DataFilter{
		width: 90%;
		margin-top: 60%;
		margin-left: 5%;
		margin-right: 0%;
		padding-right: 0%;
	}

	#filters{
		width: 100%;
	}

	.segmented-control__item {
	width : 100%;
	}
}

@media (max-width: 220px) {
	#DataFilter{
		margin-top: 80%;
	}
}


input[type=range] {
  height: 19px;
  -webkit-appearance: none;
  margin: 10px 0;
  width: 90%;
  z-index: -2;
}
input[type=range]:focus {
  outline: none;
}
input[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 10px;
  cursor: pointer;
  box-shadow: 1px 1px 2px #000000;
  background: #7D7D7D;
  border-radius: 5px;
  border: 1px solid #000000;
}
input[type=range]::-webkit-slider-thumb {
  box-shadow: 1px 1px 1px #000000;
  border: 1px solid #000000;
  height: 11px;
  width: var(--number-page);
  border-radius: 10px;
  background: #FFFFFF;
  cursor: pointer;
  -webkit-appearance: none;
  margin-top: -1.5px;
}
input[type=range]:focus::-webkit-slider-runnable-track {
  background: #7D7D7D;
}
input[type=range]::-moz-range-track {
  width: 100%;
  height: 10px;
  cursor: pointer;
  box-shadow: 1px 1px 2px #000000;
  background: #7D7D7D;
  border-radius: 5px;
  border: 1px solid #000000;
}
input[type=range]::-moz-range-thumb {
  box-shadow: 1px 1px 1px #000000;
  border: 1px solid #000000;
  height: 11px;
  width: 50px;
  border-radius: 10px;
  background: #FFFFFF;
  cursor: pointer;
}
input[type=range]::-ms-track {
  width: 100%;
  height: 10px;
  cursor: pointer;
  background: transparent;
  border-color: transparent;
  color: transparent;
}
input[type=range]::-ms-fill-lower {
  background: #7D7D7D;
  border: 1px solid #000000;
  border-radius: 10px;
  box-shadow: 1px 1px 2px #000000;
}
input[type=range]::-ms-fill-upper {
  background: #7D7D7D;
  border: 1px solid #000000;
  border-radius: 10px;
  box-shadow: 1px 1px 2px #000000;
}
input[type=range]::-ms-thumb {
  margin-top: 1px;
  box-shadow: 1px 1px 1px #000000;
  border: 1px solid #000000;
  height: 11px;
  width: 50px;
  border-radius: 10px;
  background: #FFFFFF;
  cursor: pointer;
}
input[type=range]:focus::-ms-fill-lower {
  background: #7D7D7D;
}
input[type=range]:focus::-ms-fill-upper {
  background: #7D7D7D;
}
</style>
