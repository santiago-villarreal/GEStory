<template>
  <div id="license">
    <div id="header"><img src="img/UCL_logo.png" height="40" alt=""><img src="img/GEStoryLogo.png" height="40" alt=""><img src="img/LouRIM.png" height="40" alt=""></div>
    
      <h1>About</h1>
      <div id="contentLic">
      <h2>GEStory: An Atlas for User-Defined Gestures as an Interactive Design Space </h2>
        <p> How can we provide designers and developers with some support to identify the most appropriate gestures for gestural user interfaces depending on their context of use? To address this research question, we develop GEStory, an on-line atlas of gestures resulting from gesture elicitation studies with four main functionalities: (1) search for user-defined gestures identified in such studies by querying its features in an interactive design space, (2) show the preferred gestures and their characteristics for a given action (represented through a referent) with a given device  in an environment and/or carried out with various body parts, (3) compare the existing studies and (4) suggest adding new studies. To feed GEStory, we have conducted two systematic literature reviews: a macroscopic analysis of 216 papers on their metadata, such as authors, definitions, year of publication, type of publication, participants, referents, parts of the body (finger, hand, wrist, arm, head, leg, foot and Whole body), number of proposed gestures; a microscopic analysis of 267 papers analyzing and classifying the referents, the  final gestures coming out the consensus set, their representation and characterization. We also propose an assessment of credibility of these studies as a measure for categorizing their strength of impact. GEStory acts as an interactive design space for gestural interaction to inform researchers and practitioners on existing preferred gestures in different contexts of use, and enable the identification of gaps and opportunities for new studies.</p>
       <h2>FAQ</h2>
      <h2>License MIT </h2>
    <p>GEStory and Gelicit: Online Support Platforms for Designers and Developers to identify the most appropriate gestures for gestural user interfaces, doctoral thesis of Santiago Villarreal-Narvaez, <a href = "mailto: santiago.villarreal@uclouvain.be" target="_blank">santiago.villarreal@uclouvain.be</a> under the supervision of Pr. Jean Vanderdonckt and PR. Jorge Perez-Medina, LouRIM, UCLouvain</p>
    <p>We appreciate the collaboration of:</p>
    <ul>
      <li type="square">Anthony Doeraene</li>
      <li type="square">Lorenzo D'intino Salgado</li>
      <li type="square">Loïc Laridant</li>
      <li type="square">Ling Leung</li>
      <li type="square">Quentin Massinon</li>
      <li type="square">Pierre Marcipont</li>
      <li type="square">Darius Muntean</li>
      <li type="square">Yseult Poncelet</li>
    </ul>

    <p>This version is part of a prototype, This work is based on the tool:</p>

<p style="margin: 0px 100px 0px 100px;">Florian Heller, Kashyap Todi, and Kris Luyten. An Interactive Design Space for Wearable Displays. In <i>MobileHCI&nbsp;’21: Proceedings of the the 23rd International Conference on Human-Computer Interaction with Mobile Devices and Services</i>, MobileHCI&nbsp;’21, 2021, <a href="http://dx.doi.org/10.1145/3447526.347203">10.1145/3447526.347203</a>. </p>

<p><a href="javascript:history.back()"> Return</a></p>
    </div>
  </div>
</template>



<style>
#license {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #022d55;
  width:100%;
}
a {
  text-decoration: none;
  color: #D99100;
}
p{
  width: 95%; 
  text-align: justify;
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
}
h1{
  position: fixed;
  left: 2%;
  top: 0px;
}
#contentLic {
  position: fixed;
  left: 2%;
  top: 10%;
  width: 98%;
  overflow-x: hidden;
  overflow-y: auto;
	max-height: 90%;

}
</style>
