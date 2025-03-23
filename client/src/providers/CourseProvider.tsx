import { ReactNode } from 'react';

import CourseContext from '@/contexts/CourseContext';
import useCourses from '@/hooks/useCourses';

const CourseProvider = ({ children }: { children: ReactNode }) => {
	const data = useCourses();

	return <CourseContext.Provider value={data}>{children}</CourseContext.Provider>;
};

export default CourseProvider;
