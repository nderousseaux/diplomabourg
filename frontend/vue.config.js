/*
module.exports  =
{
	publicPath: process.env.NODE_ENV  ===  'production'  ?  './'  :  '/'
}
*/

module.exports = {
  transpileDependencies: true,
  devServer: {
    proxy: {
      'backend': {
        target: 'http://localhost:10005',
        changeOrigin: true,
        pathRewrite: {
          '^/backend': ''
        }
      },
    }
  }
}
