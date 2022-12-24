import useFetch from "./hooks/useFetch";
import Table from "react-bootstrap/Table";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import axios from "axios";
import { useEffect, useState } from "react";

const AllWords = () => {
  const { data, loading } = useFetch("/words?sort=stage");
  const [flashCards, setFlashCards] = useState(null);
  useEffect(() => {
    setFlashCards(data);
  }, [loading, data]);
  const [deletedWord, setDeletedWord] = useState(null);
  const [show, setShow] = useState(false);

  const deleteHandler = async (id) => {
    axios
      .delete(`/words/${id}`)
      .then((res) => {
        setDeletedWord(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    axios
      .get(`/words`)
      .then((res) => {
        setFlashCards(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    setShow(true);
  };

  return (
    <div>
      <Table responsive striped variant="warning">
        <thead>
          <tr>
            <th>#</th>
            <th>Word</th>
            <th>Definition</th>
            <th>Stage</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {loading ? (
            <tr>
              <th>loading</th>
              <th>loading</th>
              <th>loading</th>
              <th>loading</th>
              <th>loading</th>
            </tr>
          ) : (
            flashCards &&
            flashCards.words.map((flashCard, i) => (
              <tr key={flashCard._id}>
                <td>{i + 1}</td>
                <td>{flashCard.word}</td>
                <td>{flashCard.definition}</td>
                <td>{flashCard.stage}</td>
                <td>
                  <Button
                    variant="outline-danger"
                    onClick={() => deleteHandler(flashCard._id)}
                  >
                    <i className="bi bi-trash2-fill"></i>
                  </Button>
                  <Modal show={show} onHide={() => setShow(false)}>
                    <Modal.Header closeButton>
                      <p>this word is deleted:</p>
                    </Modal.Header>
                    <Modal.Body>
                      {deletedWord && <h3>{deletedWord.word}</h3>}
                    </Modal.Body>
                  </Modal>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    </div>
  );
};

export default AllWords;
