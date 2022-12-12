import React, { useEffect, useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Header from "./Header";
import { useParams } from "react-router-dom";
import GPAGraph from "./GPAGraph";
import Reddit from "./Reddit";
import ProfessorList from "./ProfessorList";

/**
 * Course: displays Header and all course info: basic course info, cumulative
 * GPA graph, list of reddit comments, and info on instructors that teach that
 * course.
 * when in course page, pssing in a new search parameter does not rerender the
 * data (also applies to professor page)
 * @returns Course React element
 */
const Course = () => {
  const courseID = useParams().id;

  const [courseInfo, setCourseInfo] = useState({}); // useState hook to store the courseInfo
  const [redditList, setRedditList] = useState([]); // useState hook to store the redditList
  const [graphInfo, setGraphInfo] = useState({}); // // useState hook to store the graphInfo

  const [professorList, setProfessorList] = useState([]); // useState hook to store the professorList
  const [profGraphInfo, setProfGraphInfo] = useState([]); // useState hook to store the professor graph info

  // useEffect hook to fetch the data from the API
  useEffect(() => {
    // fetch professor grade distributions
    fetch("http://3.145.22.97/grade-distribution/" + courseID)
      .then((response) =>
        response.json().then((json) => {
          if (json && json["professor_cumulative_grade_distribution"]) {
            setProfGraphInfo(json["professor_cumulative_grade_distribution"]);
          } else setProfGraphInfo({});
        })
      )
      .catch((e) => console.log("error while calling grade-distribution API"));
  }, [courseInfo, courseID]);

  useEffect(() => {
    // fetch professor info
    fetch("http://3.145.22.97/course-profs/" + courseID)
      .then((response) =>
        response.json().then((json) => {
          var professors = [];
          // For professor course in the json response, create a new object with
          // the professor name, rate my professor rating, department, rate my
          // professor rating class, and professor ID
          for (var key in json) {
            const name = json[key].name;
            const RMPRating = json[key].RMPRating;
            const dept = json[key].dept;
            const RMPRatingClass = json[key].RMPRatingClass;
            const id = key;

            let graph = {}; // populate professor graph with prof-specific GPA's
            if (profGraphInfo.hasOwnProperty(id)) {
              const temp = profGraphInfo[id];
              if ( // if no prof graph info exists, make an empty graph
                temp.aCount === 0 &&
                temp.abCount === 0 &&
                temp.bCount === 0 &&
                temp.bcCount === 0 &&
                temp.cCount === 0 &&
                temp.dCount === 0 &&
                temp.fCount === 0
              )
                graph = [];
              else // otherwise, set the values of graph to
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
            professors.push({ // push the prof data to the professors array
              name,
              RMPRating,
              dept,
              RMPRatingClass,
              id,
              graph,
            });
          }
          setProfessorList(professors); //set the ProfessorList state as the professors array
        })
      )
      .catch((e) => console.log("error while calling course-profs API", e));
  }, [profGraphInfo, courseID]);

  useEffect(() => {
    // fetch course info
    fetch("http://3.145.22.97/course-info/" + courseID).then((response) =>
      response.json().then((json) => {
        setCourseInfo(json);
      })
    );
  }, [courseID]);

  useEffect(() => {
    // fetch reddit info
    fetch("http://3.145.22.97/reddit-comments/" + courseID).then((response) =>
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
        setRedditList(comments); // set the RedditList state as the comments array
      })
    );
  }, [courseInfo, courseID]);

  // The returned gpa graph distribution for this course is converted into the required format for our graph API
  useEffect(() => {
    // fetch cumulative GPA data
    fetch("http://3.145.22.97/grade-distribution/" + courseID).then(
      (response) =>
        response.json().then((json) => {
          if (json && json.cumulative) { // check if there is cumulative grade data for the class
            if (
              json.cumulative.aCount === 0 &&
              json.cumulative.abCount === 0 &&
              json.cumulative.bCount === 0 &&
              json.cumulative.bcCount === 0 &&
              json.cumulative.cCount === 0 &&
              json.cumulative.dCount === 0 &&
              json.cumulative.fCount === 0
            )
              setGraphInfo([]); // set the graph to an empty graph if no data
            else
              setGraphInfo([ // set the graph to the cumulative values if there is data
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
  }, [courseInfo, courseID]);

  return (
    <Container className="full">
      <Row>
        <Header />
      </Row>
      <Container className="grey-box full">
        <Row>
          {/*Course Name */}
          <h3 className="bold-heading-style">{courseInfo.cName}</h3>
        </Row>
        <Row className="heading-style">
          {/*Course Code */}
          <h3>{courseInfo.cCode}</h3>
        </Row>

        <Row>
          <Col>
            <Row>
              <h5 className="bold-heading-style">Subject</h5>
            </Row>
            <Row>
              {/*Course Subject */}
              <h5 className="heading-style">{courseInfo.cSubject}</h5>
            </Row>
          </Col>

          <Col>
            <Row>
              <h5 className="bold-heading-style">Credits</h5>
            </Row>
            <Row>
              {/*Number of course credits */}
              <h5 className="heading-style">{courseInfo.cCredits}</h5>
            </Row>
          </Col>
        </Row>

        <Row>
          <h5 className="bold-heading-style">Description</h5>
        </Row>
        <Row>
          {/*Course description */}
          <h5 className="heading-style">{courseInfo.cDescription}</h5>
        </Row>

        <Row>
          <h5 className="heading-style">
            {/*Course requisities */}
            <b>Requisites</b>
            {": " + courseInfo.cReq}
          </h5>
        </Row>

        <Row>
          {graphInfo && // if there is graph data and reddit data, make a row to
                        // hold them
          graphInfo.length > 0 &&
          redditList &&
          redditList.length > 0 ? (
            <Col>
              {graphInfo && graphInfo.length > 0 ? ( // if there is graph data, display the graph
                <div xs={12} lg={6} className="graph-box">
                  <GPAGraph graphInfo={graphInfo} />
                </div>
              ) : (
                <></>
              )}

              {redditList && redditList.length > 0 ? ( // if there is reddit infoo display reddit comments
                <Row xs={12} md={6} className="reddit-box">
                  <Reddit redditList={redditList} />
                </Row>
              ) : (
                <></>
              )}
            </Col>
          ) : (
            <></>
          )}
          // if there is course instructor information, display the professorList
          {professorList && professorList.length > 0 ? (
            <Col xs={12} lg={6}>
              <Row>
                <h5 className="bold-heading-style">Instructors</h5>
              </Row>
              <Row xs={12} lg={6} className="professor-list-container">
                {<ProfessorList professorList={professorList} />}
              </Row>
            </Col>
          ) : ( // if there is no prof info, tell the user
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
