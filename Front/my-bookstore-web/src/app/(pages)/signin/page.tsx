import React from "react";
import './styles.css';

const SignInPage = () => {
  return (
    <div className="signin-page">
      <div className="left-column">
        <h1>Sign In</h1>
        <form className="signin-form">
          <label htmlFor="email">Email</label>
          <input type="email" id="email" placeholder="jane.doe@example.com" required />

          <label htmlFor="password">Password</label>
          <input type="password" id="password" placeholder="********" required />

          <button type="submit" className="signin-button">SIGN IN</button>

          <p className="signup-link">
            You don’t have an account? <a href="/signup">Sign up</a>
          </p>
        </form>
      </div>
      <div className="right-column">
        <img src="/images/img-signin.jpg" alt="Books" className="background-image" />
      </div>
    </div>
  );
};

export default SignInPage;
