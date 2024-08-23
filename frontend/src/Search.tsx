import './Search.css'
import {useLocation, useNavigate} from "react-router-dom";
import SearchResult, {Campus} from "./components/SearchResource.tsx";
import {Resource} from "./components/SearchResource.tsx";
import {useState} from "react";
import {searchResources} from "./functions/searchResources.ts";

export const campuses = {
    CUNY: 'CUNY',
    HUNT: 'Hunter College',
    BRCH: 'Baruch College',
    BKLN: 'Brooklyn College',
    CSTI: 'College of Staten Island',
    JJAY: 'John Jay College of Criminal Justice',
    LMAN: 'Lehman College',
    MDEV: 'Medgar Evers College',
    NYCT: 'New York City College of Technology',
    QNSC: 'Queens College',
    CCNY: 'The City College of New York',
    YORK: 'York College'
}
function Search() {
    const location = useLocation();

    const [campus, setCampus] = useState<Campus>(location.state.campus);
    const [query, setQuery] = useState(location.state.query);

    const navigate = useNavigate();

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setQuery(e.target.value);
    }

    const handleSelectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        setCampus(e.target.value as Campus);
    }

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const res = await searchResources(campus, query);
        console.log(res.message);

        navigate('/search', { state: { query: query, campus: campus, results: res.results } });
    }

    const results = location.state.results;

    for (const result of results)
        console.log(result)

    return (
        <div className="search-container">
            <img className='logo' src='/src/assets/coogle.png' alt='Coogle Logo' height={200}/>
            <form className='search-form' onSubmit={handleSubmit} style={{gap: '1em', marginBottom: '1em'}}>
                <div>
                    <label style={{marginRight: '0.7em'}}>Campus:</label>
                    <select name="campus" id="campus-select" value={campus} onChange={handleSelectChange} required>
                        <option value='' disabled>Select a campus</option>
                        <option value="BRCH">Baruch College</option>
                        <option value="BKLN">Brooklyn College</option>
                        <option value="CSTI">College of Staten Island</option>
                        <option value="HUNT">Hunter College</option>
                        <option value="JJAY">John Jay College of Criminal Justice</option>
                        <option value="LMAN">Lehman College</option>
                        <option value="MDEV">Medgar Evers College</option>
                        <option value="NYCT">New York City College of Technology</option>
                        <option value="QNSC">Queens College</option>
                        <option value="CCNY">The City College of New York</option>
                        <option value="YORK">York College</option>
                    </select>
                </div>
                <div className='search-bar'>
                    <input
                        placeholder='What do you need?'
                        className='search-input'
                        value={query}
                        onChange={handleInputChange}
                        required
                    />

                    <button>Search</button>
                </div>
            </form>

            <h5 className="search-query">Results for "{query}" at {campuses[location.state.campus as Campus]} ({results.length}):</h5>

            <div className="resource-list">
                {
                    results && results.map((result: Resource[], i: number) =>
                        <SearchResult key={i} resource={result[2]}/>
                    )
                }
            </div>
        </div>
    )
}

export default Search