import { Route, Routes } from 'react-router';

import RootLayout from '@/components/layouts/RootLayout';
import { privateRoutes, publicRoutes } from '@/routes/routes';
import AuthLayout from './components/layouts/AuthLayout';
import ProtectedLayout from '@/components/layouts/ProtectedLayout';

const App = () => {
	return (
		<Routes>
			{publicRoutes.map((route, idx) => {
				const Layout = route.layout === null ? AuthLayout : RootLayout;
				return (
					<Route
						key={idx}
						element={<Layout />}>
						<Route
							path={route.path}
							element={<route.component />}
						/>
						<Route element={<ProtectedLayout />}>
							{privateRoutes.map((route, idx) => (
								<Route
									key={idx}
									path={route.path}
									element={
										<route.component />
									}
								/>
							))}
						</Route>
					</Route>
				);
			})}
		</Routes>
	);
};

export default App;
