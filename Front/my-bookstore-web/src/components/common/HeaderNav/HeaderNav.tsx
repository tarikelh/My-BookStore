import React from 'react';
import styles from './HeaderNav.module.css';

const HeaderNav: React.FC = () => {
  return (
    <header className={styles.header}>
      <h1>My C2W BookStore</h1>
      <nav className={styles.nav}>
      <ul>
        <li><a href="/">Home</a></li>
        {/* <li><a href="/subscribe">Subcribe</a></li> */}
        <li><a href="/products">Shop</a></li>
        <li><a href="/cart">Basket</a></li>
      </ul>
      </nav>
    </header>
  );
};

export default HeaderNav;
