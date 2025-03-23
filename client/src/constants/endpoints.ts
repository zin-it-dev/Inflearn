const ENDPOINTS = {
	categories: import.meta.env.API_CATEGORIES_URL,
	courses: (keyword?: string, category?: string) => {
		let url = `${import.meta.env.VITE_API_COURSES_URL}?`;

		if (keyword) url += `keyword=${keyword}&`;
		if (category) url += `category=${category}`;

		return url.endsWith('&') ? url.slice(0, -1) : url;
	},
	comments: import.meta.env.VITE_API_COMMENTS_URL,
};

export default ENDPOINTS;
