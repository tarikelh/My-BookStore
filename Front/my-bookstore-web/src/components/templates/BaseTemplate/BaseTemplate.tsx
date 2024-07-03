import React from 'react';
import HeaderNav from '../../common/HeaderNav/HeaderNav';
import styles from './BaseTemplate.module.css';

type BaseTemplateProps = {
  children: React.ReactNode;
};

const BaseTemplate: React.FC<BaseTemplateProps> = ({ children }) => {
  return (
    <div className={styles.container}>
      <HeaderNav />
      <main>{children}</main>
    </div>
  );
};

export default BaseTemplate;
