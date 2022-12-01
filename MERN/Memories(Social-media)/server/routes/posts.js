import { Router } from "express";
import {
  createPost,
  deletePost,
  getAllPosts,
  getPost,
  updatePost,
  likePost,
} from "../controllers/posts.js";

export const router = Router();

router.route("/").get(getAllPosts).post(createPost);
router.route("/:id").get(getPost).delete(deletePost).patch(updatePost);
router.route("/:id/likePost").patch(likePost);
