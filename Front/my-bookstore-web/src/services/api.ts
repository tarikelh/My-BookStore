import axios from 'axios';

const api = axios.create({
    baseURL: process.env.NEXT_API_BASE_URL,
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*", 
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
        "Cache-Control": "no-cache, no-store"
    },
});

export default api;