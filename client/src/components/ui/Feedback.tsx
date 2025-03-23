import { Figure } from 'react-bootstrap';

import { Comment } from '@/types/comment.type';

const Feedback = (comment: Comment) => {
	return (
		<Figure className='text-center container'>
			<blockquote className='blockquote'>
				<p className='mb-0'>{comment.content}</p>
			</blockquote>
			<Figure.Caption className='blockquote-footer'>
				<cite
					className='text-primary'
					title={comment.user}>
					{comment.user}
				</cite>
			</Figure.Caption>
		</Figure>
	);
};

export default Feedback;
