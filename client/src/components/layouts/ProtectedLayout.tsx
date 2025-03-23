import { Navigate, Outlet } from 'react-router';

const ProtectedLayout = () => {
	const user = false;

	return user ? <Outlet /> : <Navigate to='/sign-in' />;
};

export default ProtectedLayout;
