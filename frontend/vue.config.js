const { defineConfig } = require('@vue/cli-service')
module.exports = {

  publicPath: process.env.NODE_ENV === 'production' ? '/static/dist/' : 'http://localhost:8080',

  outputDir: '../static/dist',
  indexPath: '../../templates/base-vue.html',

  devServer: {
    proxy: {
      "^/api/": {
        target: "http://127.0.0.1:8000/api/",
        ws: false,
      },
    },
    hot: 'only',
    headers: {"Access-Control-Allow-Origin": "*"},
    devMiddleware: {
      writeToDisk: true
    }
  }
}
