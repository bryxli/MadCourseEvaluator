import React from "react";
//import { Link } from "react-router-dom";

const Home = () => {
  return (
    <>
      <div className="white-box">Madger Courses</div>
      <div className="pink-box">
        <h1>Madger Courses</h1>
        <h4>Detailed Course information at your fingertips</h4>
        <form className="search-box">
          <input type="search" placeholder="Search..." />
          <button type="submit">Search</button>
        </form>
        {/**<br />
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/course">Course</Link>
          </li>
          <li>
            <Link to="/instructor">Instructor</Link>
          </li>
  </ul>**/}
      </div>
    </>
  );
};

export default Home;
