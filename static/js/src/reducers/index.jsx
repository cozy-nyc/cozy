import { combineReducers } from 'redux';

import CategoryReducer from './reducer-categories';
import ItemReducer from './reducer-items';
import ListingReducer from './reducer-listings';

const allReducers = combineReducers({
   categories: CategoryReducer,
   items: ItemReducer,
   listings: ListingReducer,
});

export default allReducers;
