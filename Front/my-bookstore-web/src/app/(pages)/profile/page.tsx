import React from "react";
import './styles.css';

const ProfilePage = () => {
  return (
    <div className="profile-page">
      <div className="left-column">
        <h1>Profile</h1>
        <form className="profile-form">
          <label htmlFor="lastname">Last Name</label>
          <input type="text" id="lastname" name="lastname" placeholder="DOE" required />

          <label htmlFor="firstname">First Name</label>
          <input type="text" id="firstname" name="firstname" placeholder="John" required />

          <label htmlFor="email">Email</label>
          <input type="email" id="email" name="email" placeholder="jane.doe@example.com" required />

          <label htmlFor="password">Password</label>
          <input type="password" id="password" name="password" placeholder="********" required />

          <button type="submit" className="update-button">Update</button>
        </form>
      </div>
      <div className="right-column">
        <img src="/images/img-profile.jpg" alt="Books" className="background-image" />
      </div>
    </div>
  );
};

export default ProfilePage;
