import React from 'react';
import { Container } from 'react-bootstrap';

const Footer: React.FC = () => {
	return (
		<Container
			as='footer'
			className='py-3 my-4 border-top'>
			<p className='mb-3 mb-md-0 text-body-secondary text-center'>
				&copy; {new Date().getFullYear()} ZIN Inc Website 🐻
			</p>
		</Container>
	);
};

export default Footer;
