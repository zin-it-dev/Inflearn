import axios from '@/configs/axios';
import ENDPOINTS from '@/constants/endpoints';
import { Comment } from '@/types/comment.type';

export const getCommments = async (): Promise<Comment[] | undefined> => {
	try {
		const response = await axios.get(ENDPOINTS['comments']);
		return response.data;
	} catch (error) {
		console.error('Error fetching comments', error);
	}
};
