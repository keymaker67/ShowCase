import {
  createHotel,
  deleteHotel,
  getAllHotels,
  getOneHotel,
  updateHotel,
} from "../controllers/hotels.js";
import Router from "express";
import { verifyAdmin } from "../utils/verifyToken.js";

const router = Router();

router.route("/").get(getAllHotels).post(verifyAdmin, createHotel);
router
  .route("/:id")
  .get(getOneHotel)
  .patch(verifyAdmin, updateHotel)
  .delete(verifyAdmin, deleteHotel);

export default router;
