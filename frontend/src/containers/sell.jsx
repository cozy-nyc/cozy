import React, {Component} from 'react';
import {connect} from 'react-redux';
import ItemForm from '../forms/item-form';
import ListingForm from '../forms/listing-form';


class Sell extends Component {
   constructor(props){
    super(props);
    this.state = {
        isItemReady: false
    };
    this.handleItemFormUpdate = this.handleItemFormUpdate.bind(this);
}

   handleItemFormUpdate(itemValues) {
      this.setState({isItemReady: itemValues});
      console.log(this.state.isItemReady);
   }

   render() {
      return (
         <div>
               <ItemForm success={this.handleItemFormUpdate}/>
               <br />
               { this.state.isItemReady && <ListingForm />}
         </div>
       );
   }
}

export default Sell;
