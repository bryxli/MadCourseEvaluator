import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Search from "./Search";

const Home = () => {
  return (
    <Container className="full">
      <Row className="header-text">Madger Courses</Row>
      <Row className="pink-box">
        <h1>Madger Courses</h1>
        <h4>Detailed Course information at your fingertips</h4>
        <Search />
      </Row>
    </Container>
  );
};

export default Home;
