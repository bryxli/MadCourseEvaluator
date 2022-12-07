import React, { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Header from "./Header";
import { useParams, useNavigate } from "react-router-dom";

// Instructor: component that shows instructor info as well as a list of all
//    classes taught by the instructor(and links to each one)
const Instructor = () => {
  let navigate = useNavigate();

  const professorID = useParams().id;

  const [courses, setCourses] = useState([]);
  const [professor, setProfessor] = useState({});
  // fetch professor info and professor courses for a particular professorID
  useEffect(() => {
    fetch(
      "https://madcourseevaluator.herokuapp.com/prof-info/" + professorID
    ).then((response) =>
      response.json().then((json) => {
        setProfessor(json);
      })
    );
    fetch(
      "https://madcourseevaluator.herokuapp.com/prof-courses/" + professorID
    ).then((response) =>
      response.json().then((json) => {
        console.log(json);
        var classes = [];
        for (var key in json) {
          const classFull = {
            code: json[key].cCode,
            name: json[key].cName,
            id: key,
          };
          classes.push(classFull);
        }
        setCourses(classes);
      })
    );
  }, []);

  return (
    <>
      <Container className="full">
        <Row>
          <Header />
        </Row>
        <Container className="pink-box">
          <Row>
            <h1 style={{ fontSize: "xxx-large" }}>{professor.name}</h1>
          </Row>
          <Row>
            <Col>
              <Row>
                <h5 className="bold-heading-style">Department </h5>

                <h5 className="heading-style">{"  - " + professor.dept}</h5>
              </Row>

              <Row>
                <h5 className="bold-heading-style">Rating </h5>

                <h5 className="heading-style">
                  {"  - " +
                    professor.RMPRating +
                    "/" +
                    professor.RMPTotalRatings +
                    "(" +
                    professor.RMPRatingClass +
                    ")"}
                </h5>
              </Row>
            </Col>
          </Row>
          {courses.length > 0 && (
            <Row className="course-list">
              {courses.map((course) => (
                <p
                  className="course-list-item"
                  key={course.id}
                  onClick={() => {
                    navigate({
                      pathname: `/course/${course.id}`,
                    });
                  }}
                >
                  <h4 className="course-id">
                    {course.code + " - "}{" "}
                    <bold style={{ color: "#FF7787" }}>{course.name}</bold>
                  </h4>
                </p>
              ))}
            </Row>
          )}
        </Container>
      </Container>
    </>
  );
};

export default Instructor;
