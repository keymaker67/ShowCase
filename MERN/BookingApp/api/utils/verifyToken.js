import { StatusCodes } from "http-status-codes";
import createError from "./error.js";
import jwt from "jsonwebtoken";

export const verifyToken = (req, res, next) => {
  const token = req.cookies.access_token;
  if (!token)
    return next(
      createError(StatusCodes.UNAUTHORIZED, "You are not authenticated!")
    );
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err)
      return next(createError(StatusCodes.FORBIDDEN, "Token is not valid!"));
    req.user = user;
  });
};

export const verifyUser = (req, res, next) => {
  verifyToken(req, res, next);
  if (req.user.id === req.params.id || req.user.isAdmin) {
    next();
  } else {
    return next(createError(StatusCodes.FORBIDDEN, "You are not authorized!"));
  }
};

export const verifyAdmin = (req, res, next) => {
  verifyToken(req, res, next);
  if (req.user.isAdmin) {
    next();
  } else {
    return next(createError(StatusCodes.FORBIDDEN, "You are not authorized!"));
  }
};
