(function(e){function t(t){for(var o,s,i=t[0],l=t[1],u=t[2],m=0,p=[];m<i.length;m++)s=i[m],Object.prototype.hasOwnProperty.call(a,s)&&a[s]&&p.push(a[s][0]),a[s]=0;for(o in l)Object.prototype.hasOwnProperty.call(l,o)&&(e[o]=l[o]);c&&c(t);while(p.length)p.shift()();return n.push.apply(n,u||[]),r()}function r(){for(var e,t=0;t<n.length;t++){for(var r=n[t],o=!0,i=1;i<r.length;i++){var l=r[i];0!==a[l]&&(o=!1)}o&&(n.splice(t--,1),e=s(s.s=r[0]))}return e}var o={},a={suggest:0},n=[];function s(t){if(o[t])return o[t].exports;var r=o[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,s),r.l=!0,r.exports}s.m=e,s.c=o,s.d=function(e,t,r){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(s.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)s.d(r,o,function(t){return e[t]}.bind(null,o));return r},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=t,i=i.slice();for(var u=0;u<i.length;u++)t(i[u]);var c=l;n.push([2,"chunk-vendors"]),r()})({"08dc":function(e,t,r){"use strict";r("7aa9")},2:function(e,t,r){e.exports=r("5dd6")},"5dd6":function(e,t,r){"use strict";r.r(t);r("e260"),r("e6cf"),r("cca6"),r("a79d");var o=r("2b0e"),a=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{attrs:{id:"suggest"}},[e._m(0),r("div",{attrs:{id:"contentSug"}},[r("h1",[e._v("Suggest a GES ")]),r("p",[e._v("Thank you for collaborating with us")]),r("FormSuggest"),e._m(1)],1)])},n=[function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{attrs:{id:"header"}},[r("img",{attrs:{src:"img/UCL_logo.png",height:"40",alt:""}}),r("img",{attrs:{src:"img/GEStoryLogo.png",height:"40",alt:""}}),r("img",{attrs:{src:"img/LouRIM.png",height:"40",alt:""}})])},function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("p",[r("a",{attrs:{href:"javascript:history.back()"}},[e._v(" Return")])])}],s=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{attrs:{id:"formSuggest"}},[e.sentSuggestion?e._e():r("form",{staticClass:"form",attrs:{id:"fSuggestion",action:""},on:{submit:function(t){return t.preventDefault(),e.GESinfo.apply(null,arguments)}}},[r("h2",[e._v("About you")]),r("label",{staticClass:"form-label",attrs:{for:"#personName"}},[e._v("Your Name")]),r("input",{directives:[{name:"model",rawName:"v-model",value:e.personName,expression:"personName"}],staticClass:"form-input",attrs:{type:"text",id:"personName",required:"",placeholder:"Santiago Villarreal-Narvaez"},domProps:{value:e.personName},on:{input:function(t){t.target.composing||(e.personName=t.target.value)}}}),r("label",{staticClass:"form-label",attrs:{for:"#email"}},[e._v("Email")]),r("input",{directives:[{name:"model",rawName:"v-model",value:e.email,expression:"email"}],staticClass:"form-input",attrs:{type:"email",id:"email",placeholder:"santiago.villarreal@uclouvain.be"},domProps:{value:e.email},on:{input:function(t){t.target.composing||(e.email=t.target.value)}}}),r("h2",[e._v("About GES")]),r("label",{staticClass:"form-label",attrs:{for:"#GESName"}},[e._v("GES Name")]),r("input",{directives:[{name:"model",rawName:"v-model",value:e.GESName,expression:"GESName"}],staticClass:"form-input",attrs:{type:"text",id:"GESName",required:"",placeholder:"Title of GES"},domProps:{value:e.GESName},on:{input:function(t){t.target.composing||(e.GESName=t.target.value)}}}),r("label",{staticClass:"form-label",attrs:{for:"#authors"}},[e._v("Authors")]),r("input",{directives:[{name:"model",rawName:"v-model",value:e.authors,expression:"authors"}],staticClass:"form-input",attrs:{type:"text",id:"authors",required:"",placeholder:"Leng, Hoo Yong and Norowi, Noris Mohd and Jantan, Azrul Hazri"},domProps:{value:e.authors},on:{input:function(t){t.target.composing||(e.authors=t.target.value)}}}),r("label",{staticClass:"form-label",attrs:{for:"#urlGES"}},[e._v("URL")]),r("input",{directives:[{name:"model",rawName:"v-model",value:e.urlGES,expression:"urlGES"}],staticClass:"form-input",attrs:{type:"text",id:"urlGES",required:"",placeholder:"http://doi.acm.org/10.1145/2702613.2702971"},domProps:{value:e.urlGES},on:{input:function(t){t.target.composing||(e.urlGES=t.target.value)}}}),r("input",{staticClass:"form-submit",attrs:{type:"submit",value:"Send suggestion"}})]),e.sentSuggestion?r("p",[e._v("Your suggestion has been sent, thank you. "),r("a",{on:{"~click":function(t){return e.otherSuggestion.apply(null,arguments)}}},[e._v("Send another")])]):e._e()])},i=[],l={name:"FormSuggest",data:function(){return{personName:"",email:"",GESName:"",authors:"",urlGES:"",sentSuggestion:!1}},methods:{GESinfo:function(){console.log(this.personName),console.log(this.email),console.log(this.GESName),console.log(this.authors),console.log(this.urlGES),this.sentSuggestion=!0},otherSuggestion:function(){this.personName="",this.email="",this.GESName="",this.authors="",this.urlGES="",this.sentSuggestion=!1}}},u=l,c=(r("5f95"),r("2877")),m=Object(c["a"])(u,s,i,!1,null,null,null),p=m.exports,g={name:"FormSuggestPage",components:{FormSuggest:p}},f=g,d=(r("08dc"),Object(c["a"])(f,a,n,!1,null,null,null)),h=d.exports;o["a"].config.productionTip=!1,new o["a"]({render:function(e){return e(h)}}).$mount("#suggest")},"5f95":function(e,t,r){"use strict";r("fb1a")},"7aa9":function(e,t,r){},fb1a:function(e,t,r){}});
//# sourceMappingURL=suggest.f0794ec1.js.map