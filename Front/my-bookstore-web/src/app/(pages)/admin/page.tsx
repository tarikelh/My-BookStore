import React from "react";
import './styles.css';
import PageHeading from "@/components/common/PageHeading/PageHeading";

const AdminPage = () => {
  const products = [
    { id: 1, name: "Roman-Policier", description: "Description of Product1", photo: "roman-policier.jpg", price: "16.99", available: true, isbn: "978-8-3353-2565-4" },
    { id: 2, name: "Documentation-MySQL", description: "Description of Product2", photo: "doc-mysql.jpg", price: "21.99", available: true, isbn: "978-5-3490-8182-8" },
    { id: 3, name: "Manuel-Docker", description: "Description of Product3", photo: "man-docker.jpg", price: "25.99", available: true, isbn: "978-2-7373-9403-4" },
  ];

  return (
    <div className="admin-page">
      <PageHeading title="Admin Products"/>
      <table className="product-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Photo</th>
            <th>Price</th>
            <th>Available</th>
            <th>ISBN</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product, index) => (
            <tr key={index}>
              <td>{product.id}</td>
              <td>{product.name}</td>
              <td>{product.description}</td>
              <td>{product.photo}</td>
              <td>{product.price} €</td>
              <td>
                <input type="checkbox" checked={product.available} readOnly />
              </td>
              <td>{product.isbn}</td>
              <td>
                <button className="action-button edit-button">✏️</button>
                <button className="action-button delete-button">🗑️</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AdminPage;
