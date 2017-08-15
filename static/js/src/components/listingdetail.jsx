import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { getListing } from '../actions/listing-actions';
import { connect } from 'react-redux';

import Navbar from './navbar';
@connect((store) => ({
   listing: store.listings.activelisting,
}))
class Listing extends Component {
   componentDidMount() {
      const {dispatch, params: {listingid}} = this.props;
      dispatch(getListing(listingid));
   }

   render(){
      const {listing} = this.props;
      if(!listing) return null;
      return (
         <div>
            <Navbar />
            <h1>{ listing.item_name }</h1>
            <h1>${ listing.price } Size { listing.size }</h1>
            <h1>{ listing.location }</h1>
            <h1>{ listing.description }</h1>
         </div>
      );
   }
};

export default Listing;
