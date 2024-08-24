import {useState} from 'react'
// import {createResource} from './functions/createResource';
import './App.css'
import {searchResources} from "./functions/searchResources.ts";
import {useNavigate} from "react-router-dom";
import logo from './assets/coogle.png';


function App() {
    const [campus, setCampus] = useState('');
    const [searchQuery, setSearchQuery] = useState('');
    const [loading, setLoading] = useState(false);

    const navigate = useNavigate();

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setSearchQuery(e.target.value);
    }

    const handleSelectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        setCampus(e.target.value);
    }

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        setLoading(true);

        let res;

        try {
            res = await searchResources(campus, searchQuery);
        } catch (err) {
            console.error(err);
            alert('Something went wrong, please try again later.');
            setLoading(false);
        }

        console.log(res.message);

        navigate('/search', { state: { query: searchQuery, campus: campus, results: res.results } });
    }

    return (
        <>
            <img className='logo' src={logo} alt='Coogle Logo' height={200}/>
            <form className='search-form' onSubmit={handleSubmit}>
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
                        value={searchQuery}
                        onChange={handleInputChange}
                        required
                    />

                    {
                        loading
                            ? <button className='search-button' disabled>Searching...</button>
                            : <button className='search-button'>Search</button>
                    }
                </div>
            </form>
        </>
    )
}

export default App
