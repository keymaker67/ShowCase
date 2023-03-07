import { Schema, model } from "mongoose";

const wordSchema = new Schema(
  {
    word: {
      type: String,
      required: [true, "Please provide word"],
      unique: [true, "This word already exists"],
    },
    definition: {
      type: String,
      required: [true, "Please provide definition"],
    },
    stage: {
      type: Number,
      default: 1,
    },
    last_review_date: {
      type: Number,
      default: new Date().getTime(),
    },
  },
  { timestamps: true }
);

export default model("Word", wordSchema);
