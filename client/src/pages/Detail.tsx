import { useParams } from 'react-router';

const Detail = () => {
	const { id } = useParams();

	return <div>Detail {id}</div>;
};

export default Detail;
