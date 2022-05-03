module.exports =
{
	transpileDependencies: true,
	devServer: {
		proxy: {
			'backend': {
				target: "http://localhost:10005",
				//target: 'http://hephaistos.nathanaelderousseaux.fr:3306',
				changeOrigin: true,
				pathRewrite: {
					"^/backend": ""
				}
			}
		}
	},

	publicPath: process.env.NODE_ENV === 'production' ? './' : '/',

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
