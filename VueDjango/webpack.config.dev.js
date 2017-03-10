var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    entry: {
        index: './modules/index/app/index/index.js'
    },
    output: {
        path: path.resolve('./static/bundles/'),
        publicPath: './static/bundles/',
        filename: "[name]-[hash].js"
    },
    module: {
        loaders: [
            {
                test: /\.vue$/,
                loader: 'vue'
            },
            {
                test: /\.js$/,
                loader: "babel",
                exclude: /node_modules/
            },
            {
                test: /\.json$/,
                loader: 'json'
              },
              {
        test: /\.html$/,
        loader: 'vue-html'
      },
            {
                test:/\.css$/,
                loader: "style!css"
            },
            {
                test:/\.(png|jpg|gif|svg)$/,
                loader: "url?limit=50000"
            }
        ]
    },
    plugins: [
        new BundleTracker({filename: './webpack-stats.json'})
    ],
    devServer: {
        historyApiFallback: true,
        noInfo: true
    },
    devtool: '#eval-source-map'
}