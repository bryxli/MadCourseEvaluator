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
