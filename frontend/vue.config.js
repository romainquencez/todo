module.exports = {
  css: {
    loaderOptions: {
      sass: {
        data: `@import "@/scss/style.scss";`
      }
    }
  },
  devServer: {
    proxy: {
      '/api': {
        target: 'http://backend:8080',
        changeOrigin: true
      }
    },
    watchOptions: process.env.OS === 'windows'
      ? {
          poll: true,
          ignored: /node_modules/
        }
      : {
          poll: false
        }
  }
};
