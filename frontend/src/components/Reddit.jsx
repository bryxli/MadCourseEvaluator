import React from "react";

const data = [
  {
    link: "https://www.reddit.com/r/UWMadison/comments/sk50i0/where_should_i_go_and_what_should_i_do_for_help/hvix6dl/",
    body: "I\\u2019m not a CS major, but I\\u2019m pretty sure there\\u2019s a discord for CS 577 students",
    upvotes: 13,
    id: 1,
  },
  {
    link: "https://www.reddit.com/r/UWMadison/comments/sk50i0/where_should_i_go_and_what_should_i_do_for_help/hvix6dl/",
    body: "I\\u2019m not a CS major, but I\\u2019m pretty sure there\\u2019s a discord for CS 577 students",
    upvotes: 13,
    id: 1,
  },
  {
    link: "https://www.reddit.com/r/UWMadison/comments/sk50i0/where_should_i_go_and_what_should_i_do_for_help/hvix6dl/",
    body: "I\\u2019m not a CS major, but I\\u2019m pretty sure there\\u2019s a discord for CS 577 students",
    upvotes: 13,
    id: 1,
  },
  {
    link: "https://www.reddit.com/r/UWMadison/comments/sk50i0/where_should_i_go_and_what_should_i_do_for_help/hvix6dl/",
    body: "I\\u2019m not a CS major, but I\\u2019m pretty sure there\\u2019s a discord for CS 577 students",
    upvotes: 13,
    id: 1,
  },
];

const Reddit = () => {
  return (
    <>
      <div className="reddit-box-header">
        <img height="124px" width="220px" src="Reddit.png" />
      </div>
      <div className="reddit-box-body">
        {data.map((thread) => (
          <>
            <p
              onClick={() => {
                window.open(thread.link, "_blank");
              }}
              className="reddit-list-item"
              key={thread.id}
            >
              {thread.body}
            </p>
          </>
        ))}
      </div>
    </>
  );
};

export default Reddit;
