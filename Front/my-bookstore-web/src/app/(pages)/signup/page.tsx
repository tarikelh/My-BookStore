import React from "react";
import './styles.css';

const SignUpPage = () => {
  return (
    <div className="signup-page">
      <div className="left-column">
        <h1>Sign Up</h1>
        <form className="signup-form">
          <label htmlFor="lastname">Last Name</label>
          <input type="text" id="lastname" name="lastname" placeholder="DOE" required />

          <label htmlFor="firstname">First Name</label>
          <input type="text" id="firstname" name="firstname" placeholder="Jane" required />

          <label htmlFor="email">Email</label>
          <input type="email" id="email" name="email" placeholder="jane.doe@example.com" required />

          <label htmlFor="password">Password</label>
          <input type="password" id="password" name="password" placeholder="********" required />

          <button type="submit" className="signup-button">Sign Up</button>

          <p className="signin-link">
            You have an account? <a href="/signin">Sign In</a>
          </p>
        </form>
      </div>
      <div className="right-column">
        <img src="/images/img-signin.jpg" alt="Books" className="background-image" />
      </div>
    </div>
  );
};

export default SignUpPage;
