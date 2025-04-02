import { Navigate, Outlet } from 'react-router';

const user = false;

const AuthGuard = () => {
	return user ? (
		<Outlet />
	) : (
		<Navigate
			to='/auth/login'
			replace
		/>
	);
};

export default AuthGuard;
