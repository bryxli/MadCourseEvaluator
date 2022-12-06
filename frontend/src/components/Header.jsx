import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Search from "./Search";
import { LinkContainer } from "react-router-bootstrap";

const Header = () => {
  return (
    <Container className="full">
      <div class="topnav">
        <a class="active" href="/" style={{ fontWeight: "bold" }}>
          &nbsp;&nbsp;&nbsp;MadCourseEvaluator
        </a>
        <a href="/">Home</a>
        <a href="/Docs">Docs</a>
      </div>
    </Container>
  );
};

export default Header;
