"use client";
import React, { useState } from "react";
import "./styles.css";
import PageHeading from "@/components/common/PageHeading/PageHeading";

const ProductDetails = () => {
  const product = {
    id: 1,
    name: "Watermelon",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Mauris sit amet massa vitae tortor condimentum lacinia quis. Placerat orci nulla pellentesque dignissim enim sit amet venenatis. Sed arcu non odio euismod lacinia.",
    photo: "/images/img-product.jpg",
    price: "1.89",
  };

  const [quantity, setQuantity] = useState(2);

  const handleIncrease = () => {
    setQuantity(quantity + 1);
  };

  const handleDecrease = () => {
    if (quantity > 1) {
      setQuantity(quantity - 1);
    }
  };

  return (
    <div>
      <PageHeading />
      <div className="product-details">
        <div className="left-column">
          <img
            src={product.photo}
            alt={product.name}
            className="product-image"
          />
        </div>
        <div className="right-column">
          <h3>{product.name}</h3>
          <p>{product.description}</p>
          <p className="product-price">{`$${product.price}`}</p>
          <div className="product-actions">
            <button className="quantity-button" onClick={handleDecrease}>
              -
            </button>
            <span className="quantity">{quantity}</span>
            <button className="quantity-button" onClick={handleIncrease}>
              +
            </button>
            <button className="add-to-cart">Add to cart</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProductDetails;
