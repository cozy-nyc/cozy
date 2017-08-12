import React from 'react';

import SearchBar from './searchbar';

const Navbar = () => (
    <div id="navbar">
      <a className="navbar-brand" href="">exchange</a>
      <SearchBar />
      <span>
        <a href="">Sell</a> | <a href="">Account</a>
      </span>
    </div>
);

export default Navbar;
