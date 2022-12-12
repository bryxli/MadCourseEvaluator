import React, { useEffect, useState } from "react";
import { Typeahead } from "react-bootstrap-typeahead";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { useNavigate } from "react-router-dom";

/**
 * Search: search bar for users to search by course or instructor
 * This component is used by Home and Course (previously also Header)
 * @returns Search React element
 */
const Search = () => {
  // Initialize class list and professor list
  const [classList, setClassList] = useState([]);
  const [profList, setProfList] = useState([]);

  // useEffect hook to fetch the data from the API
  useEffect(() => {
    // fetch class data from host
    fetch("http://3.145.22.97/all-courses").then((response) =>
      response.json().then((json) => {
        var classes = [];
        // for each class get their course code, name, and course ID
        for (var key in json) {
          const code = json[key].cCode;
          const name = json[key].cName;
          const id = json[key].cUID;
          // concatenate class code and name so that either can be used in search
          const classFull = {
            result: code.concat(" - " + name),
            id: id,
          };
          classes.push(classFull);
        }
        setClassList(classes); // set the class state as the classes array
      })
    );
    // fetch professor data from host
    fetch("http://3.145.22.97/all-profs").then((response) =>
      response.json().then((json) => {
        var professors = [];
        // for each professor get their name and professor ID
        for (var key in json) {
          const name = json[key].name;
          const id = key;
          const professorFull = {
            result: name,
            id: id,
          };
          professors.push(professorFull); // push the new object to the professors array
        }
        setProfList(professors); // set the professorList state as the profList array
      })
    );
  }, []);

  // make search options classList and profList
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
          placeholder="Course or Professor (Ex: CS300)"
          selected={selected}
        />
      </Form.Group>
      <Button type="submit" hidden></Button>
    </Form>
  );
};

export default Search;
