import axios from "axios";

const clasificacionApi = axios.create({
  baseURL: "http://localhost:8000/clasificacion/api/clasificacion/",
});

export const getAllRanking = () => clasificacionApi.get("/");

export const createRanking = (ranking) =>
  clasificacionApi.post("/add", ranking);
