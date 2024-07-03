import React from "react";
import './styles.css';
import PageHeading from "@/components/common/PageHeading/PageHeading";

const DashboardPage = () => {
  const orders = [
    { number: "0110", date: "21/05/2024", state: "In progress", total: "35.00 €" },
    { number: "0111", date: "21/05/2024", state: "Completed", total: "42.98 €" },
    { number: "0109", date: "21/05/2024", state: "Cancelled", total: "23.99 €" },
  ];

  return (
    <div className="dashboard-page">
      <PageHeading/>
      <table className="order-table">
        <thead>
          <tr>
            <th>Ord number</th>
            <th>Date</th>
            <th>State</th>
            <th>Total</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order, index) => (
            <tr key={index}>
              <td>{order.number}</td>
              <td>{order.date}</td>
              <td>{order.state}</td>
              <td>{order.total}</td>
              <td>
                <button className="details-button">Details</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DashboardPage;
