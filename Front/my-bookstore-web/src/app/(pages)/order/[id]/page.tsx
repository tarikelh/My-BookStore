import React from "react";
import "./styles.css";
import PageHeading from "@/components/common/PageHeading/PageHeading";

const OrderConfirmationPage: React.FC = () => {
  const orderNumber = "1234";
  const orderDate = "May 21, 2024";
  const customerName = "TARIK";
  const products = [
    {
      name: "Roman-Policier",
      description: "Description of Product1",
      quantity: 2,
      price: 16.99,
    },
    {
      name: "Documentation-MySQL",
      description: "Description of Product2",
      quantity: 1,
      price: 21.99,
    },
    {
      name: "Manuel-Docker",
      description: "Description of Product3",
      quantity: 2,
      price: 25.99,
    },
  ];
  const subtotal = 107.95;
  const total = 107.95;

  return (
    <div>
      <PageHeading/>
      <div className="order-confirmation">
        <p className="thank-you">
          Thank you for your order {customerName.toUpperCase()}, we have
          received your order n°{orderNumber}. It is now being processed
        </p>
        <table>
          <thead>
            <tr>
              <th>Product</th>
              <th>Quantity</th>
              <th>Price</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product, index) => (
              <tr key={index}>
                <td>
                  {product.name} | {product.description}
                </td>
                <td>{product.quantity}</td>
                <td>{product.price.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <div className="totals">
          <div className="subtotal">
            <span>Subtotal</span>
            <span>{subtotal.toFixed(2)}</span>
          </div>
          <div className="total">
            <span>Total</span>
            <span>{total.toFixed(2)}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default OrderConfirmationPage;
