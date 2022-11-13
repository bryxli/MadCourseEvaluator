import React, { useEffect, useState } from "react";
import {
  BarChart,
  CartesianGrid,
  YAxis,
  XAxis,
  Tooltip,
  Legend,
  Bar,
} from "recharts";

const GPAGraph = ({ id }) => {
  // this is the fetch command to call the endpoint /distr/cUID assuming endpoint returns pre-formatted json file
  // const [gradeDistribution, setGradeDistribution] = useState({});
  /**  useEffect(() => {
    fetch("/distr/" + course).then((response) =>
      response.json().then((data) => {
        setGradeDistribution(data);
      })
    );
  }, []);
  */

  const [graphInfo, setGraphInfo] = useState({});

  //the returned gpa graph distribution for this course is converted into the required format for our graph API
  useEffect(() => {
    fetch("/graphDistribution/" + id).then((response) =>
      response.json().then((d) => {
        const json_str = JSON.stringify(d);
        const json = JSON.parse(json_str);
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
  }, []);

  //displaying a BAR graph
  return (
    <BarChart width={400} height={250} data={graphInfo}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />{" "}
      {/**XAxis displays the name label of each object in the array **/}
      <YAxis dataKey="grade" />{" "}
      {/**XAxis displays the grade label of each object in the array **/}
      <Tooltip />
      <Legend />
      <Bar dataKey="grade" fill="#FF7787" />
    </BarChart>
  );
};

export default GPAGraph;
