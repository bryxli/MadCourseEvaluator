import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";

// Reddit: This component shows Reddit comments about a certain class, using
//    comment specified by redditList
// This component is used by Course
const Reddit = ({ redditList }) => {
  return (
    <>
      {redditList && redditList.length > 0 ? (
        <Container>
          <Row className="reddit-box-header">
            <img
              height="124px"
              width="220px"
              src="/Reddit.png"
              alt="reddit-logo"
            />
          </Row>

          <Row className="reddit-box-body">
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
          </Row>
        </Container>
      ) : (
        <></>
      )}
    </>
  );
};

export default Reddit;
