import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Search from "./Search";
import { LinkContainer } from "react-router-bootstrap";

// header: white bar with Madger Courses text that links back to homepage
// contains search bar on left
const Header = () => {
  return (
    <Container className="full">
      <Row>
        <Col className="header-text">
          <LinkContainer to="/">
            <h3>Madger Courses</h3>
          </LinkContainer>
        </Col>
        <Col>
          <Search />
        </Col>
      </Row>
    </Container>
  );
};

export default Header;
