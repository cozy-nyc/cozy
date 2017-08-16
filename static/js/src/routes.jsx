import React from "react";
import {IndexRoute, Route} from "react-router";

import App from "./containers/app";
import Dashboard from "./containers/dashboard";
import Home from "./components/home"
import About from "./components/about";
import Item from "./components/itemdetail";
import Listing from "./components/listingdetail";
import Error404 from './components/404-error'
import RequireAuth from './components/auth/require-auth'
import Register from './components/auth/register';
import Login from './components/auth/login';
import Sell from './containers/sell';

export default (
   <Route path="/" component={App}>
       <IndexRoute component={Home} />
       // Static Pages
       <Route path="about" component={About} />

       // Shop Pages
       <Route path="s/:itemid/jawns" component={Item}/>
       <Route path="s/:itemid/jawns/:listingid" component={Listing}/>
       <Route path="sell" component={Sell}/>

       // Auth Pages
       <Route path="login" component={Login}/>
       <Route path="register" component={Register}/>

       //User Pages
       <Route path="dashboard" component={RequireAuth(Dashboard)}/>

       //   Error pages
       <Route path='*'component={Error404} />
    </Route>
 );
