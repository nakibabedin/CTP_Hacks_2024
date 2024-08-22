import { useEffect, useState } from 'react'
import { fetchEndpoint } from './functions/fetchEndpoint';
import './App.css'

function App() {
	const [data, setData] = useState<string>('');

	useEffect(() => {
		const getMsg = async () => {
			const res = await fetchEndpoint('/');
			setData(res.message);
		}

		getMsg();
	}, []);

	return (
		<>
			<div>{data}</div>
		</>
	)
}

export default App
