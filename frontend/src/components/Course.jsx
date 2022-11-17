import React, { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Header from "./Header";
import { useSearchParams } from "react-router-dom";
import GPAGraph from "./GPAGraph";
import Reddit from "./Reddit";
import ProfessorList from "./ProfessorList";

const Course = () => {
  const [searchparams] = useSearchParams();
  const courseID = searchparams.get("id");

  const [courseInfo, setCourseInfo] = useState({});

  //the returned gpa graph distribution for this course is converted into the required format for our graph API
  useEffect(() => {
    fetch("/course/" + courseID).then((response) =>
      response.json().then((d) => {
        const json_str = JSON.stringify(d);
        const json = JSON.parse(json_str);
        setCourseInfo(json);
      })
    );
  }, []);

  console.log(courseInfo);

  // todo:create a GET request using course for course data, then pass in as props
  // todo:after retrieving data, fill our heading-style, GPAGraph, Reddit, ProfessorList with props
  return (
    <Container className="full">
      <Row>
        <Header />
      </Row>
      <Container className="grey-box">
        <Row>
          <Col>
            <Row>
              <h3 className="bold-heading-style">{courseInfo.cName}</h3>
            </Row>
            <Row className="heading-style">
              <h3>{courseInfo.cCode}</h3>
            </Row>
            <Row className="graph-box">
              <GPAGraph id={courseID} />
            </Row>

            <Row className="reddit-box-header">
              <img
                height="124px"
                width="220px"
                src="/Reddit.png"
                alt="reddit-logo"
              />
            </Row>
            <Reddit id={courseID} />
          </Col>

          <Col>
            <Row>
              <Col>
                <Row>
                  <h5 className="bold-heading-style">Subject</h5>
                </Row>
                <Row>
                  <h5 className="heading-style">{courseInfo.cSubject}</h5>
                </Row>
              </Col>

              <Col>
                <Row>
                  <h5 className="bold-heading-style">Credits</h5>
                </Row>
                <Row>
                  <h5 className="heading-style">{courseInfo.cCredits}</h5>
                </Row>
              </Col>
            </Row>

            <Row>
              <h5 className="bold-heading-style">Description</h5>
            </Row>
            <Row>
              <h5 className="heading-style">{courseInfo.cDescription}</h5>
            </Row>

            <Row>
              <h5 className="heading-style">{courseInfo.cReq}</h5>
            </Row>

            <Row>
              <h5 className="bold-heading-style">Instructors</h5>
            </Row>
            <Row className="heading-style">
              {<ProfessorList id={courseID} />}
            </Row>
          </Col>
        </Row>
      </Container>
    </Container>
  );
};

export default Course;
