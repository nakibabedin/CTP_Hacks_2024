export const fetchEndpoint = async (endpoint : string) => {
	let res = await fetch('http://127.0.0.1:5000' + endpoint);
	return await res.json();
}