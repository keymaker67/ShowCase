import { model, Schema } from "mongoose";
import bcrypt from "bcryptjs";
import createError from "../utils/error.js";
import { StatusCodes } from "http-status-codes";
import jwt from "jsonwebtoken";
const UserSchema = new Schema(
  {
    username: {
      type: String,
      required: true,
      unique: true,
    },
    email: {
      type: String,
      required: true,
      unique: true,
    },
    password: {
      type: String,
      required: true,
    },
    isAdmin: {
      type: Boolean,
      default: false,
    },
  },
  { timestamps: true }
);

UserSchema.pre("save", async function (next) {
  try {
    this.password = await bcrypt.hashSync(this.password, 10);
  } catch (error) {
    next(
      createError(
        StatusCodes.CONFLICT,
        "Something went wrong with hash password"
      )
    );
  }
});

UserSchema.methods.comparePassword = async function (candidatePassword, next) {
  try {
    return await bcrypt.compare(candidatePassword, this.password);
  } catch (error) {
    next(
      createError(
        StatusCodes.CONFLICT,
        "Something went wrong with compare password"
      )
    );
  }
};

UserSchema.methods.createJWT = async function (next) {
  try {
    const token = jwt.sign(
      { id: this._id, isAdmin: this.isAdmin },
      process.env.JWT_SECRET
    );
    return token;
  } catch (error) {
    next(
      createError(
        StatusCodes.CONFLICT,
        "Something went wrong with creatind JWT"
      )
    );
  }
};

export default model("User", UserSchema);
