import api from '../utilities/api';

export function fetchListings() {
   return function(dispatch) {
      api.get("http://0.0.0.0:8000/api/items/")
         .then((response) => {
            dispatch({type: "FETCH_ITEMS_FULFILLED", payload: response.data})
         })
         .catch((err) => {
            dispatch({type: "FETCH_ITEMS_ERROR", payload: err})
         })
   }
}
