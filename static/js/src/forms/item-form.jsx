import React, {Component} from 'react';
import {connect} from 'react-redux';
import { Field, reduxForm } from 'redux-form';
import Autocomplete from 'react-autocomplete';
import { get } from '../actions/items/get'

const renderInput = field => (
    <div>
      <input className="form-control" {...field.input}/>
      {field.touched && field.error && <div className="error">{field.error}</div>}
   </div>
);


@connect((store, state) => {
   return {
   items: state.items,
   listings: store.listings.listings,
   };
})
class ItemForm extends Component {
   state = {
      item_id: null,
      item_name: '',
      item_category: '',
      item_subCategory: '',
      items: [],
      categories: [],
      subCategories: [],
       error: null,
       success: true,
      itemSelected: false
   };

   formSubmit = data => {
       var success = this.state.success;
       var selected = this.state.itemSelected;
      //  console.log(success);
       this.props.success(success);
       if(selected){
         //  get(value, (suggestions) => {
         //     const {dispatch} = this.state;
         //  });
         console.log('nut')
       }
      else {
         // const {dispatch} = this.state;
         console.log('jawn');
      }
   };

   onChange(id, newValue) {
    console.log(`${id} changed to ${newValue}`);
  }

  autofill(item) {
     this.setState ({
       item_id: item.id,
       item_category: item.category,
       item_subCategory: item.subCategory,
       itemSelected: true
    });
 }


   render() {
       const {handleSubmit} = this.props;

       return (
            <form onSubmit={handleSubmit(this.formSubmit)}>
               <div>
               <label>Name</label>
               <div>
               <Autocomplete
                   inputProps={{ id: 'item-autocomplete' }}
                   value={this.state.item_name}
                   items={this.state.items}
                   getItemValue={(item) => item.name}
                   onSelect={(item_name, item) => {
                     // set the menu to only the selected item
                     this.setState({ item_name, items: [ item ] })
                     {this.autofill(item)}
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
                     <div
                       key={item.id}
                     >{item.name}</div>
                   )}
                 />
           </div>
              </div>

              <div>
              <label>Catagory</label>
              <div>
                 <Autocomplete
                     inputProps={{ id: 'category-autocomplete' }}
                     value={this.state.item_category}
                     items={this.state.categories}
                     getItemValue={(category) => category.name}
                     onChange={(event, value) => {
                       this.setState({ item_category: value })
                       clearTimeout(this.requestTimer)
                     //   get(value, (suggestions) => {
                     //     this.setState({ items: suggestions })
                     //  })
                     }}
                     renderItem={(category, isHighlighted) => (
                       <div
                         key={category.id}
                       >{category.name}</div>
                     )}
                   />

             </div>
          </div>

                <div>
               <label>SubCategory</label>
               <div>
                   <Autocomplete
                       inputProps={{ id: 'subcategory-autocomplete' }}
                       value={this.state.item_subCategory}
                       items={this.state.subCategories}
                       getItemValue={(subcategory) => subcategory.name}
                       onChange={(event, value) => {
                         this.setState({ item_subCategory: value })
                         clearTimeout(this.requestTimer)
                       //   get(value, (suggestions) => {
                       //     this.setState({ items: suggestions })
                       //  })
                       }}
                       renderItem={(subcategory, isHighlighted) => (
                         <div
                           key={subcategory.id}
                         >{subcategory.name}</div>
                       )}
                    />
              </div>
           </div>
           <div>
                 <button type="submit">Next</button>
          </div>
            </form>
       );
   }
}

ItemForm = reduxForm({
  form: 'ItemForm'
})(ItemForm)

export default ItemForm;
