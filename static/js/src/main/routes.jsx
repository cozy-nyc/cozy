import React from "react";
import {IndexRoute, Route} from "react-router";

import Home from "./containers/home";
import Listing from "./containers/listing";

export default (
    <Route path="/">
        <IndexRoute component={Home}/>
     </Route>
 );
