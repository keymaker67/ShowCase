import { StatusCodes } from "http-status-codes";
import User from "../models/User.js";
import createError from "../utils/error.js";

export const register = async (req, res, next) => {
  try {
    const newUser = await User.create(req.body);
    res.status(StatusCodes.CREATED).json({ msg: "User has been created" });
  } catch (error) {
    next(error);
  }
};

export const login = async (req, res, next) => {
  try {
    const user = await User.findOne({ username: req.body.username });
    if (!user) {
      return next(createError(StatusCodes.NOT_FOUND, "User not found!"));
    }
    const passwordVerified = await user.comparePassword(req.body.password);
    if (!passwordVerified)
      return next(
        createError(StatusCodes.BAD_REQUEST, "password is incorrect")
      );
    const { password, isAdmin, ...otherDetails } = user._doc;
    const token = await user.createJWT();
    res
      .cookie("access_token", token, { httpOnly: true })
      .status(StatusCodes.OK)
      .json({ ...otherDetails });
  } catch (error) {
    console.log(error);
    next(error);
  }
};
