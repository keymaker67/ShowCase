import { StatusCodes } from "http-status-codes";
import Hotel from "../models/Hotel.js";
import Room from "../models/Room.js";
import createError from "../utils/error.js";

export const createRoom = async (req, res, next) => {
  try {
    const newRoom = await Room.create(req.body);
    await Hotel.findByIdAndUpdate(req.params.hotelid, {
      $push: { rooms: newRoom._id },
    });
    res.status(StatusCodes.CREATED).json(newRoom);
  } catch (error) {
    next(error);
  }
};

export const getAllRooms = async (req, res, next) => {
  try {
    const rooms = await Room.find();
    res.status(StatusCodes.OK).json(rooms);
  } catch (error) {
    next(error);
  }
};

export const getOneRoom = async (req, res, next) => {
  try {
    const room = await Room.findById(req.params.id);
    res.status(StatusCodes.OK).json(room);
  } catch (error) {
    next(error);
  }
};

export const updateRoom = async (req, res, next) => {
  try {
    const updatedRoom = await Room.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });
    res.status(StatusCodes.OK).json(updatedRoom);
  } catch (error) {
    next(error);
  }
};

export const deleteRoom = async (req, res, next) => {
  try {
    await Room.findByIdAndDelete(req.params.id);
    await Hotel.findByIdAndUpdate(req.params.hotelid, {
      $pull: { rooms: req.params.id },
    });
    res.status(StatusCodes.OK).json({ msg: "Room deleted" });
  } catch (error) {
    next(error);
  }
};
