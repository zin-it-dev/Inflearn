import { Link } from 'react-router';

const Footer = () => {
	return (
		<footer className='py-3'>
			<p className='mb-3 mb-md-0 text-center'>
				Copyright &copy; {new Date().getFullYear()} by{' '}
				<Link
					className='fw-bold text-decoration-none'
					to={'https://github.com/zin-it-dev'}
					target='_blank'>
					ZIN
				</Link>{' '}
				Company, Inc
			</p>
		</footer>
	);
};

export default Footer;
