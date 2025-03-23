import Card from 'react-bootstrap/Card';
import { ButtonGroup } from 'react-bootstrap';
import { Link } from 'react-router';

import { Course } from '@/types/course.type';

const Item = (item: Course) => {
	return (
		<Card className='shadow-sm'>
			<Link to={`/collection/${item.id}`}>
				<Card.Img
					variant='top'
					src='data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22257%22%20height%3D%22120%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20257%20120%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_195a7f1e2ce%20text%20%7B%20fill%3A%2367a774%3Bfont-weight%3Abold%3Bfont-family%3AArial%2C%20Helvetica%2C%20Open%20Sans%2C%20sans-serif%2C%20monospace%3Bfont-size%3A13pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_195a7f1e2ce%22%3E%3Crect%20width%3D%22257%22%20height%3D%22120%22%20fill%3D%22%2381d192%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2294.75520706176758%22%20y%3D%2266%22%3E257x120%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E'
				/>
			</Link>
			<Card.Body>
				<Card.Title>{item.title}</Card.Title>
				<Card.Subtitle className='mb-2 text-muted'>
					{item.category}
				</Card.Subtitle>
				<Card.Text>{item.description}</Card.Text>
				<div className='d-flex justify-content-between align-items-center'>
					<ButtonGroup>
						<small>Lessons: {item.lessons}</small>
					</ButtonGroup>
					<small className='text-body-secondary'>9 mins</small>
				</div>
			</Card.Body>
		</Card>
	);
};

export default Item;
