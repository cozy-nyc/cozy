import React, {Component} from 'react';
import {connect} from 'react-redux';
import Autocomplete from 'react-autocomplete';
import { get } from '../actions/items/get'
import { Link } from 'react-router'



@connect((store, state) => {
   return {
   items: state.items,
   listings: store.listings.listings,
   };
})
class SearchBar extends Component {
   state = {
      item_id: null,
      item_name: '',
      items: [],
   };


   render(){
     return (
        <Autocomplete
            inputProps={{ id: 'item-autocomplete' }}
            value={this.state.item_name}
            items={this.state.items}
            getItemValue={(item) => item.name}
            onSelect={(item_name, item) => {
              // set the menu to only the selected item
              this.setState({ item_name, items: [ item ] })
              // or you could reset it to a default list again
              // this.setState({ unitedStates: getStates() })
            }}
            onChange={(event, value) => {
              this.setState({ item_name: value })
              clearTimeout(this.requestTimer)
              get(value, (suggestions) => {
                this.setState({ items: suggestions })
             })
            }}
            renderItem={(item, isHighlighted) => (
               <Link to={`/s/${item.id}/jawn/`} activeClassName="active">
                 <div key={item.id}>{item.name}</div>
               </Link>
            )}
         />
      );
   }
};

export default SearchBar;
