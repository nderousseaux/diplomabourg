module.exports = 
{
	transpileDependencies: true,
	devServer: {
		proxy: {
			'dev_url': {
				target: "http://localhost:10005",
				changeOrigin: true,
				pathRewrite: {
					"^/dev_url": ""
				}
			}
		}
	},

	// publicPath: process.env.NODE_ENV === 'production' ? './' : '/',

	pwa:
	{
		name: "Diplomabourg",
		themeColor: "#040004",
		manifestOptions:
		{
			background_color: "#ffff",
			start_url: ".",
			display: "standalone"

		},
		appleMobileWebAppCapable: "yes",
		appleMobileWebAppStatusBarStyle: "black",
		iconPaths: {
			faviconSVG: null,
			favicon32: "img/icons/favicon-32x32.png",
			favicon16: "img/icons/favicon-16x16.png",
			appleTouchIcon: "img/icons/apple-touch-icon-152x152.png",
			maskIcon: null,
			msTileImage: "img/icons/msapplication-icon-144x144.png"
		}
	},
	pluginOptions:
	{
		electronBuilder:
		{
			customFileProtocol: './'
		}
	}
}
