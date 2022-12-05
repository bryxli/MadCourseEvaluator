import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { createSearchParams, useNavigate } from "react-router-dom";
import {
  BarChart,
  CartesianGrid,
  YAxis,
  XAxis,
  Tooltip,
  Legend,
  Bar,
} from "recharts";
const ProfessorList = ({ professorList }) => {
  let navigate = useNavigate();

  return (
    <div className="professor-list">
      {professorList.map((prof) => (
        <Container key={prof.id} className="professor-list-item">
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
            <Col xs={prof.graph && prof.graph.length > 0 ? undefined : 12}>
              <Row>
                <h6 className="center">
                  <b>{prof.name}</b>
                </h6>
              </Row>
              <Row>
                <p> </p>
              </Row>
              <Row>
                <h6 className="center">
                  <b>{"Dept"}</b>
                </h6>
              </Row>
              <Row>
                <h6 className="center">{prof.dept}</h6>
              </Row>
              <Row>
                <h6 className="center">
                  <b>{"Rating"}</b>
                </h6>
              </Row>
              <Row>
                <h6 className="center">
                  {prof.RMPRating + "/5, " + prof.RMPRatingClass}
                </h6>
              </Row>
            </Col>
            {prof.graph && prof.graph.length > 0 && (
              <Col xs={8}>
                <BarChart width={300} height={200} data={prof.graph}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" />{" "}
                  {/**XAxis displays the name label of each object in the array **/}
                  <YAxis dataKey="grade" />{" "}
                  {/**XAxis displays the grade label of each object in the array **/}
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="grade" fill="#FF7787" />
                </BarChart>
              </Col>
            )}
          </Row>
        </Container>
      ))}
    </div>
  );
};

export default ProfessorList;
