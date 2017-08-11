import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import store from '../store';
import Navbar from '../components/navbar';
import ListingsQuery from '../components/listingquery';



const HomePage= () => {
  return (
      <div>
         <Navbar />
         <Listings />
      </div>
);
};

export default HomePage;
