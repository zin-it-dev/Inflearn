import Base from './base.type';

export type Comment = Base & {
	content: string;
	user: string;
};
