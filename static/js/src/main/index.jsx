import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import {hashHistory, Router} from "react-router"

import store from './store';
import routes from './routes';

import createBrowserHistory from 'history/createBrowserHistory'

const newHistory = createBrowserHistory();

ReactDOM.render(
   <Provider store={store}>
      <Router history={newHistory} routes={routes}/>
   </Provider>,
  document.getElementById('react-root')
);
