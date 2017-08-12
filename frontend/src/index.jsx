import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import {browserHistory, Router} from "react-router";

import store from './store';
import routes from './routes';
import Navbar from './components/navbar';
import Listings from './components/listingquery';



ReactDOM.render(
   <Provider store={store}>
      <Router history={browserHistory} routes={routes}/>
   </Provider>,
  document.getElementById('react-root')
);
