import axios from 'axios';

const BASE_URL = import.meta.env.VITE_SOME_KEY || 'http://127.0.0.1:5000/';

export default axios.create({
	baseURL: BASE_URL,
	headers: {
		'Content-type': 'application/json',
	},
	timeout: 3000,
});
