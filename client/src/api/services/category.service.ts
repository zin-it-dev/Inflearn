import { isAxiosError } from 'axios';

import { Category } from '@/types/category.type';
import { ENDPOINTS } from '@/utils/constants/endpoints';
import { axiosInstance } from '@/api/configs/axios';

export const fetchCategories = async (): Promise<Category[]> => {
	try {
		const response = await axiosInstance.get<Category[]>(ENDPOINTS.categories);

		if (response) {
			return response.data ?? [];
		}
		throw new Error('Data is undefined');
	} catch (error) {
		if (isAxiosError(error)) {
			console.error('Failed to fetch categories', error);
		}
		return [];
	}
};
