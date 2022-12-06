import React, { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Header from "./Header";
import { useParams } from "react-router-dom";
import GPAGraph from "./GPAGraph";
import Reddit from "./Reddit";
import ProfessorList from "./ProfessorList";

// when in course page, pssing in a new search parameter does not rerender the data (also applies to professor page)
const Course = () => {
  const courseID = useParams().id;

  const [courseInfo, setCourseInfo] = useState({});
  const [redditList, setRedditList] = useState([]);
  const [graphInfo, setGraphInfo] = useState({});

  const [professorList, setProfessorList] = useState([]);
  const [profGraphInfo, setProfGraphInfo] = useState([]);

  useEffect(() => {
    fetch(
      "https://madcourseevaluator.herokuapp.com/grade-distribution/" + courseID
    )
      .then((response) =>
        response.json().then((json) => {
          if (json && json["professor_cumulative_grade_distribution"]) {
            setProfGraphInfo(json["professor_cumulative_grade_distribution"]);
          } else setProfGraphInfo({});
        })
      )
      .catch((e) => console.log("error while calling grade-distribution API"));
  }, [courseInfo]);

  useEffect(() => {
    fetch("https://madcourseevaluator.herokuapp.com/course-profs/" + courseID)
      .then((response) =>
        response.json().then((json) => {
          var professors = [];
          for (var key in json) {
            const name = json[key].name;
            const RMPRating = json[key].RMPRating;
            const dept = json[key].dept;
            const RMPRatingClass = json[key].RMPRatingClass;
            const id = key;

            let graph = {};
            if (profGraphInfo.hasOwnProperty(id)) {
              const temp = profGraphInfo[id];

              graph = [
                { name: "A", grade: temp.aCount ?? 0 },
                { name: "AB", grade: temp.abCount ?? 0 },
                { name: "B", grade: temp.bCount ?? 0 },
                { name: "BC", grade: temp.bcCount ?? 0 },
                { name: "C", grade: temp.cCount ?? 0 },
                { name: "D", grade: temp.dCount ?? 0 },
                { name: "F", grade: temp.fCount ?? 0 },
              ];
            }
            professors.push({
              name,
              RMPRating,
              dept,
              RMPRatingClass,
              id,
              graph,
            });
          }
          setProfessorList(professors);
        })
      )
      .catch((e) => console.log("error while calling course-profs API", e));

    console.log(professorList);
  }, [profGraphInfo]);

  useEffect(() => {
    fetch(
      "https://madcourseevaluator.herokuapp.com/course-info/" + courseID
    ).then((response) =>
      response.json().then((json) => {
        setCourseInfo(json);
      })
    );
  }, []);

  useEffect(() => {
    fetch(
      "https://madcourseevaluator.herokuapp.com/reddit-comments/" + courseID
    ).then((response) =>
      response.json().then((json) => {
        var comments = [];
        for (var key in json) {
          const id = key;
          const body = json[key].comBody;
          const link = json[key].comLink;
          const votes = json[key].comVotes;

          comments.push({ id, body, link, votes });
        } // This converts the JSON object of reddit threads into an array
        comments.sort((a, b) => {
          return b.votes - a.votes;
        }); // Sorting in descending order based on upvotes
        setRedditList(comments);
      })
    );
  }, [courseInfo]);

  // The returned gpa graph distribution for this course is converted into the required format for our graph API
  useEffect(() => {
    fetch(
      "https://madcourseevaluator.herokuapp.com/grade-distribution/" + courseID
    ).then((response) =>
      response.json().then((json) => {
        if (json && json.cumulative) {
          setGraphInfo([
            { name: "A", grade: json.cumulative.aCount },
            { name: "AB", grade: json.cumulative.abCount },
            { name: "B", grade: json.cumulative.bCount },
            { name: "BC", grade: json.cumulative.bcCount },
            { name: "C", grade: json.cumulative.cCount },
            { name: "D", grade: json.cumulative.dCount },
            { name: "F", grade: json.cumulative.fCount },
          ]);
        } else setGraphInfo([]);
      })
    );
  }, [courseInfo]);

  return (
    <Container className="full">
      <Row>
        <Header />
      </Row>
      <Container className="grey-box full">
        <Row>
          <h3 className="bold-heading-style">{courseInfo.cName}</h3>
        </Row>
        <Row className="heading-style">
          <h3>{courseInfo.cCode}</h3>
        </Row>

        <Row>
          <Col>
            <Row>
              <h5 className="bold-heading-style">Subject</h5>
            </Row>
            <Row>
              <h5 className="heading-style">{courseInfo.cSubject}</h5>
            </Row>
          </Col>

          <Col>
            <Row>
              <h5 className="bold-heading-style">Credits</h5>
            </Row>
            <Row>
              <h5 className="heading-style">{courseInfo.cCredits}</h5>
            </Row>
          </Col>
        </Row>

        <Row>
          <h5 className="bold-heading-style">Description</h5>
        </Row>
        <Row>
          <h5 className="heading-style">{courseInfo.cDescription}</h5>
        </Row>

        <Row>
          <h5 className="heading-style">
            <b>Requisites</b>
            {": " + courseInfo.cReq}
          </h5>
        </Row>

        <Row>
          <Col>
            {graphInfo && graphInfo.length > 0 ? (
              <div xs={12} lg={6} className="graph-box">
                <GPAGraph graphInfo={graphInfo} />
              </div>
            ) : (
              <></>
            )}

            {redditList && redditList.length > 0 ? (
              <Row xs={12} md={6} className="reddit-box">
                <Reddit redditList={redditList} />
              </Row>
            ) : (
              <h5 className="heading-style">
                No reddit threads found for this course
              </h5>
            )}
          </Col>
          {professorList && professorList.length > 0 ? (
            <Col xs={12} lg={6}>
              <Row>
                <h5 className="bold-heading-style">Instructors</h5>
              </Row>
              <Row xs={12} lg={6} className="professor-list-container">
                {<ProfessorList professorList={professorList} />}
              </Row>
            </Col>
          ) : (
            <>
              <h5 className="heading-style">
                No Intructor Info found for this course
              </h5>
            </>
          )}
        </Row>
      </Container>
    </Container>
  );
};

export default Course;
