var webpack = require('webpack');
var merge = require('webpack-merge')
var config = require('./webpack.config.dev.js');

module.exports = merge(config,{
    plugins: [
        new webpack.optimize.UglifyJsPlugin({
          compress: {
            warnings: false
          },
          mangle: false
        })
    ]
})