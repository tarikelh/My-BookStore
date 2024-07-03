import React from "react";
import './globals.css';

const HomePage: React.FC = () => {
  return (
    <div className="container">
      <h3>Welcome in our Book Shop about everything and nothing</h3>
      <div className="buttons">
        <button className="shopButton">Browse our Shop</button>
      </div>
      <div className="images">
        <img src="/images/img-signin.jpg" alt="Book display" />
        <img src="/images/img-homepage.jpg" alt="Library" />
      </div>
    </div>
  );
};

export default HomePage;
