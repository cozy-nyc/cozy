import api from '../../utils/api';

export function fetchItems(value) {
   return function(dispatch) {
      if(value == null || value == ''){
         api.get('/api/items/')
            .then((response) => {
               dispatch({type: "FETCH_ITEMS_FULFILLED", payload: response.data})
            })
            .catch((err) => {
               dispatch({type: "FETCH_ITEMS_ERROR", payload: err})
            })
      }else {
         api.get('/api/items/?q='+value)
            .then((response) => {
               dispatch({type: "FETCH_ITEMS_FULFILLED", payload: response.data})
            })
            .catch((err) => {
               dispatch({type: "FETCH_ITEMS_ERROR", payload: err})
            })
      }
      }
}

export function get(value, suggestions) {
      return api.get('/api/items/?q='+value)
      .then((response) => {
         suggestions(response.data);
      })
      .catch((err) => {
         console.log(err);
      })

}
