import React, { useEffect, useState } from "react";

const Reddit = (props) => {
  const id = props.id;

  const [redditList, setRedditList] = useState([]);
  useEffect(() => {
    fetch("/reddit-comments/" + id).then((response) =>
      response.json().then((json) => {
        var comments = [];
        for (var key in json) {
          const id = key;
          const body = json[key].comBody;
          const link = json[key].comLink;
          const votes = json[key].comVotes;

          comments.push({ id, body, link, votes });
        } // This converts the JSON object of reddit threads into an array
        comments.sort((a, b) => {
          return b.votes - a.votes;
        }); // Sorting in descending order based on upvotes
        setRedditList(comments);
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
