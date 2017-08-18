import { combineReducers } from 'redux';
import { reducer as formReducer } from 'redux-form';

import CategoryReducer from './reducer-categories';
import ItemReducer from './reducer-items';
import ListingReducer from './reducer-listings';
import authReducer from './reducer-auth';

const allReducers = combineReducers({
   categories: CategoryReducer,
   items: ItemReducer,
   listings: ListingReducer,
   auth: authReducer,
   form: formReducer,
});

export default allReducers;
