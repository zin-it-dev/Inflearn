import React from 'react';
import { Container } from 'react-bootstrap';
import { Outlet } from 'react-router';

const AuthLayout: React.FC = () => {
	return (
		<Container as='main'>
			<Outlet />
		</Container>
	);
};

export default AuthLayout;
