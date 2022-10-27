import React from "react";

const data = [
  { courseID: "CS 577", id: 1, courseName: "Introduction to Algorithms" },
  {
    courseID: "CS 540",
    id: 2,
    courseName: "Introduction to Artificial Intelligence",
  },
  { courseID: "MATH 222", id: 3, courseName: "Calculus 2" },
  { courseID: "MATH 341", id: 4, courseName: "Linear Algebra" },
];

const Instructor = () => {
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
        <h1 style={{ fontSize: "xxx-large" }}>Professor A</h1>
        <div className="course-list">
          {data.map((course) => (
            <p className="course-list-item" key={course.id}>
              <h4 className="course-id">
                {course.courseID + " - "}{" "}
                <bold style={{ color: "#FF7787" }}>{course.courseName}</bold>
              </h4>
            </p>
          ))}
        </div>
      </div>
    </>
  );
};

export default Instructor;
