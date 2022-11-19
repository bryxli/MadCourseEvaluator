import React, { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Header from "./Header";
import { useNavigate } from "react-router-dom";

const Instructor = ({ id }) => {
  //sample id until professor component is connected to other pages
  id = 125529;
  let navigate = useNavigate();
  const routeChange = (path) => {
    navigate(path);
  };

  // IMPORTANT CHANGE NEEDED: there are two endpoints: /prof-info and /prof-courses
  const [courses, setCourses] = useState([]);
  const [professor, setProfessor] = useState({});
  useEffect(() => {
    fetch("/prof-info/" + id).then((response) =>
      response.json().then((data) => {
        var courses = [];
        var courses_taught = data["courses-taught"];
        for (var key in courses_taught) {
          const id = key;
          const code = courses_taught[key].cCode;
          const name = courses_taught[key].cName;

          courses.push({ id, code, name });
        } //this converts the JSON object of courses-taught threads into an array
        setCourses(courses);

        setProfessor({
          name: data.professor_data.name,
          dept: data.professor_data.dept,
          rating: data.professor_data.RMPRating,
          id,
          totalRatings: data.professor_data.RMPTotalRatings,
          review: data.professor_data.RMPRatingClass,
        });
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
                    professor.rating +
                    "/" +
                    professor.totalRatings +
                    "(" +
                    professor.review +
                    ")"}
                </h5>
              </Row>
            </Col>
          </Row>
          <Row className="course-list">
            {courses &&
              courses.map((course) => (
                <p
                  className="course-list-item"
                  key={course.id}
                  onClick={() => {
                    routeChange("/course/?id=" + course.id);
                  }}
                >
                  <h4 className="course-id">
                    {course.code + " - "}{" "}
                    <bold style={{ color: "#FF7787" }}>{course.name}</bold>
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
