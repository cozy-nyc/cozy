
module.exports = {

  module: {
    loaders: [{
      test: /\.(js|jsx)$/,
      exclude: /node_modules/,
      loader: 'babel-loader',
      query: {
         babelrc: false,
        presets: ['es2015', 'stage-2', 'react'],
        plugins: ['transform-decorators-legacy', 'react-hot-loader/babel']
      }
    }, {
      test: /\.css$/,
      loader: 'style-loader!css-loader'
    }]
  },

  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.jsx']
  }
};
