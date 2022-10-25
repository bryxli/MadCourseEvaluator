import React from "react";
import ProfessorList from "./ProfessorList";
import GPAGraph from "./GPAGraph";
import Reddit from "./Reddit";
const Course = () => {
  return (
    <>
      <div className="white-box">Madger Courses</div>

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
