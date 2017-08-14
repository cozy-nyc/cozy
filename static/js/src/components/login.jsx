import React, {Component} from 'react';
import {connect} from 'react-redux';

import LoginForm from '../forms/login-form'

class Login extends Component {

   render() {
      return (
         <div>
            <h1>Login</h1>
            <LoginForm />
         </div>
       );
   }
}

export default Login;
