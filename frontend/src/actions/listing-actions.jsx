import api from '../utilities/api';

export function fetchListings() {
   return function(dispatch) {
      api.get("http://0.0.0.0:8000/api/listing/")
         .then((response) => {
            dispatch({type: "FETCH_LISTINGS_FULFILLED", payload: response.data})
         })
         .catch((err) => {
            dispatch({type: "FETCH_LISTINGS_ERROR", payload: err})
         })
   }
}
