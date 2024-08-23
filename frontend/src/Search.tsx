import './Search.css'
import {useLocation} from "react-router-dom";
import SearchResult, {Campus} from "./components/SearchResource.tsx";
import {Resource} from "./components/SearchResource.tsx";

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

    const query = location.state.query;
    const campus : Campus = location.state.campus;
    const results = location.state.results;

    console.log(location.state.campus)

    return (
        <>
            <h1 className='logo'>Project Name</h1>

            <form className='search-form' style={{gap: '1em', marginBottom: '1em'}}>
                <div>
                    <label style={{marginRight: '0.7em'}}>Campus:</label>
                    <select name="campus" id="campus-select" value={campus} required>
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
                        required
                    />

                    <button>Search</button>
                </div>
            </form>

            <h5 className="search-query">Results for "{query}" at {campuses[campus]} ({results.length}):</h5>


            <div className="resource-list">
                {
                    results && results.map((result: Resource[], i: number) =>
                        <SearchResult key={i} resource={result[2]}/>
                    )
                }
            </div>
        </>
    )
}

export default Search