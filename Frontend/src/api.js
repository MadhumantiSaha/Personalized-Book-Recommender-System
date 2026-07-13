import axios from "axios";

const API_BASE = "http://localhost:8000/api";

export async function fetchMeta() {
  const res = await axios.get(`${API_BASE}/meta`);
  return res.data;
}

export async function getRecommendations({ query, category, tone }) {
  const res = await axios.post(`${API_BASE}/recommend`, { query, category, tone });
  return res.data.results;
}