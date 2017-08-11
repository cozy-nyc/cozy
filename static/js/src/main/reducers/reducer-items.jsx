export default function Reducer(
   state={
      item: {
         id: null,
         name: null,
         category: null,
         description: null,
      },
      fetching: false,
      fetched: false,
      item: [],
      error: null,
   }, action
   ) {
   switch (action.type) {
      case "FETCH_ITEMS_PENDING": {
         return {...state, fetching: true}
         break;
      }
      case "FETCH_ITEMS_REJECTED":{
         return {...state, fecthing: false, error: action.payload}
         break;
      }
      case "FETCH_ITEMS_FULFILLED": {
         return {
            ...state,
            fecthing: false,
            fetched: true,
            items: action.payload,
            }
         break;
      }
   }
   return state;
};
