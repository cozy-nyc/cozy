import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import {browserHistory, Router} from "react-router";
import Cookies from 'universal-cookie';
import { AUTH_USER } from './actions/auth/types';

import store from './store';
import routes from './routes';


// This is the place where we can load elements from a cookie to be used in our app

// Django CRSF Token is stored in a cookie

const cookies = new Cookies();

const token = cookies.get('token');

if (token) {
  store.dispatch({ type: AUTH_USER });
}

ReactDOM.render(
   <Provider store={store}>
      <Router history={browserHistory} routes={routes}/>
   </Provider>,
  document.getElementById('react-root')
);
