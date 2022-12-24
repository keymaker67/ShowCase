import { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import axios from "axios";

const NewWord = () => {
  const [flashCard, setFlashCard] = useState({
    word: "",
    definition: "",
  });

  const handleChange = (e) => {
    setFlashCard((perv) => ({ ...perv, [e.target.id]: e.target.value }));
    console.log(flashCard);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newWord = axios.post("/words", flashCard);
    setFlashCard({ word: "", definition: "" });
    const inputWord = document.getElementById("word");
    inputWord.value = "";
    document.getElementById("definition").value = "";
    inputWord.focus();
    console.log(newWord);
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group className="mb-3" controlId="word">
        <Form.Label>New word</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter new word"
          onChange={handleChange}
        />
      </Form.Group>

      <Form.Group className="mb-3" controlId="definition">
        <Form.Label>Definition</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter definition"
          onChange={handleChange}
        />
      </Form.Group>
      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
};

export default NewWord;
