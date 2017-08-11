import React from 'react';

const ListingBox= (props) => {
  return (
    <a href=''>
      <h1>{props.name}</h1>
      <h1>{props.price}</h1>
      <h1>{props.size}</h1>
    </a>
  );
};

export default ListingBox;
