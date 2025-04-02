export const BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000';

export const ENDPOINTS = {
	categories: import.meta.env.VITE_API_CATEGORY,
	courses: import.meta.env.VITE_API_COURSE,
	token: '/auth/token/',
};
