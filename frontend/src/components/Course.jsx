import React, { useEffect, useState } from "react";
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

  const data = {
    cCode: "COMP SCI 577",
    cCredits: "4 credits",
    cDescription:
      "Basic paradigms for the design and analysis of efficient algorithms: greed, divide-and-conquer, dynamic programming, reductions, and the use of randomness. Computational intractability including typical NP-complete problems and ways to deal with them.",
    cName: "INTRODUCTION TO ALGORITHMS",
    cReq: "Requisites: (MATH/COMPSCI240 or STAT/COMPSCI/MATH475) and (COMP SCI 367 or 400), or graduate/professional standing, or declared in the Capstone Certificate in Computer Sciences for Professionals",
    cSubject: "Computer Sciences",
    cUID: 50806,
  };
  const [graphInfo, setGraphInfo] = useState({});

  useEffect(() => {
    fetch("/graphDistribution/" + course).then((response) =>
      response.json().then((d) => {
        if (d && d.cumulative) {
          setGraphInfo([
            { name: "A", grade: d.cumulative.aCount },
            { name: "AB", grade: d.cumulative.abCount },
            { name: "B", grade: d.cumulative.bCount },
            { name: "BC", grade: d.cumulative.bcCount },
            { name: "C", grade: d.cumulative.cCount },
            { name: "D", grade: d.cumulative.dCount },
            { name: "F", grade: d.cumulative.fCount },
          ]);
        } else setGraphInfo([]);
      })
    );
  }, []);

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
              <h3 className="bold-heading-style">{data.cName}</h3>
            </Row>
            <Row className="heading-style">
              <h3>{data.cCode}</h3>
            </Row>
            <Row className="graph-box">
              <GPAGraph id={course} graphInfo={graphInfo} />
            </Row>

            <Row className="reddit-box-header">
              <img height="124px" width="220px" src="Reddit.png" />
            </Row>
            <Reddit id={course} />
          </Col>

          <Col>
            <Row>
              <Col>
                <Row>
                  <h5 className="bold-heading-style">Subject</h5>
                </Row>
                <Row>
                  <h5 className="heading-style">{data.cSubject}</h5>
                </Row>
              </Col>

              <Col>
                <Row>
                  <h5 className="bold-heading-style">Credits</h5>
                </Row>
                <Row>
                  <h5 className="heading-style">{data.cCredits}</h5>
                </Row>
              </Col>
            </Row>

            <Row>
              <h5 className="bold-heading-style">Description</h5>
            </Row>
            <Row>
              <h5 className="heading-style">{data.cDescription}</h5>
            </Row>

            <Row>
              <h5 className="heading-style">{data.cReq}</h5>
            </Row>

            <Row className="heading-style">
              {/**<ProfessorList id={course} />**/}
            </Row>
          </Col>
        </Row>
      </Container>
    </Container>
  );
};

export default Course;
