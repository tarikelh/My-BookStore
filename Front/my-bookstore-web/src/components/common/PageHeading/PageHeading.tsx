import React from "react";
import "./PageHeading.module.css";

interface PageHeadingProps {
  title: string;
  descriptionTitle: string;
}

const PageHeading: React.FC<PageHeadingProps> = ({title, descriptionTitle}) => {
  return (
    <div className="page-heading">
      <div className="page-heading-left">
        <h2>{title}</h2>
        <p className="availability-date">
          {descriptionTitle}
        </p>
      </div>
      <div className="page-heading-right">
        <button className="filter-button active">Default</button>
        <button className="filter-button">A-Z</button>
        <button className="filter-button">List view</button>
      </div>
    </div>
  );
};

export default PageHeading;
