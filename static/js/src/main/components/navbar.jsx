import React from 'react';

const navbar = () => {
  return (
    <div id="navbar">
      <a class="navbar-brand" href="">exchange</a>
      <input type="text" placeholder="Search..." class="form-control"></input>
      <span>
        <a href="">Sell</a> | <a href="">Account</a>
      </span>
    </div>
  );
};

export default navbar;
