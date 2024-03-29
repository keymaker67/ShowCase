import { StatusCodes } from "http-status-codes";
import Hotel from "../models/Hotel.js";

export const getAllHotels = async (req, res, next) => {
  const { min, max, ...others } = req.query;
  try {
    const hotels = await Hotel.find({
      ...others,
      cheapestPrice: { $gt: min || 1, $lt: max || 999 },
    })
    .limit(req.query.limit);
    res.status(StatusCodes.OK).json(hotels);
  } catch (error) {
    next(error);
  }
};

export const countByCity = async (req, res, next) => {
  const cities = req.query.cities.split(",");
  try {
    const list = await Promise.all(
      cities.map((city) => {
        return Hotel.countDocuments({ city: city });
      })
    );
    res.status(StatusCodes.OK).json(list);
  } catch (error) {
    next(error);
  }
};

export const countByType = async (req, res, next) => {
  const types = ["hotel", "apartment", "resort", "villa", "cabin"];
  try {
    const list = await Promise.all(
      types.map(async (type) => {
        const number = await Hotel.countDocuments({ type: type });
        return {
          type: type,
          count: number,
        };
      })
    );
    res.status(StatusCodes.OK).json(list);
  } catch (error) {
    next(error);
  }
};

export const getOneHotel = async (req, res, next) => {
  try {
    const hotel = await Hotel.findById(req.params.id);
    res.status(StatusCodes.OK).json(hotel);
  } catch (error) {
    next(error);
  }
};

export const createHotel = async (req, res, next) => {
  try {
    const newHotel = await Hotel.create(req.body);
    res.status(StatusCodes.CREATED).json(newHotel);
  } catch (error) {
    next(error);
  }
};

export const updateHotel = async (req, res, next) => {
  try {
    const updatedHotel = await Hotel.findByIdAndUpdate(
      req.params.id,
      req.body,
      {
        new: true,
      }
    );
    res.status(StatusCodes.OK).json(updatedHotel);
  } catch (error) {
    next(error);
  }
};

export const deleteHotel = async (req, res, next) => {
  try {
    await Hotel.findByIdAndDelete(req.params.id);
    res.status(StatusCodes.OK).json({ msg: "Hotel deleted" });
  } catch (error) {
    next(error);
  }
};
