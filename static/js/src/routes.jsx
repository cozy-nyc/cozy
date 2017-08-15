import React from "react";
import {IndexRoute, Route} from "react-router";

import Home from "./components/home";
import About from "./components/about";
import Item from "./components/itemdetail";
import Listing from "./components/listingdetail";
import Login from './components/login'

export default (
    <Route path="/">
        <IndexRoute component={Home} />
        <Route path="about" component={About} />
        <Route path="s/:itemid/jawns" component={Item}/>
        <Route path="s/:itemid/jawns/:listingid" component={Listing}/>
        <Route path="login" component={Login}/>
     </Route>
 );
