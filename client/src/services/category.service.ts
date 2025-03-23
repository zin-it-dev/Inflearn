import axios from '@/configs/axios';
import Category from '@/types/category.type';

export const getCategories = async (): Promise<Category[] | undefined> => {
	try {
		const response = await axios.get('/categories/');
		return response.data;
	} catch (error) {
		console.error('Error fetching posts', error);
	}
};
