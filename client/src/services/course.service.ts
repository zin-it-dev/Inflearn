import axios from '@/configs/axios';
import ENDPOINTS from '@/constants/endpoints';
import { Courses } from '@/types/course.type';

export const getCourses = async (
	keyword?: string,
	category?: string,
): Promise<Courses | undefined> => {
	try {
		const response = await axios.get(ENDPOINTS['courses'](keyword, category));
		return response.data;
	} catch (error) {
		console.error('Error fetching courses', error);
	}
};
