import React from 'react';
import ReactDOM from 'react-dom';
import { AppContainer } from 'react-hot-loader';
import HelloWorld from './components/hello-world';
import axios from 'axios'
//import ItemList from './api/items',
//import api from '../utilities/api'
axios.get('/api/items/1')
  .then(function(response){
    console.log(response);
  })
  .catch(function(error) {
    console.log(error);
  });

ReactDOM.render(
  <AppContainer>
    <HelloWorld />
  </AppContainer>,
  document.getElementById('react-root')
);

if (module.hot) {
  module.hot.accept('./components/hello-world', () => {
    const HelloWorld = require('./components/hello-world').default;
    ReactDOM.render(
      <AppContainer>
        <HelloWorld />
      </AppContainer>,
      document.getElementById('react-root')
    );
  });
}
