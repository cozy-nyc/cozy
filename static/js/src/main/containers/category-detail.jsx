import React, {Component} from 'react';
import { connect } from 'react-redux';

class CategoryDetail extends Component {
   render() {
      if(!this.props.category ) {
         return (<h2>Select a Category</h2>);
      }
      return (
         <div>
            <h1>{ this.props.category.name }</h1>
         </div>
      );
   }
}

function mapStateToProps(state) {

  return {
    category: state.activeCatergory
  };
}

export default connect(mapStateToProps)(CategoryDetail);
