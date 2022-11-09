import React, { useEffect, useState } from "react";

const data = [
  {
    Fname: "Angel",
    Lname: "Abruna Rodriguez",
    dept: "Chemistry",
    RMPID: 1057192,
    RMPRating: 4.1,
    RMPTotalRatings: 13,
    RMPRatingClass: "good",
  },
  {
    Fname: "Angel",
    Lname: "Abruna Rodriguez",
    dept: "Chemistry",
    RMPID: 1057192,
    RMPRating: 4.1,
    RMPTotalRatings: 13,
    RMPRatingClass: "good",
  },
  {
    Fname: "Angel",
    Lname: "Abruna Rodriguez",
    dept: "Chemistry",
    RMPID: 1057192,
    RMPRating: 4.1,
    RMPTotalRatings: 13,
    RMPRatingClass: "good",
  },
  {
    Fname: "Angel",
    Lname: "Abruna Rodriguez",
    dept: "Chemistry",
    RMPID: 1057192,
    RMPRating: 4.1,
    RMPTotalRatings: 13,
    RMPRatingClass: "good",
  },
  {
    Fname: "Angel",
    Lname: "Abruna Rodriguez",
    dept: "Chemistry",
    RMPID: 1057192,
    RMPRating: 4.1,
    RMPTotalRatings: 13,
    RMPRatingClass: "good",
  },
];

const ProfessorList = (props) => {
  const course = props.id;

  const [professorList, setProfessorList] = useState([]);
  useEffect(() => {
    fetch("/proflist/" + course).then((response) =>
      response.json().then((data) => {
        setProfessorList(data);
      })
    );
  }, []);

  professorList;

  return (
    <div className="professor-list">
      {data.map((prof) => (
        <p className="professor-list-item" key={prof.RMPID}>
          <img src="person.jpeg" style={{ height: 100, width: 100 }} />
          <h5>{prof.Fname + " " + prof.Lname}</h5>
          <h6>{"Dept " + prof.dept}</h6>
          <h6>{"Rating - " + prof.RMPRating}</h6>
          <h6>{"Class Rating - " + prof.RMPRatingClass}</h6>
          <h6>{"Total Ratings - " + prof.RMPTotalRatings}</h6>
        </p>
      ))}
    </div>
  );
};

export default ProfessorList;
