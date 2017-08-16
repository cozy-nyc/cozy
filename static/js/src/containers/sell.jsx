import React, {Component} from 'react';
import {connect} from 'react-redux';
import { Field, reduxForm } from 'redux-form';

const renderInput = field => (
    <div>
      <input className="form-control" {...field.input}/>
      {field.touched && field.error && <div className="error">{field.error}</div>}
    </div>
);


@connect((store, state) => {
   return {
   items: store.items.items,
   listings: store.listings.listings,
   };
})
class Sell extends Component {
   state = {
       error: null,
       success: null
   };

   formSubmit = data => {
       const {dispatch} = this.props;
       console.log(data)
   };

   render() {
       const {handleSubmit} = this.props;
       return (
            <form onSubmit={handleSubmit(this.formSubmit)}>
               <Field component={renderInput} label="Item Name" name="item_name" type="text"/>
               <Field component={renderInput} label="Category" name="item_category" type="text"/>
               <Field component={renderInput} label="Sub Catagory" name="item_sub_category" type="text"/>
               <button className="btn btn-primary" type="submit">Submit</button>
            </form>
       );
   }
}

Sell = reduxForm({
  form: 'sell'
})(Sell)

export default Sell;
