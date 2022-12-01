import User from "../models/user.js";
import { Strategy as localStrategy } from "passport-local";

export default (passport) => {
  passport.use(
    new localStrategy({ usernameField: "email" }, (email, password, done) => {
      User.findOne({ email: email })
        .then(async (user) => {
          if (!user) {
            return done(null, false, {
              message: "That email is not registered!",
            });
          }
          const isPasswordCorrect = await user.comparePassword(password);
          if (isPasswordCorrect) {
            return done(null, user);
          }
          return done(null, false, { message: "Password incorrect" });
        })
        .catch((err) => {
          console.log(err);
        });
    })
  );
  passport.serializeUser((user, done) => {
    done(null, user.id);
  });
  passport.deserializeUser((id, done) => {
    User.findById(id, (err, user) => {
      done(err, user);
    });
  });
};
