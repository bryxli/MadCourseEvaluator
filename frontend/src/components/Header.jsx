import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Search from "./Search";
import { LinkContainer } from "react-router-bootstrap";

const Header = () => {
  return (
    <Container className="full header-container">
      <Row>
        <Col xs={1} className="header-logo">
        <img
              height="50px"
              width="50px"
              src="/teamLogo.ico"
              alt="team-logo"
            />
        </Col>
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
