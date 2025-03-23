import { useContext, useEffect, useState } from 'react';
import { Col, Row } from 'react-bootstrap';

import CourseContext from '@/contexts/CourseContext';
import { Course } from '@/types/course.type';
import Item from './Item';

const NewestCourses = () => {
	const context = useContext(CourseContext);
	const [courses, setCourses] = useState<Course[]>([]);

	useEffect(() => {
		if (context && context.results) {
			setCourses(context.results.slice(0, 10));
		}
	}, [context]);

	return (
		<section className='py-5'>
			<h2 className='text-lg-start text-md-start text-sm-center text-center mb-3'>
				Newest Courses
			</h2>
			{courses && courses.length > 0 ? (
				<Row
					lg={4}
					md={2}
					sm={1}
					xs={1}
					className='g-4'>
					{courses.map((course) => (
						<Col key={course.id}>
							<Item {...course} />
						</Col>
					))}
				</Row>
			) : (
				<p className='text-center fw-bold'>No courses available</p>
			)}
		</section>
	);
};

export default NewestCourses;
