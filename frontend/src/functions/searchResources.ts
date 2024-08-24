export const searchResources = async (campus: string, query: string, amount: number = 10) => {
    const res = await fetch('https://www.coogle.live/searchResources', {
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