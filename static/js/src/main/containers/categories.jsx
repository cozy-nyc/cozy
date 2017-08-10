import React, { Component } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { selectCategory } from '../actions/quary';

class Categories extends Component {

  createListItems(){
    return this.props.categories.map((category) => {
      return (
        <li
          key={category.id}
          onClick={() => this.props.selectCategory(category)}
        >
          {category.name}
        </li>
      );
    });
  }

  render() {
    return (
      <ul>
        {this.createListItems()}
      </ul>
    );
  }

}

function mapStateToProps(state) {

  return {
    categories: state.categories
  };
}

function matchDispatchToProps(dispatch){
  return bindActionCreators({selectCategory: selectCategory}, dispatch)
}

export default connect(mapStateToProps, matchDispatchToProps)(Categories);
