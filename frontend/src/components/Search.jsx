import React, { useEffect, useState } from "react";
import { Typeahead } from "react-bootstrap-typeahead";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useNavigate } from "react-router-dom";

const Search = () => {
  // Initialize class list
  const [classList, setClassList] = useState([]);
  const [profList, setProfList] = useState([]);
  useEffect(() => {
    fetch("http://3.145.22.97/all-courses").then((response) =>
      response.json().then((json) => {
        var classes = [];
        for (var key in json) {
          const code = json[key].cCode;
          const name = json[key].cName;
          const id = json[key].cUID;
          const classFull = {
            result: code.concat(" - " + name),
            id: id,
          };
          classes.push(classFull);
        }
        setClassList(classes);
      })
    );
    fetch("http://3.145.22.97/all-profs").then((response) =>
      response.json().then((json) => {
        var professors = [];
        for (var key in json) {
          const name = json[key].name;
          const id = key;
          const professorFull = {
            result: name,
            id: id,
          };
          professors.push(professorFull);
        }
        setProfList(professors);
      })
    );
  }, []);

  const [selected, setSelected] = useState([]);
  const options = classList.concat(profList);

  // Submit button navigation
  const navigate = useNavigate();

  const submit = (e) => {
    e.preventDefault();
    if (classList.includes(selected[0])) {
      navigate({
        pathname: `/course/${selected[0].id}`,
      });
    } else if (profList.includes(selected[0])) {
      navigate({
        pathname: `/instructor/${selected[0].id}`,
      });
    }
    window.location.reload(true);
  };

  return (
    <Form onSubmit={submit}>
      <Form.Group>
        <Typeahead
          id="search"
          onChange={setSelected}
          labelKey={(option) => option.result}
          options={options}
          placeholder="Course or Professor (Ex: COMP SCI 300)"
          selected={selected}
        />
      </Form.Group>
      <Button type="submit" hidden></Button>
    </Form>
  );
};

export default Search;
