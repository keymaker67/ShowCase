import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import bodyParser from "body-parser";
import { connect } from "mongoose";
import { router as postRouter } from "./routes/posts.js";

dotenv.config();

const app = express();

app.use(bodyParser.json({ limit: "30mb", extended: true }));
app.use(bodyParser.urlencoded({ limit: "30mb", extended: true }));
app.use(cors());

app.use("/posts", postRouter);

const port = process.env.PORT || 5000;

connect(process.env.MONGO_URI)
  .then(() => {
    app.listen(port, () => console.log(`Server is litening on port ${port}`));
  })
  .catch((err) => {
    console.log(err.message);
  });
