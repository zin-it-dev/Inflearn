import { Col, Row } from 'react-bootstrap';
import { Link } from 'react-router';
import { useContext } from 'react';
import Carousel from 'react-bootstrap/Carousel';

import CourseContext from '@/contexts/CourseContext';
import Item from '@/components/ui/Item';
import useComments from '@/hooks/useComments';
import Feedback from '@/components/ui/Feedback';
import { Comment } from '@/types/comment.type';
import NewestCourses from '@/components/ui/NewestCourses';

const Home = () => {
	const courses = useContext(CourseContext);

	const data = useComments();

	return (
		<>
			<section className='py-5 text-center'>
				<Row className='py-lg-5'>
					<Col
						lg={7}
						md={9}
						className='mx-auto'>
						<h1 className='display-4 fw-bold text-center'>
							Welcome to Inflearn 인프런 🎓
						</h1>
						<p className='lead text-body-secondary'>
							Learn from top experts. Discover thousands
							of high-quality courses to enhance your
							skills!
						</p>
						<p>
							<Link
								to={'/collection'}
								className='btn btn-warning btn-lg my-2'>
								Get Started
							</Link>
							<Link
								to={'/supports'}
								className='btn btn-primary btn-lg my-2'>
								Supports Us
							</Link>
						</p>
					</Col>
				</Row>
			</section>

			<NewestCourses />

			<div className='py-5'>
				<h2 className='text-lg-start text-md-start text-sm-center text-center mb-3'>
					All Courses
				</h2>

				{courses?.results && courses.results.length > 0 ? (
					<Row
						lg={4}
						md={2}
						sm={1}
						xs={1}
						className='g-4'>
						{courses.results.map((course) => (
							<Col key={course.id}>
								<Item {...course} />
							</Col>
						))}
					</Row>
				) : (
					<p className='text-center fw-bold'>No courses available</p>
				)}
			</div>

			<div className='py-5'>
				<h2 className='text-lg-start text-md-start text-sm-center text-center mb-3'>
					Feedbacks
				</h2>

				<Carousel>
					{data?.map((comment: Comment) => (
						<Carousel.Item
							interval={1000}
							key={comment.id}>
							<Feedback {...comment} />
						</Carousel.Item>
					))}
				</Carousel>
			</div>
		</>
	);
};

export default Home;
