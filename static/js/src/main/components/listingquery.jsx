import React from 'react';
import { connect } from 'react-redux';

import { fetchListings } from '../actions/listing-actions';

import ListingBox from './listingbox';

@connect((store) => {
   return {
      listings: store.listings.listings,
      listingFetched: store.listings.fetched,
      items: store.items.item
   };
})
export default class ListingQuery extends React.Component {

   componentWillMount() {
      this.props.dispatch(fetchListings())
   }

   render(){

      const { item, listings } = this.props;

      const mappedListings = listings.map(listing => <li><ListingBox price={ listing.price } size={ listing.size }/></li>)

      return (
         <ul>
            {mappedListings}
         </ul>

      );
   }
}
