import React from 'react';
import { connect } from 'react-redux';

import { fetchListings } from '../actions/listings/actions';

import ListingBox from './listingbox';

@connect((store) => {
   return {
      listings: store.listings.listings,
      listingsFetched: store.listings.fetched,
      items: store.items.items
   };
})
export default class ListingQuery extends React.Component {

   componentWillMount() {
      this.props.dispatch(fetchListings())
   }

   render(){

      const { item, listings } = this.props;

      const mappedListings = listings.map(listing => <li key={ listing.id }><ListingBox
         name={ listing.item_name }
         itemid={ listing.item }
         listingid={ listing.id }
         price={ listing.price }
         size={ listing.size }
         /></li>)

      return (
         <ul>
            {mappedListings}
         </ul>

      );
   }
}
