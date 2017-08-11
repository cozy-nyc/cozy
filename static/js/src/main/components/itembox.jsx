import React from 'react';

const ItemBox= (props) => {
  return (
    <a href="">
      <h1>{props.name}</h1>
      <h1>{props.avgprice}</h1>
      <h1>{props.lowestprice}</h1>
    </a>
  );
};

export default ItemBox;
