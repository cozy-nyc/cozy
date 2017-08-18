import api from '../../utils/api';

export function fetchListings() {
   return function(dispatch) {
      api.get("/api/items/")
         .then((response) => {
            dispatch({type: "FETCH_ITEMS_FULFILLED", payload: response.data})
         })
         .catch((err) => {
            dispatch({type: "FETCH_ITEMS_ERROR", payload: err})
         })
   }
}
