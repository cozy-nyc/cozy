import api from '../utils/api';
import { SubmissionError } from 'redux-form'

export function login(values) {
   api.post('/api-token-auth/',{
       username: values.username,
       password: values.password
       })
       .then(function(response){
         csrftoken = response.data
         console.log(response);
       })
       .catch(function(error) {
         console.log(error);
       });
}
