import React from 'react';

const Navbar = () => (

    <div id="navbar">
      <a className="navbar-brand" href="">exchange</a>
      <input type="text" placeholder="Search..." className="form-control"></input>
      <span>
        <a href="">Sell</a> | <a href="">Account</a>
      </span>
    </div>

);

export default Navbar;
