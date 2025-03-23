import { useQuery } from '@tanstack/react-query';

import { QUERY_KEYS } from '@/constants/queryKey';
import { getCommments } from '@/services/comment.service';

const useComments = () => {
	const { data } = useQuery({
		queryKey: [QUERY_KEYS[2]],
		queryFn: getCommments,
	});

	return data;
};

export default useComments;
