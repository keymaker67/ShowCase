import express from "express";
import dotenv from "dotenv";
import { connect } from "mongoose";
import userRouter from "./routers/users.js";
import roomRouter from "./routers/rooms.js";
import hotelRouter from "./routers/hotels.js";
import authRouter from "./routers/auth.js";
import { StatusCodes } from "http-status-codes";
import cookieParser from "cookie-parser";

dotenv.config();
const app = express();

app.use(express.json());
app.use(cookieParser());

app.use("/rooms", roomRouter);
app.use("/users", userRouter);
app.use("/hotels", hotelRouter);
app.use("/auth", authRouter);

app.use((err, req, res, next) => {
  const errorStatus = err.status || StatusCodes.INTERNAL_SERVER_ERROR;
  const errorMessage = err.message || "Somthing went wrong please try agian";
  return res.status(errorStatus).json({
    success: false,
    status: errorStatus,
    message: errorMessage,
    stack: err.stack,
  });
});

const port = process.env.PORT || 5000;

const connectDB = async () => {
  await connect(process.env.MONGO_URI)
    .then(() => console.log("DB connected"))
    .catch((error) => {
      console.log(error);
    });
};

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
  connectDB();
});
