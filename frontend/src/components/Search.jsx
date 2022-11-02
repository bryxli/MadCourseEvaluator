import React, { useEffect, useState } from "react";
import { Typeahead } from "react-bootstrap-typeahead";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useNavigate } from "react-router-dom";

const Search = () => {
  // Initialize class list
  const [classList, setClassList] = useState([]);
  useEffect(() => {
    fetch("/courselist").then((response) =>
      response.json().then((data) => {
        setClassList(data);
      })
    );
  }, []);

  const [selected, setSelected] = useState([]);
  const options = classList;

  // Submit button navigation
  let navigate = useNavigate();
  const submit = function submit() {
    navigate(`/course?id=${encodeURIComponent(selected[0].id)}`);
  };

  return (
    <Form onSubmit={submit}>
      <Form.Group>
        <Typeahead
          id="search"
          onChange={setSelected}
          labelKey={(option) => `${option.id} - ${option.name}`}
          options={options}
          placeholder="Course (Ex: CS 300)"
          selected={selected}
        />
      </Form.Group>
      <Button type="submit" hidden></Button>
    </Form>
  );
};

export default Search;
