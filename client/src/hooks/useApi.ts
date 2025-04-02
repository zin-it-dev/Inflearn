import {
	QueryFunction,
	useMutation,
	UseMutationOptions,
	useQuery,
	useQueryClient,
	UseQueryOptions,
} from '@tanstack/react-query';

export const useApiGet = <TData, TError = unknown>(
	key: string[],
	fn: QueryFunction<TData>,
	options?: Omit<UseQueryOptions<TData, TError>, 'queryKey' | 'queryFn'>,
) =>
	useQuery<TData, TError>({
		queryKey: key,
		queryFn: fn,
		...options,
	});

export const useApiSend = <TData, TVariables = void, TError = unknown>(
	fn: (variables: TVariables) => Promise<TData>,
	success?: (data: TData) => void,
	error?: (err: TError) => void,
	invalidateKey?: string[][],
	options?: Omit<
		UseMutationOptions<TData, TError, TVariables>,
		'mutationFn' | 'onSuccess' | 'onError'
	>,
) => {
	const queryClient = useQueryClient();

	return useMutation<TData, TError, TVariables>({
		mutationFn: fn,
		onSuccess: (data) => {
			invalidateKey?.forEach((key) => {
				queryClient.invalidateQueries({ queryKey: key });
			});

			success?.(data);
		},
		onError: error,
		retry: 2,
		...options,
	});
};
