import {
  createHotel,
  deleteHotel,
  getAllHotels,
  getOneHotel,
  updateHotel,
  countByCity,
  countByType,
} from "../controllers/hotels.js";
import Router from "express";
import { verifyAdmin } from "../utils/verifyToken.js";

const router = Router();

router.route("/").get(getAllHotels).post(verifyAdmin, createHotel);
router.get("/countByCity", countByCity);
router.get("/countByType", countByType);

router
  .route("/find/:id")
  .get(getOneHotel)
  .patch(verifyAdmin, updateHotel)
  .delete(verifyAdmin, deleteHotel);

export default router;
