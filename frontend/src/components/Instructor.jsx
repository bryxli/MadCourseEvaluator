import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Header from "./Header";

{
  /**        */
}

const Instructor = () => {
  const data = {
    courses_taught: [
      {
        cCode: "COMP SCI 577",
        cCredits: "4 credits",
        cDescription:
          "Basic paradigms for the design and analysis of efficient algorithms: greed, divide-and-conquer, dynamic programming, reductions, and the use of randomness. Computational intractability including typical NP-complete problems and ways to deal with them.",
        cName: "INTRODUCTION TO ALGORITHMS",
        cReq: "Requisites: (MATH/COMPSCI240 or STAT/COMPSCI/MATH475) and (COMP SCI 367 or 400), or graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals",
        cSubject: "Computer Sciences",
        cUID: 40539,
      },
    ],
    professor_data: {
      RMPID: 125529,
      RMPRating: 1.9,
      RMPRatingClass: "poor",
      RMPTotalRatings: 46,
      dept: "Computer Science",
      name: "Eric Bach",
    },
  };
  return (
    <>
      <Container className="full">
        <Row>
          <Header />
        </Row>
        <Container className="pink-box">
          <Row>
            <h1 style={{ fontSize: "xxx-large" }}>
              {data.professor_data.name}
            </h1>
          </Row>
          <Row>
            <Col>
              <Row>
                <h5 className="bold-heading-style">Department </h5>

                <h5 className="heading-style">
                  {"  - " + data.professor_data.dept}
                </h5>
              </Row>

              <Row>
                <h5 className="bold-heading-style">Rating </h5>

                <h5 className="heading-style">
                  {"  - " +
                    data.professor_data.RMPRating +
                    "/10     (" +
                    data.professor_data.RMPRatingClass +
                    ")"}
                </h5>
              </Row>
            </Col>
          </Row>
          <Row className="course-list">
            {data &&
              data.courses_taught &&
              data.courses_taught.map((course) => (
                <p className="course-list-item" key={course.cUID}>
                  <h4 className="course-id">
                    {course.cCode + " - "}{" "}
                    <bold style={{ color: "#FF7787" }}>{course.cName}</bold>
                  </h4>
                </p>
              ))}
          </Row>
        </Container>
      </Container>
    </>
  );
};

export default Instructor;
