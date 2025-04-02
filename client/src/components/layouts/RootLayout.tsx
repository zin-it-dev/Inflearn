import React from 'react';
import { Container } from 'react-bootstrap';
import { Outlet } from 'react-router';

import Header from '../ui/Header';
import Footer from '../ui/Footer';

const RootLayout: React.FC = () => {
	return (
		<>
			<Header />

			<Container as='main'>
				<Outlet />
			</Container>

			<Footer />
		</>
	);
};

export default RootLayout;
