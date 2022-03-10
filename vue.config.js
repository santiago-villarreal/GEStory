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
    license:{
      entry: "./src/pages/license/license.js",
      template: "./src/pages/license/license.html",
      filename: "license.html",
      title:"License"
  },
  suggest:{
    entry: "./src/pages/suggest/suggest.js",
    template: "./src/pages/suggest/suggest.html",
    filename: "suggest.html",
    title:"Suggest a GES"
  },
  adminGEStory:{
    entry: "./src/pages/adminGEStory/adminGEStory.js",
    template: "./src/pages/adminGEStory/adminGEStory.html",
    filename: "adminGEStory.html",
    title:"Manage GEStory"
  }

  },
  devServer: {
    disableHostCheck: true
  }
};