import React from "react";
import './styles.css';
import PageHeading from "@/components/common/PageHeading/PageHeading";

const CartPage = () => {
  return (
    <div>
      <PageHeading title="Basket" descriptionTitle="3 Items" />
      <div className="cart-content">
        <ul className="cart-items">
          {[
            { name: "Crimson sweet melon", pricePerUnit: "$0.89 / lb", quantity: 2, totalPrice: "$1.78", imgSrc: "/images/img-product.jpg" },
            { name: "Rainier cherries", pricePerUnit: "$3.99 / lb", quantity: 1, totalPrice: "$3.99", imgSrc: "/images/img-product.jpg" },
            { name: "Bartlett pears", pricePerUnit: "$1.99 / ea", quantity: 2, totalPrice: "$3.98", imgSrc: "/images/img-product.jpg" }
          ].map((item, index) => (
            <li className="cart-item" key={index}>
              <img src={item.imgSrc} alt={item.name} />
              <div className="item-details">
                <h6>{item.name}</h6>
                <p>{item.pricePerUnit}</p>
                <div className="quantity">
                  <button>-</button>
                  <span>{item.quantity}</span>
                  <button>+</button>
                </div>
              </div>
              <p className="total-price">{item.totalPrice}</p>
            </li>
          ))}
        </ul>
        <div className="order-summary">
          <h4>Order summary</h4>
          <div>
            <label>Subtotal</label><p>$27.44</p>
          </div>
          <div>
            <label>Shipping</label><p>$3.99</p>
          </div>
          <div>
            <label>Tax</label><p>$2.00</p>
          </div>
          <div className="total">
            <label>Total</label><p>$33.43</p>
          </div>
          <button className="checkout-button">Check out →</button>
        </div>
      </div>
    </div>
  );
};

export default CartPage;
