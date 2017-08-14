import api from '../utils/api';

export function login() {
   api.post('/api-token-auth/',{
       username: 'test',
       password: 'yeet12345'
       })
       .then(function(response){
         csrftoken = response.data
         console.log(response);
       })
       .catch(function(error) {
         console.log(error);
       });
    }
}
