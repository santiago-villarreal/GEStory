
<template>
<div id="DataFilter">
	<div id="filters">
		<fieldset
			v-for="(filter, index) in filters"
			v-bind:key="index"
			:id="'filter-'+index"
			v-bind:class="{ active: isFilterActive(filter) }"
		>
		<legend>{{filter.key | capitalize }}</legend>
			<input :id="'filter-'+index+'-enable'" type="checkbox" :value="index" v-model="activeFilters">
			<ul	class="segmented-control">
				<li v-for="(value, vindex) in filter.values" :key="vindex" class="segmented-control__item">
					<input :id="index+vindex+value" v-bind:type="filter.multipleSelection ?  'checkbox' : 'radio'"  :value="value" v-model="filter.filterValues" class="segmented-control__input">
					<label class="segmented-control__label" :for="index+vindex+value">{{value | capitalize}}</label>
				</li>
			</ul>
<!-- 			<div>{{subFiltersForFilter(filter)}}</div> -->
		</fieldset>
	</div>
	<input type="checkbox" name="tableView" value="true" /> Table view
<!-- <span>Active filters: {{ activeFilters }}</span>
 <ul class="userWrap" v-if="tableView===false">-->
<ul class="userWrap">
	<li
	v-for="(entry, index) in filteredData"
	:key="index"
	:item="entry"
	class="user"
	v-on:click="$root.$emit('did-select-item',entry);"
	>
		<h2 class="title">{{ entry.name | capitalize}}</h2>
		<span class="language"><strong>{{ entry.title | capitalize}}</strong></span>
		<div class="bar" :style="'--bar-value:'+(entry.credibility*100)+'%;'" :title="'Credibility: '+entry.credibility">{{entry.credibility}}</div>
	</li>
</ul>
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
		},
		{
		'key': 'device', 
		'values': ["smart-phone","touch-surface","smart-ring","smart-watch","prototype", "no-device"],
		'filterValues': [],
		'multipleSelection': true,
		},
		{
		'key': 'user', 
		'values': ["civilian","children","infantrymen","elderly","old"],
		'filterValues': [],
		'multipleSelection': true,
		},
		{
		'key': 'task', 
		'values': ["perform action", "scale", "next", "previous", "draw object", "rotate", "increase", "decrease", "deactivate", "activate", "ok", "cancel"],
		'filterValues': [],
		'multipleSelection': true,
		},
		{
		'key': 'type',
		'values': ["Pointing", "Semaphoric\nStatic", "Semaphoric\nDynamic", "Semaphoric\nStroke", "Pantomimic", "Iconic\nStatic", "Iconic\nDynamic", "Manipulation"],
		'filterValues': [],
		'multipleSelection': true,
		},
		{
		'key': 'form',
		'values': ["Static Gesture", "Dynamic Gesture"],
		'filterValues': [],
		'multipleSelection': true,
		},
		{
		'key': 'nature',
		'values': ["Deictic", "Iconic", "Miming", "Physical"],
		'filterValues': [],
		'multipleSelection': true,
		},
		{
		'key': 'symmetry',
		'values': ["Unilateral", "Bilateral-Symmetric", "Bilateral-Asymmetric"],
		'filterValues': [],
		'multipleSelection': true,
		},
		{
		'key': 'locale',
		'values': ["On-the-object", "In-the-air", "Mixed"],
		'filterValues': [],
		'multipleSelection': true,
		},
		{
		'key': 'year', 
		'values': ["2012","2014","2017","2018","2019","2020","2021","2022"],
		'filterValues': [],
		'multipleSelection': true,
		}
		
		/*{
		'key': 'Gesture type',
		'values': ["Poiting", "Semaphoric", "Pantomimic", "Iconic", "Manipulation"],
		'filterValues': [],
		'multipleSelection': false,
		'subfilters': []
		},*/
	]; 
	
	/*{
		'key': 'type',
		'values': ["Accessories", "Clothing", "Skin & Body"],
		'filterValues': [],
		'multipleSelection': false,
		'subfilters': [] // Subfilters only work with multipleSelection: false
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
				data: []			// The data this component works on
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

		},
		watch: {
			filteredData: {
				handler: function (value) {
					this.$emit("input", value);
				},
				immediate: true
			}
		},
		methods: {
			subFiltersForFilter(filter) {
				return subFilters.filter( f => f.parent == filter.key && filter.filterValues.length > 0 && f.parentValue == filter.filterValues)
			},
			isFilterActive: function(filter) {
				return this.activeFilters.includes(this.filters.indexOf(filter));
			},
			
			
		},
		computed: {
			filteredData: function () {
				// Collect all filterkeys, and their possible values
				let filterList = {};
				for (let index of this.activeFilters) {
					filterList[this.filters[index]['key']] = this.filters[index]['filterValues'];
				}
				return this.data.filter(useConditions(filterList));
			},
		},
	};
</script>

<style scoped>



#DataFilter {
	width:50%;
	margin-right:30%;
	margin-left:20%;
	margin-top:8%;
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


.active {
	border-color: #F00 ;
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
}
.user {
  padding: 10px;
  margin: 1% 0;
  border: 1px solid #ddd;
  border-radius: 3px;
  width: 30%;
  text-align: left;
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
	#DataFilter{
		width: 90%;
		margin-top: 15%;
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
}

@media (max-width: 300px) {
	#DataFilter{
		width: 90%;
		margin-top: 40%;
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

	.user{
		width : 100%;
	}
}


</style>
