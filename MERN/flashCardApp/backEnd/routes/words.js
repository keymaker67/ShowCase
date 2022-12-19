// import { Router as router } from "express";
import express from "express";
const router = express.Router();
import {
  getWords,
  getWord,
  updateWord,
  createWord,
  deleteWord,
} from "../controllers/words.js";

router.route("/").get(getWords).post(createWord);
router.route("/:id").get(getWord).patch(updateWord).delete(deleteWord);

export default router;
