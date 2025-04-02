import React from 'react';
import { NavDropdown } from 'react-bootstrap';

import { useApiGet } from '@/hooks/useApi';
import { Category } from '@/types/category.type';
import { fetchCategories } from '@/api/services/category.service';
import { Link } from 'react-router';

const Categories: React.FC = () => {
	const { data, error, isLoading } = useApiGet<Category[]>(['categories'], fetchCategories);

	return (
		<NavDropdown
			title='Categories'
			id='offcanvasNavbarDropdown-expand-lg'>
			{isLoading ? (
				<NavDropdown.Item disabled>Loading...</NavDropdown.Item>
			) : error ? (
				<NavDropdown.Item disabled>
					Error loading categories
				</NavDropdown.Item>
			) : data?.length ? (
				data.map((category) => (
					<NavDropdown.Item
						as={Link}
						key={category.id}
						to={`/collection/?category=${category.id}`}>
						{category.name}
					</NavDropdown.Item>
				))
			) : (
				<NavDropdown.Item disabled>
					No categories available
				</NavDropdown.Item>
			)}
		</NavDropdown>
	);
};

export default Categories;
