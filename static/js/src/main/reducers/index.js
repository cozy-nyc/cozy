import { combineReducers } from 'redux';
import CategoryReducer from './reducer-categories';
import ActiveCategory from './reducer-active-category';


const allReducers = combineReducers({
   categories: CategoryReducer,
   activeCatergory: ActiveCategory
});

export default allReducers;
