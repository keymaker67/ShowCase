import {
  createRoom,
  deleteRoom,
  getAllRooms,
  getOneRoom,
  updateRoom,
} from "../controllers/rooms.js";
import Router from "express";
import { verifyAdmin } from "../utils/verifyToken.js";

const router = Router();

router.route("/").get(getAllRooms);
router.route("/:hotelid").post(verifyAdmin, createRoom);
router.route("/:id").get(getOneRoom).patch(verifyAdmin, updateRoom);
router.delete("/:id/:hotelid", verifyAdmin, deleteRoom);
export default router;
