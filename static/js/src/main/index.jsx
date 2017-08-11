import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import store from './store';
import Home from './containers/home';


ReactDOM.render(
  <Provider store={store}>
     <Home />
  </Provider>,
  document.getElementById('react-root')
);
