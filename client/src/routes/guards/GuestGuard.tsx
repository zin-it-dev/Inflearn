import React from 'react';
import { Navigate, Outlet } from 'react-router';

const user = false;

const GuestGuard: React.FC = () => {
	return user ? (
		<Navigate
			to='/'
			replace
		/>
	) : (
		<Outlet />
	);
};

export default GuestGuard;
