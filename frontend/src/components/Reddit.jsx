import React, { useEffect, useState } from "react";

const Reddit = (props) => {
  const id = props.id;

  const [redditList, setRedditList] = useState([]);
  useEffect(() => {
    fetch("/reddit-comments/" + id).then((response) =>
      response.json().then((data) => {
        const json_str = JSON.stringify(data);
        const json = JSON.parse(json_str);
        var classes = [];
        for (var key in json) {
          const id = key;
          const body = json[key].comBody;
          const link = json[key].comLink;
          const votes = json[key].comVotes;

          classes.push({ id, body, link, votes });
        } //this converts the JSON object of reddit threads into an array
        classes.sort((a, b) => {
          return b.votes - a.votes;
        }); //sorting in descending order based on upvotes
        setRedditList(classes);
      })
    );
  }, []);

  return (
    <div className="reddit-box-body">
      {redditList.map((thread) => (
        <p
          onClick={() => {
            window.open(thread.link, "_blank");
          }}
          className="reddit-list-item"
          key={thread.id}
        >
          {thread.body}
        </p>
      ))}
    </div>
  );
};

export default Reddit;
