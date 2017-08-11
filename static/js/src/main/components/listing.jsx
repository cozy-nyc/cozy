import React from 'react';

const Listing= (props) => {
  return (
    <div>
      <h1>{props.price}</h1>
      <h1>{props.size}</h1>
    </div>
  );
};

export default Listing;
