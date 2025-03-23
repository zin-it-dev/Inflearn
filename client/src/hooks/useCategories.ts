import { useQuery } from '@tanstack/react-query';

import { QUERY_KEYS } from '@/constants/queryKey';
import { getCategories } from '@/services/category.service';

const useCategories = () => {
	const { data } = useQuery({
		queryKey: [QUERY_KEYS[0]],
		queryFn: getCategories,	
	});

	return data;
};

export default useCategories;
