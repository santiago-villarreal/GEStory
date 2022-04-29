<template>
  <div id="license">
    <div id="header"><img src="img/UCL_logo.png" height="40" alt=""><img src="img/GEStoryLogo.png" height="40" alt=""><img src="img/LouRIM.png" height="40" alt=""></div>
    <div id="contentLic">
      <h1>License MIT </h1>
    <p>GEStory and Gelicit: Online Support Platforms for Designers and Developers to identify the most appropriate gestures for gestural user interfaces, doctoral thesis of Santiago Villarreal-Narvaez, <a href = "mailto: santiago.villarreal@uclouvain.be">santiago.villarreal@uclouvain.be</a> under the supervision of Pr. Jean Vanderdonckt and PR. Jorge Perez-Medina, LouRIM, UCLouvain</p>
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

<p class="ref">Florian Heller, Kashyap Todi, and Kris Luyten. An Interactive Design Space for Wearable Displays. In <i>MobileHCI&nbsp;’21: Proceedings of the the 23rd International Conference on Human-Computer Interaction with Mobile Devices and Services</i>, MobileHCI&nbsp;’21, 2021, <a href="http://dx.doi.org/10.1145/3447526.347203">10.1145/3447526.347203</a>. </p>

<p><a href="javascript:history.back()"> <img src="../../../public/img/bx-undo.svg" width="48px"></a></p>
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
#header {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  padding: 5px;
  background-color:  #c7b062;
  color: white;
  text-align: right;
  display: flex;
  align-items: center;
}
#contentLic {
  position: fixed;
  left: 15px;
  width: 90%;
  top:5%
}

.ref{
  margin: 0px 100px 0px 100px;
}

@media (max-width: 600px) {
  #contentLic {
    position: relative;
    top: 80px;
    z-index: -1;
  }

  .ref{
    margin: 0px 10px;
  }

	#header {
    justify-content: space-between;
    flex-wrap: wrap;
  }
}
</style>
