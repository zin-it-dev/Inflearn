import { useQuery } from '@tanstack/react-query';
import { useSearchParams } from 'react-router';

import { getCourses } from '@/services/course.service';
import { QUERY_KEYS } from '@/constants/queryKey';

const useCourses = () => {
	const [searchParams] = useSearchParams();

	const keyword = searchParams.get('keyword') || '';
	const category = searchParams.get('category') || '';

	const { data } = useQuery({
		queryKey: [QUERY_KEYS[1], keyword, category],
		queryFn: () => getCourses(keyword, category),
	});

	return data;
};

export default useCourses;
