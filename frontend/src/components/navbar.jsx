import React, { Component } from 'react';
import { IndexLink, Link } from 'react-router'
import { connect } from 'react-redux';

import SearchBar from './searchbar';

@connect((state) => ({
   isAuth: state.auth.authenticated
}))
class Navbar extends Component {

   render(){
      const { isAuth } = this.props;

      return (
      <div id="navbar">
         <IndexLink to="/">exchange</IndexLink>
         <SearchBar />
         <span>
         <Link to={`/sell`}>Sell</Link>|
            { !isAuth && <Link to={`/login`}>Login</Link> }
            { isAuth && <Link to={`/dashboard`}>Account</Link> }
         </span>
      </div>
      )
   }
}

export default Navbar;
