import React, { useState } from "react";
import { Typeahead } from "react-bootstrap-typeahead";

const Search = () => {
  const [selected, setSelected] = useState([]);

  const options = ["CS 300", "CS 506", "CS 577"];

  return (
    <Typeahead
      id="basic-example"
      onChange={setSelected}
      options={options}
      placeholder="Course or Instructor name"
      selected={selected}
    />
  );
};

export default Search;
