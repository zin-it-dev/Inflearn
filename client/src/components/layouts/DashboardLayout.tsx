import { Outlet } from 'react-router';

const DashboardLayout = () => {
	return (
		<section>
			<Outlet />
		</section>
	);
};

export default DashboardLayout;
