import React, { useEffect, useState } from "react";
import { Typeahead } from "react-bootstrap-typeahead";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { createSearchParams, useNavigate } from "react-router-dom";

const Search = () => {
  // Initialize class list
  const [classList, setClassList] = useState([]);
  useEffect(() => {
    fetch("/all-courses").then((response) =>
      response.json().then((data) => {
        const json_str = JSON.stringify(data);
        const json = JSON.parse(json_str);
        var classes = [];
        for (var key in json) {
          const code = json[key].cCode;
          const name = json[key].cName;
          const id = json[key].cUID;
          const classFull = {
            code: code,
            name: name,
            id: id,
          };
          classes.push(classFull);
        }
        setClassList(classes);
      })
    );
  }, []);

  const [selected, setSelected] = useState([]);
  const options = classList;

  // Submit button navigation
  const navigate = useNavigate();
  const submit = (e) => {
    e.preventDefault();
    navigate({
      pathname: "/course",
      search: createSearchParams({
        id: selected[0].id,
      }).toString(),
    });
  };

  return (
    <Form onSubmit={submit}>
      <Form.Group>
        <Typeahead
          id="search"
          onChange={setSelected}
          labelKey={(option) => `${option.code} - ${option.name}`}
          options={options}
          placeholder="Course (Ex: CS300)"
          selected={selected}
        />
      </Form.Group>
      <Button type="submit" hidden></Button>
    </Form>
  );
};

export default Search;
