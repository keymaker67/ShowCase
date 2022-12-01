import express from "express";
import dotenv from "dotenv";
import { router as indexRouter } from "./routes/index.js";
import { router as usersRouter } from "./routes/users.js";
import { connect } from "mongoose";
import expressEjsLayouts from "express-ejs-layouts";
import session from "express-session";
import flash from "connect-flash";
import passport from "passport";
import localStrategy from "./config/passport.js";

dotenv.config();
localStrategy(passport);

const app = express();

//  Middlewares
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(
  session({
    secret: "secret",
    resave: true,
    saveUninitialized: true,
  })
);
app.use(passport.initialize());
app.use(passport.session());
app.use(flash());
app.use((req, res, next) => {
  res.locals.success_msg = req.flash("success_msg");
  res.locals.error_msg = req.flash("error_msg");
  res.locals.error = req.flash("error");
  next();
});

//  EJS
app.use(expressEjsLayouts);
app.set("view engine", "ejs");

//  Routes
app.use("/", indexRouter);
app.use("/users", usersRouter);

const port = 3000 || process.env.PORT;

const start = async () => {
  try {
    await connect(process.env.MONGO_URI);
    app.listen(port, () => {
      console.log(`Server listening on ${port} ... `);
    });
  } catch (error) {
    console.log(error);
  }
};
start();
