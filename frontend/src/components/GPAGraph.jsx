import React from "react";
import {
  BarChart,
  CartesianGrid,
  YAxis,
  XAxis,
  Tooltip,
  Legend,
  Bar,
} from "recharts";

/**
 * GPAGraph: displays a BAR graph based on info passed in through graphInfo
 * This component is used by Course
 * @param {*} graphInfo data to be displayed in graph, determined in Course
 * @returns GPAGraph React element
 */
const GPAGraph = ({ graphInfo }) => {
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
