import React, { useState } from "react";
import { Typeahead } from "react-bootstrap-typeahead";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

const Search = () => {
  const [selected, setSelected] = useState([]);
  const options = ["CS 300", "CS 506", "CS 577"];

  return (
    <Form method="post">
      <Form.Label>Search</Form.Label>
      <Typeahead
        id="search"
        onChange={setSelected}
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
