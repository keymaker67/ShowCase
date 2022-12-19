import dotenv from "dotenv";
import { connect } from "mongoose";
import app from "./server.js";

dotenv.config();

const port = process.env.PORT;
const start = async () => {
  try {
    const options = {
      maxPoolSize: 10,
      serverSelectionTimeoutMS: 5000,
      socketTimeoutMS: 45000,
    };
    await connect(process.env.MONGO_URI, options);
    app.listen(port, () => {
      console.log(`server is listening on port ${port}`);
    });
  } catch (error) {
    console.log(error);
  }
};
start();
