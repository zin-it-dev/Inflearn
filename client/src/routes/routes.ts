import Collection from '@/pages/Collection';
import Detail from '@/pages/Detail';
import Home from '@/pages/Home';
import LogIn from '@/pages/LogIn';
import Profile from '@/pages/Profile';

/* eslint-disable @typescript-eslint/no-explicit-any */
type RouteType = {
	path: string;
	component: any;
	layout: any | undefined | null;
};

export const publicRoutes: RouteType[] = [
	{
		path: '/',
		component: Home,
		layout: undefined,
	},
	{
		path: '/collection',
		component: Collection,
		layout: undefined,
	},
	{
		path: '/collection/:id',
		component: Detail,
		layout: undefined,
	},
	{
		path: '/sign-in',
		component: LogIn,
		layout: null,
	},
];

export const privateRoutes: RouteType[] = [
	{
		path: '/profile',
		component: Profile,
		layout: undefined,
	},
];
