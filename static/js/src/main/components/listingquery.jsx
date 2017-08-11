import React from 'react';
import { connect } from 'react-redux';

import { fetchListings } from '../actions/listing-actions';

import Navbar from './navbar';
import Listing from './listing';

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

      const mappedListings = listings.map(listing =><Listing price={ listing.price } size={ listing.size }/>)

      return (
         <table>
            <td>{mappedListings}</td>
         </table>

      );
   }
}
