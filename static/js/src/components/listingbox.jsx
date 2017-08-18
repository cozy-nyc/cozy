import React from 'react';
import { Link } from 'react-router'

const ListingBox= (props) => {

   var itemid = parseInt(props.itemid);
   var listingurl = '/s/'+itemid+'/jawns';

   return (
      <Link to={`/s/${props.itemid}/jawns/${props.listingid}`} activeClassName="active">
         <div>
            <h1>{ props.name }</h1>
            <h1>${ props.price }</h1>
            <h1>Size: { props.size }</h1>
         </div>
      </Link>
  );
};

export default ListingBox;
