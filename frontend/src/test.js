const fetch = require("node-fetch");

fetch("http://3.145.22.97/all-courses").then((response) =>
  response.json().then((json) => {
    console.log(json);
  })
);
