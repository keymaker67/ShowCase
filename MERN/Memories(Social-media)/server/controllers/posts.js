import { StatusCodes } from "http-status-codes";
import mongoose from "mongoose";
import Post from "../models/post.js";

const getAllPosts = async (req, res) => {
  try {
    const posts = await Post.find();
    res.status(StatusCodes.OK).json(posts);
  } catch (error) {
    res.status(StatusCodes.NOT_FOUND).json({ msg: error });
  }
};

const getPost = async (req, res) => {
  try {
    const post = await Post.findOne();
    res.status(StatusCodes.OK).json({ msg: "get one post" });
  } catch (error) {
    res.status(StatusCodes.NOT_FOUND).json({ msg: error });
  }
};

const createPost = async (req, res) => {
  try {
    const newPost = await Post.create(req.body);
    res.status(StatusCodes.CREATED).json(newPost);
  } catch (error) {
    res.status(StatusCodes.CONFLICT).json({ msg: error });
  }
};

const updatePost = async (req, res) => {
  const { id } = req.params;
  const post = req.body;
  if (!mongoose.Types.ObjectId.isValid(id)) {
    return res.status(StatusCodes.NOT_FOUND).send("No post with that id");
  }
  try {
    const updatedPost = await Post.findByIdAndUpdate(id, post, { new: true });
    res.status(StatusCodes.OK).json(updatedPost);
  } catch (error) {
    console.log(error);
  }
};

const deletePost = async (req, res) => {
  const { id } = req.params;
  if (!mongoose.Types.ObjectId.isValid(id)) {
    return res.status(StatusCodes.NOT_FOUND).send("No post with that id");
  }
  try {
    await Post.findByIdAndDelete(id);
    res.status(StatusCodes.OK).json({ msg: "post deleted" });
  } catch (error) {
    console.log(error);
  }
};

const likePost = async (req, res) => {
  const { id } = req.params;
  if (!mongoose.Types.ObjectId.isValid(id)) {
    return res.status(StatusCodes.NOT_FOUND).send("No post with that id");
  }
  try {
    const post = await Post.findById(id);
    const updatedPost = await Post.findByIdAndUpdate(
      id,
      {
        likeCount: post.likeCount + 1,
      },
      { new: true }
    );
    res.status(StatusCodes.OK).json({ updatedPost });
  } catch (error) {
    console.log(error);
  }
};

export { getAllPosts, getPost, updatePost, createPost, deletePost, likePost };
