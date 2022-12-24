import useFetch from "./hooks/useFetch";
import Table from "react-bootstrap/Table";
const AllWords = () => {
  const { data, loading } = useFetch("/words");
  return (
    <div>
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
          {loading ? (
            <div>loading</div>
          ) : (
            data &&
            data.words.map((flashCard, i) => (
              <tr key={flashCard._id}>
                <th>{i + 1}</th>
                <th>{flashCard.word}</th>
                <th>{flashCard.definition}</th>
                <th>{flashCard.stage}</th>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    </div>
  );
};

export default AllWords;
