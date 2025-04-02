import Loading from '@/components/ui/Loading';
import { FC, JSX, lazy, Suspense } from 'react';

const Loadable = (Component: FC) => (props: JSX.IntrinsicAttributes) => {
	return (
		<Suspense fallback={<Loading />}>
			<Component {...props} />
		</Suspense>
	);
};

const Home = Loadable(lazy(() => import('@/pages/Home')));
const About = lazy(() => import('@/pages/About'));
const Contact = lazy(() => import('@/pages/Contact'));
const Login = lazy(() => import('@/pages/Login'));
const Register = lazy(() => import('@/pages/Register'));
const Profile = lazy(() => import('@/pages/Profile'));

type AppRoute = {
	path: string;
	component: FC;
	layout?: FC | null;
};

export const publicRoutes: AppRoute[] = [
	{ path: '/', component: Home },
	{ path: '/about', component: About },
	{ path: '/contact', component: Contact },
	{ path: '/auth/login', component: Login, layout: null },
	{ path: '/auth/register', component: Register, layout: null },
];

export const privateRoutes: AppRoute[] = [{ path: '/profile', component: Profile, layout: null }];
