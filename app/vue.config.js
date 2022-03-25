
module.exports = {
  /*publicPath: process.env.RENDER_PATH == undefined
    ? '/GEStory/'
    : '/',
  // outputDir: "docs"*/

  pages:{
    index:{
        entry: "./src/main.js",
        template: "./public/index.html",
        filename: "index.html",
        title:"GEStory"
    },
    about:{
      entry: "./src/pages/about/about.js",
      template: "./src/pages/about/about.html",
      filename: "about.html",
      title:"About"
  },
  suggest:{
    entry: "./src/pages/adminGEStory/adminGEStory.js",
    template: "./src/pages/adminGEStory/adminGEStory.html",
    filename: "suggest.html",
    title:"SuggestGES",
  },
  adminGEStory:{
    entry: "./src/pages/adminGEStory/adminGEStory.js",
    template: "./src/pages/adminGEStory/adminGEStory.html",
    filename: "adminGEStory.html",
    title:"Manage GEStory"
  }

  }


};