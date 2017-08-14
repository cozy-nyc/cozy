import { combineReducers } from 'redux';

import CategoryReducer from './reducer-categories';
import ItemReducer from './reducer-items';
import ListingReducer from './reducer-listings';
import UserReducer from './reducer-users'

const allReducers = combineReducers({
   categories: CategoryReducer,
   items: ItemReducer,
   listings: ListingReducer,
   activeUser: UserReducer
});

export default allReducers;
