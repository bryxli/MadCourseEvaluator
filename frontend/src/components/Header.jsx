import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Search from "./Search";
import { LinkContainer } from "react-router-bootstrap";
import { useLocation } from "react-router-dom";

// header: white bar with Madger Courses text that links back to homepage
//    contains search bar on left
// this component is used by Course, Instructor and Home
const Header = () => {
  let location = useLocation();
  const [isHome, setIsHome] = useState(location);

  React.useEffect(() => {
    // Google Analytics
    console.log(location.pathname);
    if (location.pathname === "/") setIsHome(true);
    else setIsHome(false);
  }, [location]);

  return (
    <Container className="full">
      <Row>
        <LinkContainer to="/">
          <Col className="header-start">
            <img className="header-logo" src="/teamLogo.png" alt="team-logo" />

            <h3 className="header-text">  UW </h3>
          </Col>
        </LinkContainer>
        {!isHome && (
          <Col>
            <Search />
          </Col>
        )}
      </Row>
    </Container>
  );
};

export default Header;
