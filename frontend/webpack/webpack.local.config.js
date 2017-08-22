var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');
var webpack = require('webpack');
var config = require('./webpack.base.config.js');

config.entry = './src/index';

config.devtool = 'inline-sourcemap';
config.output = {
  path: path.join(__dirname, '../dist'),
  filename: 'js/bundle.min.js',
};

config.plugins = [
  new webpack.DefinePlugin({
    'process.env': {
      NODE_ENV: JSON.stringify('development'),
      API_ROOT: JSON.stringify('http://0.0.0.0:8000/'),
    }
  })
];


config.devServer = {
  inline: true,
  contentBase: './dist',
  port: 3000,
  host: '0.0.0.0',
};

module.exports = config;
