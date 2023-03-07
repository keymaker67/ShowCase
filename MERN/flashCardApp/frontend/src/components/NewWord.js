import { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Table from "react-bootstrap/Table";
import axios from "axios";

const NewWord = () => {
  const [flashCard, setFlashCard] = useState({
    word: "",
    definition: "",
  });
  const [reverseFlashCard, setReverseFlashCard] = useState({
    word: "",
    definition: "",
  });
  const [newWord, setNewWord] = useState(null);
  const [reverseNewwWord, setReverseNewWord] = useState(null);

  const handleChange = (e) => {
    // setFlashCard((perv) => ({ ...perv, [e.target.id]: e.target.value }));
    setReverseFlashCard((perv) => ({
      ...perv,
      [e.target.id === "word" ? "definition" : "word"]: e.target.value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post("/words", flashCard)
      .then((res) => {
        setNewWord(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    axios
      .post("/words", reverseFlashCard)
      .then((res) => {
        setReverseNewWord(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    setFlashCard({ word: "", definition: "" });
    setReverseFlashCard({ word: "", definition: "" });
    const inputWord = document.getElementById("word");
    inputWord.value = "";
    document.getElementById("definition").value = "";
    inputWord.focus();
  };

  return (
    <div>
      <Form onSubmit={handleSubmit} className="mb-5">
        <Form.Group className="mb-3" controlId="word">
          <Form.Label>New word</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter new word"
            onChange={handleChange}
            autoComplete="off"
          />
        </Form.Group>
        <Form.Group className="mb-3" controlId="definition">
          <Form.Label>Definition</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter definition"
            onChange={handleChange}
            autoComplete="off"
          />
        </Form.Group>
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
      <Table responsive striped variant="warning">
        <thead>
          <tr>
            <th>#</th>
            <th>Word</th>
            <th>Definition</th>
            <th>Stage</th>
          </tr>
        </thead>
        <tbody>
          {newWord && (
            <tr key={newWord._id}>
              <th>{1}</th>
              <th>{newWord.word}</th>
              <th>{newWord.definition}</th>
              <th>{newWord.stage}</th>
            </tr>
          )}
          {reverseNewwWord && (
            <tr key={reverseNewwWord._id}>
              <th>{1}</th>
              <th>{reverseNewwWord.word}</th>
              <th>{reverseNewwWord.definition}</th>
              <th>{reverseNewwWord.stage}</th>
            </tr>
          )}
        </tbody>
      </Table>
    </div>
  );
};

export default NewWord;
