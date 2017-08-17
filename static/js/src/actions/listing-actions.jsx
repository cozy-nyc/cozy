import api from '../utils/api';

export function fetchListings() {
   return function(dispatch) {
      api.get("/api/listings/")
         .then((response) => {
            dispatch({type: "FETCH_LISTINGS_FULFILLED", payload: response.data})
         })
         .catch((err) => {
            dispatch({type: "FETCH_LISTINGS_ERROR", payload: err})
         })
   }
}

export function getListing(id){
   return function(dispatch){
      api.get("http://0.0.0.0:8000/api/listings/"+id)
         .then((response) => {
            dispatch({type: "FETCH_LISTING_FULFILLED", payload: response.data})
         })
         .catch((err) => {
            dispatch({type: "FETCH_LISTING_ERROR", payload: err})
         })
   }
}
