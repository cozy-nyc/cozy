import React from 'react';
import { IndexLink } from 'react-router'

import SearchBar from './searchbar';

const Navbar = () => (
    <div id="navbar">
      <IndexLink to="/">exchange</IndexLink>
      <SearchBar />
      <span>
        <a href="">Sell</a> | <a href="">Account</a>
      </span>
    </div>
);

export default Navbar;
