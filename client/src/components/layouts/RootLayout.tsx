import { Outlet } from 'react-router';
import Container from 'react-bootstrap/Container'

import Header from '../ui/Header';
import Footer from '../ui/Footer';

const RootLayout = () => {
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
