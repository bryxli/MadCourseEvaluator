import React, { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { createSearchParams, useNavigate } from "react-router-dom";

const ProfessorList = (props) => {
  let navigate = useNavigate();

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
          const id = key;
          professors.push({ name, RMPRating, dept, RMPRatingClass, id });
        }
        setProfessorList(professors);
      })
    );
  }, []);

  return (
    <div className="professor-list">
      {professorList.map((prof) => (
        <Container className="professor-list-item" /*key={prof.RMPID}*/>
          <Row
            onClick={() => {
              navigate({
                pathname: "/instructor",
                search: createSearchParams({
                  id: prof.id,
                }).toString(),
              });
            }}
          >
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
