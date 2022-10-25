import React from "react";
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./components/Home";
import Course from "./components/Course";
import Instructor from "./components/Instructor";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="/course" element={<Course />} />
          <Route path="/instructor" element={<Instructor />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
