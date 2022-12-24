// Components
import NewWord from "../components/NewWord";
import Tab from "react-bootstrap/Tab";
import Tabs from "react-bootstrap/Tabs";
import { useState } from "react";
import AllWords from "../components/AllWords";
import TodayWords from "../components/TodayWords";

const Home = () => {
  const [key, setKey] = useState("todayWords");
  return (
    <Tabs
      id="controlled-tab-example"
      activeKey={key}
      onSelect={(k) => setKey(k)}
      className="my-3"
    >
      <Tab eventKey="todayWords" title="Today words">
        <TodayWords />
      </Tab>
      <Tab eventKey="newWord" title="New word">
        <NewWord />
      </Tab>
      <Tab eventKey="allWords" title="All words">
        <AllWords />
      </Tab>
    </Tabs>
  );
};

export default Home;
