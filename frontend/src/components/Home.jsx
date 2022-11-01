import React from "react";
import Search from "./Search";

const Home = () => {
  return (
    <>
      <div className="white-box">Madger Courses</div>
      <div className="pink-box">
        <h1>Madger Courses</h1>
        <h4>Detailed Course information at your fingertips</h4>
        <Search />
      </div>
    </>
  );
};

export default Home;
