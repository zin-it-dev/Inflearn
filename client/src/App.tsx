import React from 'react';
import { Route, Routes } from 'react-router';

import AuthLayout from '@/components/layouts/AuthLayout';
import RootLayout from '@/components/layouts/RootLayout';
import DashboardLayout from '@/components/layouts/DashboardLayout';
import { privateRoutes, publicRoutes } from '@/routes/routes';
import AuthGuard from '@/routes/guards/AuthGuard';
import GuestGuard from '@/routes/guards/GuestGuard';

const App: React.FC = () => {
	return (
		<Routes>
			{publicRoutes.map((route, idx) => {
				const Layout =
					route.layout === null
						? AuthLayout
						: route.layout ?? RootLayout;

				const Guard = route.path.startsWith('/auth/')
					? GuestGuard
					: React.Fragment;

				return (
					<Route
						key={idx}
						path={route.path}
						element={
							<Guard>
								<Layout />
							</Guard>
						}>
						<Route
							index
							element={<route.component />}
						/>
					</Route>
				);
			})}

			<Route element={<AuthGuard />}>
				{privateRoutes.map((route, idx) => {
					const Layout =
						route.layout === null
							? DashboardLayout
							: route.layout ?? RootLayout;

					return (
						<Route
							key={idx}
							element={<Layout />}>
							<Route
								path={route.path}
								element={<route.component />}
							/>
						</Route>
					);
				})}
			</Route>
		</Routes>
	);
};

export default App;
