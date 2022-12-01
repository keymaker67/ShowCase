import { Router } from "express";
import ensureAuthenticated from "../config/auth.js";

export const router = Router();

router.get("/", (req, res) => {
  res.render("welcome");
});

router.get("/dashboard", ensureAuthenticated, (req, res) => {
  res.render("dashboard", {
    name: req.user.name,
  });
});
