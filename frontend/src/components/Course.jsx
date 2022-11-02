import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Search from "./Search";
import { useSearchParams } from "react-router-dom";
import ProfessorList from "./ProfessorList";
import GPAGraph from "./GPAGraph";
import Reddit from "./Reddit";
const Course = () => {
  const [searchparams] = useSearchParams();
  const course = searchparams.get("id");
  return (
    <Container className="full">
      <Row>
        <Col className="header-text">Madger Courses</Col>
        <Col xs={3}>
          <Search />
        </Col>
      </Row>
      <Container className="grey-box">
        <h1 className="course-name">{course}</h1>
        <Row className="row1">
          <div className="graph-box">
            <GPAGraph />
          </div>
          <div className="reddit-box">
            <Reddit />
          </div>
        </Row>
        <Row>
          <ProfessorList />
        </Row>
      </Container>
    </Container>
  );
};

export default Course;
