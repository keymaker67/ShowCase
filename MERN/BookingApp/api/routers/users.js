import {
  deleteUser,
  getAllUsers,
  getOneUser,
  updateUser,
} from "../controllers/users.js";
import Router from "express";
import { verifyAdmin, verifyUser } from "../utils/verifyToken.js";

const router = Router();

router.route("/").get(verifyAdmin, getAllUsers);
router
  .route("/:id")
  .get(verifyUser, getOneUser)
  .patch(verifyUser, updateUser)
  .delete(verifyUser, deleteUser);

export default router;
