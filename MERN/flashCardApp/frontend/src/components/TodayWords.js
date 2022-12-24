import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import Carousel from "react-bootstrap/Carousel";
import Accordion from "react-bootstrap/Accordion";
import CostumToggle from "./CustomToggle";
import Badge from "react-bootstrap/Badge";

import useStageUpdater from "./hooks/useStageUpdater";
import axios from "axios";

const TodayWords = () => {
  const { flashCards, loading } = useStageUpdater("/words");

  async function handleKnewButton(e, id, i) {
    if (e.target.value === "Know") {
      await axios.patch(`/words/${id}`, {
        $inc: { stage: 1 },
        last_review_date: new Date().getTime(),
      });
    } else {
      await axios.patch(`/words/${id}`, {
        $inc: { stage: -1 },
        last_review_date: new Date().getTime(),
      });
    }
    flashCards.splice(i);
  }

  return (
    <Card className="text-center" bg="warning">
      <Card.Header>
        {flashCards && flashCards.length > 0 ? (
          <div>
            <span style={{ fontSize: "40px" }}>Here you are, Have fun!</span>
            <Badge bg="danger">{flashCards.length}</Badge>
          </div>
        ) : (
          <span style={{ fontSize: "40px" }}>No words today!</span>
        )}
      </Card.Header>
      <Card.Body>
        <Carousel indicators={false} interval={null}>
          {loading ? (
            <span>Loading</span>
          ) : (
            flashCards &&
            flashCards.map((flashCard, i) => (
              <Carousel.Item key={flashCard._id}>
                <Accordion>
                  <Card bg="info">
                    <Card.Header>
                      <h2>{flashCard.word}</h2>
                      <CostumToggle eventKey="0" className="ms-auto">
                        Click to see the definintion
                      </CostumToggle>
                    </Card.Header>
                    <Accordion.Collapse eventKey="0">
                      <Card.Body>
                        <h3>{flashCard.definition}</h3>
                      </Card.Body>
                    </Accordion.Collapse>
                    <Card.Text className="py-5">
                      <Button
                        value={"Know"}
                        style={{ width: "20vw" }}
                        onClick={(e) => handleKnewButton(e, flashCard._id, i)}
                        className="me-2"
                      >
                        I knew it
                      </Button>
                      <Button
                        value={"DKnow"}
                        style={{ width: "20vw" }}
                        onClick={(e) => handleKnewButton(e, flashCard._id, i)}
                      >
                        Lets practice more
                      </Button>
                    </Card.Text>
                    <Card.Footer className="text-muted">
                      <h4>{flashCard.stage}</h4>
                    </Card.Footer>
                  </Card>
                </Accordion>
              </Carousel.Item>
            ))
          )}
        </Carousel>
      </Card.Body>
    </Card>
  );
};

export default TodayWords;
