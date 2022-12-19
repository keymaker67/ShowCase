import express from "express";
import cors from "cors";
import "express-async-errors";
import { errorHandler } from "./middlewares/errorHandler.js";
import { notFound } from "./middlewares/notFound.js";
import wordsRouter from "./routes/words.js";
// import path from "path";

//express app
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cors());
//  set static folder
// const __dirname = path.resolve();
// app.use(express.static(path.join(__dirname, "public")));

app.use("/api/words", wordsRouter);

app.use(errorHandler);
app.use(notFound);

export default app;
