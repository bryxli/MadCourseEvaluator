import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Header from "./Header";
import { useSearchParams } from "react-router-dom";
import ProfessorList from "./ProfessorList";
import GPAGraph from "./GPAGraph";
import Reddit from "./Reddit";

const Course = () => {
  const [searchparams] = useSearchParams();
  const course = searchparams.get("id");

  // todo:create a GET request using course for course data, then pass in as props
  // todo:after retrieving data, fill our course-name, GPAGraph, Reddit, ProfessorList with props
  return (
    <Container className="full">
      <Row>
        <Header />
      </Row>
      <Container className="grey-box">
        <h1 className="course-name">{course}</h1>
        <Row className="row1">
          <Col className="graph-box">
            <GPAGraph id={course} />
          </Col>
          <Col className="reddit-box">
            <Reddit id={course} />
          </Col>
        </Row>
        <Row>
          <ProfessorList id={course} />
        </Row>
      </Container>
    </Container>
  );
};

export default Course;
