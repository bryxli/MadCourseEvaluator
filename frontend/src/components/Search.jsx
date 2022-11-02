import React, { useEffect, useState } from "react";
import { Typeahead } from "react-bootstrap-typeahead";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

const Search = () => {
  // Initialize class list
  const [classList, setClassList] = useState([]);
  useEffect(() => {
    fetch("/").then((response) =>
      response.json().then((data) => {
        setClassList(data);
      })
    );
  }, []);

  const [selected, setSelected] = useState([]);
  classList;
  // const options = classList;
  const options = [
    // Temp data
    { id: "CS 506", name: "Software Engineering" },
    { id: "CS 577", name: "Introduction to Algorithms" },
  ];

  return (
    <Form action="/course" method="GET">
      <Typeahead
        id="search"
        onChange={setSelected}
        labelKey={(option) => `${option.id} - ${option.name}`}
        options={options}
        placeholder="Course or Instructor name"
        selected={selected}
      />
      <Button type="submit" hidden>
        Submit
      </Button>
    </Form>
  );
};

export default Search;
