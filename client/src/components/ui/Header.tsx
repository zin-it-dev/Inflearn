import { Link } from 'react-router';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Offcanvas from 'react-bootstrap/Offcanvas';
import { IoPersonOutline } from 'react-icons/io5';

import useCategories from '@/hooks/useCategories';
import Category from '@/types/category.type';
import Search from './Search';

const Header = () => {
	const data = useCategories();
	const expand: string = 'lg';

	return (
		<Navbar
			className='mb-3 shadow-sm'
			as='header'
			key={expand}
			expand={expand}
			data-bs-theme='dark'
			bg='primary'>
			<Container>
				<Link
					to={'/'}
					className='navbar-brand'>
					Inflearn 인프런 🎓
				</Link>
				<Navbar.Toggle aria-controls={`offcanvasNavbar-expand-${expand}`} />
				<Navbar.Offcanvas
					id={`offcanvasNavbar-expand-${expand}`}
					aria-labelledby={`offcanvasNavbarLabel-expand-${expand}`}
					placement='end'>
					<Offcanvas.Header closeButton>
						<Offcanvas.Title
							id={`offcanvasNavbarLabel-expand-${expand}`}>
							Offcanvas
						</Offcanvas.Title>
					</Offcanvas.Header>
					<Offcanvas.Body>
						<Nav className='justify-content-center align-items-center flex-grow-1'>
							<li className='nav-item'>
								<NavDropdown
									title='Categories'
									className='me-0'
									id={`offcanvasNavbarDropdown-expand-${expand}`}>
									{data?.map(
										(
											category: Category,
										) => (
											<Link
												key={
													category.id
												}
												className='dropdown-item'
												to={`/?category=${category.id}`}>
												{
													category.name
												}
											</Link>
										),
									)}
								</NavDropdown>
							</li>
							<li className='nav-item'>
								<Link
									className='nav-link'
									to={'/collection'}>
									Collection
								</Link>
							</li>
							<li className='nav-item'>
								<Link
									className='nav-link'
									to={'/about'}>
									About
								</Link>
							</li>
							<li className='nav-item'>
								<Link
									className='nav-link'
									to={'/contact'}>
									Contact
								</Link>
							</li>
							<li className='nav-item'>
								<NavDropdown
									title={
										<IoPersonOutline
											size={22}
										/>
									}
									className='me-0'
									id={`offcanvasNavbarDropdown-expand-${expand}`}>
									<Link
										className='dropdown-item'
										to={'/sign-in'}>
										Sign In
									</Link>
									<Link
										className='dropdown-item'
										to={'/sign-up'}>
										Sign Up
									</Link>
								</NavDropdown>
							</li>
						</Nav>
						<Search />
					</Offcanvas.Body>
				</Navbar.Offcanvas>
			</Container>
		</Navbar>
	);
};

export default Header;
