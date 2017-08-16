import React, { Component } from 'react';
import Navbar from '../components/navbar'

class App extends Component {
  render() {
    return (
      <div>
      <Navbar />

      <div className="container">
        {this.props.children}
      </div>

      <p>Footer here</p>
      </div>
    );
  }
}

export default App;
