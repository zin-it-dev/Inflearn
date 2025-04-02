import axios, { AxiosInstance, CreateAxiosDefaults } from 'axios';

import { BASE_URL } from '@/utils/constants/endpoints';

const baseConfig: CreateAxiosDefaults = {
	baseURL: BASE_URL,
	timeout: 10000,
	headers: {
		'Content-type': 'application/json',
	},
};

export const axiosInstanceInterceptors: AxiosInstance = axios.create(baseConfig);

export const axiosInstance: AxiosInstance = axios.create(baseConfig);

