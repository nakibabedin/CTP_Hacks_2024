export const searchResources = async (campus: string, query: string, amount: number = 10) => {
    const res = await fetch('http://127.0.0.1:5000/searchResources', {
        method: "POST",
        body: JSON.stringify({
            campus: campus,
            query: query,
            amount: amount
        }),
        headers: {
            'Content-Type': 'application/json; charset=UTF-8',
        },
        mode: 'cors',
    });

    return await res.json();
}