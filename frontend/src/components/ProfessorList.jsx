import React, { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const ProfessorList = (props) => {
  const course = props.id;

  const [professorList, setProfessorList] = useState([]);
  useEffect(() => {
    fetch("/course-profs/" + course).then((response) =>
      response.json().then((json) => {
        var professors = [];
        for (var key in json) {
          const name = json[key].name;
          const RMPRating = json[key].RMPRating;
          const dept = json[key].dept;
          const RMPRatingClass = json[key].RMPRatingClass;
          professors.push({ name, RMPRating, dept, RMPRatingClass });
        }
        setProfessorList(professors);
      })
    );
  }, []);

  return (
    <div className="professor-list">
      {professorList.map((prof) => (
        <Container className="professor-list-item" /*key={prof.RMPID}*/>
          <Row>
            <Col>
              <Row>
                <h6>
                  <b>{prof.name}</b>
                </h6>
              </Row>
              <Row>
                <p> </p>
              </Row>
              <Row>
                <h6>
                  <b>{"Dept"}</b>
                </h6>
              </Row>
              <Row>
                <h6>{prof.dept}</h6>
              </Row>
              <Row>
                <h6>
                  <b>{"Rating"}</b>
                </h6>
              </Row>
              <Row>
                <h6>{prof.RMPRating + "/5, " + prof.RMPRatingClass}</h6>
              </Row>
            </Col>
            <Col> // prof-specific GPA graph, eventually</Col>
          </Row>
        </Container>
      ))}
    </div>
  );
};

export default ProfessorList;
