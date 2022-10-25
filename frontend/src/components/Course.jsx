import React from "react";
import ProfessorList from "./ProfessorList";
import GPAGraph from "./GPAGraph";
import Reddit from "./Reddit";
const Course = () => {
  return (
    <>
      <div className="white-box">
        <p style={{ fontWeight: 400 }}>Madger Courses</p>
        <form className="search-box" style={{ height: "75%", width: "20%" }}>
          <input type="search" />
          <button type="submit">Search</button>
        </form>
      </div>

      <div className="grey-box">
        <h1 className="course-name">CS 577</h1>
        <div className="row1">
          <div className="graph-box">
            <GPAGraph />
          </div>
          <div className="reddit-box">
            <Reddit />
          </div>
        </div>
        <div>
          <ProfessorList />
        </div>
      </div>
    </>
  );
};

export default Course;
