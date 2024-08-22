import {FormData} from "../Create.tsx";

export const createResource = async (data : FormData) => {
	console.log({
		campus: data.campus,
		name: data.name,
		data: data
	})

	const res = await fetch('http://127.0.0.1:5000/createResource', {
		method: "POST",
		body: JSON.stringify({
			campus: data.campus,
			name: data.name,
			data: data
		}),
		headers: {
			'Content-Type': 'application/json; charset=UTF-8',
		},
		mode: 'cors',
	});

	const response = await res.json();
	console.log(response.message)

	return;
}