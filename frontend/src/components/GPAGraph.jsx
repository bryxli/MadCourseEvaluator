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

/**const data = [
  {
    name: "A",
    grade: 13,
  },
  {
    name: "B",
    grade: 20,
  },
  {
    name: "C",
    grade: 17,
  },
  {
    name: "D",
    grade: 9,
  },
  {
    name: "F",
    grade: 2,
  },
];**/

const GPAGraph = ({ graphInfo }) => {
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

  return (
    <BarChart width={400} height={250} data={graphInfo}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis dataKey="grade" />
      <Tooltip />
      <Legend />
      <Bar dataKey="grade" fill="#FF7787" />
    </BarChart>
  );
};

export default GPAGraph;
