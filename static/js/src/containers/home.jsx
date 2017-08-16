import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import Navbar from './navbar';
import ListingQuery from './listingquery';



const Home = () => {
   return (
      <div>
         <ListingQuery />
      </div>
   );
};

export default Home;
