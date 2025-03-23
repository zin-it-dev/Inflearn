import { createContext } from 'react';

import { Courses } from '@/types/course.type';

const CourseContext = createContext<Courses | undefined>(undefined);

export default CourseContext;
