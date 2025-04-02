import React from 'react';
import { Button, Form } from 'react-bootstrap';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Offcanvas from 'react-bootstrap/Offcanvas';
import { Link, NavLink } from 'react-router';

import Categories from './Categories';

const Header: React.FC = () => {
	return (
		<Navbar
			as='header'
			sticky='top'
			expand={'lg'}
			className='mb-3'>
			<Container>
				<Navbar.Brand
					className={'fw-bold'}
					as={Link}
					to='/'>
					Inflearn 인프런 🎓
				</Navbar.Brand>
				<Navbar.Toggle aria-controls='offcanvasNavbar-expand-lg' />
				<Navbar.Offcanvas
					id='offcanvasNavbar-expand-lg'
					aria-labelledby='offcanvasNavbarLabel-expand-lg'
					placement='end'>
					<Offcanvas.Header closeButton>
						<Offcanvas.Title
							className='fw-bold'
							id='offcanvasNavbarLabel-expand-lg'>
							Inflearn 인프런 🎓
						</Offcanvas.Title>
					</Offcanvas.Header>
					<Offcanvas.Body>
						<Nav className='justify-content-center flex-grow-1 pe-3'>
							<Categories />

							<Nav.Link
								as={NavLink}
								to={'/collection'}>
								Collection
							</Nav.Link>
							<Nav.Link
								as={NavLink}
								to={'/about'}>
								About
							</Nav.Link>
							<Nav.Link
								as={NavLink}
								to={'/contact'}>
								Contact
							</Nav.Link>
						</Nav>

						<Nav>
							<Nav.Link
								as={Link}
								to={'/auth/login'}>
								Log In
							</Nav.Link>
							<Nav.Link
								as={Link}
								to={'/auth/register'}>
								Register
							</Nav.Link>
						</Nav>

						<Form className='d-flex d-lg-none d-block'>
							<Form.Control
								type='search'
								placeholder='Search'
								className='me-2'
								aria-label='Search'
							/>
							<Button variant='outline-success'>
								Search
							</Button>
						</Form>
					</Offcanvas.Body>
				</Navbar.Offcanvas>
			</Container>
		</Navbar>
	);
};

export default Header;
