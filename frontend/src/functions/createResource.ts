import {FormData} from "../Create.tsx";

export const createResource = async (data : FormData) => {
	console.log({
		campus: data.campus,
		name: data.name,
		data: data
	})

	const res = await fetch('https://www.coogle.live/createResource', {
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