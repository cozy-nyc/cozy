import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import Navbar from '../components/navbar';
import ListingQuery from '../components/listingquery';



const Home = () => {
   return (
      <div>
         <Navbar />
         <ListingQuery />
      </div>
   );
};

export default Home;
