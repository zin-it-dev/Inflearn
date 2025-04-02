import React from 'react';
import { Form } from 'react-bootstrap';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { User, UserSchema } from '@/types/user.type';
import { axiosInstance } from '@/api/configs/axios';
import { LoginResponse } from '@/types/api.type';
import { ENDPOINTS } from '@/utils/constants/endpoints';
import { useApiSend } from '@/hooks/useApi';

const Login: React.FC = () => {
	const { register, handleSubmit } = useForm<User>({
		resolver: zodResolver(UserSchema),
	});

	const onSubmit = (data: User) => {
		console.log('SUCCESS', data);
	};

	const loginUser = async (data: User) => {
		const response = await axiosInstance.post<LoginResponse>(ENDPOINTS.token, data);
		return response.data;
	};

	const mutation = useApiSend((userData: User) => loginUser(userData));

	return (
		<div>
			<Form onSubmit={handleSubmit(onSubmit)}>
				{/* <input
					type='text'
					placeholder='First name'
					{...register('firstName')}
				/>
				<input
					type='text'
					placeholder='Last name'
					{...register('lastName')}
				/>
				<input
					type='text'
					placeholder='Username'
					{...register('username')}
				/> */}
				<input
					type='email'
					placeholder='Email'
					{...register('email')}
					autoComplete='email'
				/>
				<input
					type='password'
					placeholder='Password'
					{...register('password')}
					autoComplete='new-password'
				/>
				{/* <input
					type='password'
					placeholder='Confirm password'
					{...register('confirmPassword')}
					autoComplete='new-password'
				/> */}
				<input type='submit' />
			</Form>
		</div>
	);
};

export default Login;
