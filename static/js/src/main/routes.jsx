import React from "react";
import {IndexRoute, Route} from "react-router";

import HomePage from "./containers/home";

export default (
    <Route path="/">
        <IndexRoute component={HomePage}/>
     </Route>
 );
