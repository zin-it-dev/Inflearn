import { z } from 'zod';

export const UserSchema = z
	.object({
		// username: z.string().min(1, 'Username is required'),
		email: z.string().email('Invalid email'),
		password: z
			.string(),
			// .min(8, { message: 'Password is too short' })
			// .max(20, { message: 'Password is too long' }),
		// confirmPassword: z.string(),
		// firstName: z.string().min(1, 'First name is required'),
		// lastName: z.string().min(1, 'Last name is required'),
	})
	// .refine((data) => data.password === data.confirmPassword, {
	// 	message: 'Passwords do not match',
	// 	path: ['confirmPassword'],
	// });

export type User = z.infer<typeof UserSchema>;
