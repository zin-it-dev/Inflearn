import Base from './base.type';

export type Course = Base & {
	title: string;
	description: string;
	date_created: string;
	category: string;
	lessons: string;
};

export type Courses = {
	results: Pick<
		Course,
		'id' | 'title' | 'description' | 'date_created' | 'category' | 'lessons'
	>[];
};
