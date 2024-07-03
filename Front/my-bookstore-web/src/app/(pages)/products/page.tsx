import React from "react";
import './styles.css';
import PageHeading from "@/components/common/PageHeading/PageHeading";
import ProductsList from '@/components/ProductsList/ProductsList';

const ProductsPage = () => {
  return (
    <div>
      <PageHeading title="Products" descriptionTitle="3 items"/>
      <div className="products-list">
        {Array(6).fill().map((_, index) => (
          <div className="product-card" key={index}>
            <img src="/images/img-product.jpg" alt="Book Pic" />
            <h6>Book Name</h6>
            <p className="price">$24.99</p>
            <p>description</p>
            <div className="quantity">
              <button>-</button>
              <span>2</span>
              <button>+</button>
            </div>
          </div>
        ))}
      </div>
      <div>
        <ProductsList />
      </div>
    </div>
  );
};

export default ProductsPage;
