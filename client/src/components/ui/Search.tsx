import { useState } from 'react';
import { useSearchParams } from 'react-router';
import Form from 'react-bootstrap/Form';

const Search = () => {
	const [searchParams, setSearchParams] = useSearchParams();
	const [keyword, setKeyword] = useState<string>(searchParams.get('keyword') || '');

	const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
		const querySearch = e.target.value.trim();
		setKeyword(querySearch);

		if (querySearch) {
			setSearchParams({ keyword: querySearch });
		} else {
			setSearchParams({});
		}

		console.log(keyword);
	};

	return (
		<Form className='d-flex'>
			<Form.Control
				type='search'
				placeholder='Search'
				aria-label='Search'
				value={keyword}
				onChange={handleSearch}
			/>
		</Form>
	);
};

export default Search;
