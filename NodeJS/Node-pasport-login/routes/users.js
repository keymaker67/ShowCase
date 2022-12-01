import { Router } from "express";
import passport from "passport";
import User from "../models/user.js";

export const router = Router();

// Login page
router.get("/login", (req, res) => {
  res.render("login");
});
//  Register page
router.get("/register", (req, res) => {
  res.render("register");
});
//  Register handle
router.post("/register", (req, res) => {
  const { name, email, password, password2 } = req.body;
  let errors = [];

  // Check required fields
  if (!name || !email || !password || !password2) {
    errors.push({ msg: "Please fill in all fields" });
  }

  //  Check password match
  if (password !== password2) {
    errors.push({ msg: "Passwords do not match" });
  }

  //  Check pass length
  if (password.length < 6) {
    errors.push({ msg: "password should be at least 6 characters" });
  }

  if (errors.length > 0) {
    res.render("register", {
      errors,
      name,
      email,
      password,
      password2,
    });
  } else {
    User.findOne({ email: email })
      .then(async (user) => {
        if (user) {
          errors.push({ msg: "This email is already taken" });
          res.render("register", {
            errors,
            name,
            email,
            password,
            password2,
          });
        } else {
          await User.create(req.body);
          req.flash("success_msg", "You are now registerd and can log in");
          res.redirect("/users/login");
        }
      })
      .catch((err) => console.log(err));
  }
});

router.post("/login", (req, res, next) => {
  passport.authenticate("local", {
    successRedirect: "/dashboard",
    failureRedirect: "/users/login",
    failureFlash: true,
  })(req, res, next);
});

router.get("/logout", (req, res, next) => {
  req.logout((err) => {
    if (err) {
      return next(err);
    }
    req.flash("success_msg", "You are logged out");
    res.redirect("/users/login");
  });
});
