import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Search from "./Search";
import { LinkContainer } from "react-router-bootstrap";

const Header = () => {
  return (
    <Container className="full">
      <Row>
        <Col className="header-text" xs={9}>
          <LinkContainer to="/">
            <h3>Madger Courses</h3>
          </LinkContainer>
        </Col>
        <Col xs={2}>
          <Search />
        </Col>
      </Row>
    </Container>
  );
};

export default Header;
