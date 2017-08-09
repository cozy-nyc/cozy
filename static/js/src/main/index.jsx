import React from 'react';
import ReactDOM from 'react-dom';
import { AppContainer } from 'react-hot-loader';
import HelloWorld from './components/hello-world';
import axios from 'axios'
import api from '../utilities/api'



/*import ItemList from './api/items',
axios.get('/api')
  .then(function(response){
    console.log(response);
  })
  .catch(function(error) {
    console.log(error);
  });
*/

//
// api.get('/api/items/')
//   .then(function(response){
//     console.log(response);
//   })
//   .catch(function(error) {
//     console.log(error);
//   });


  api.post('/api-token-auth/',{
    username: 'test',
    password: 'yeet12345'
    })
    .then(function(response){
      csrftoken = response.data
      console.log(response);
    })
    .catch(function(error) {
      console.log(error);
    });



ReactDOM.render(
  <AppContainer>
    <HelloWorld />
    <navbar />
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
