import {useState} from 'react'
// import {fetchEndpoint} from './functions/fetchEndpoint';
import './App.css'

function App() {
    const [campus, setCampus] = useState('');
    const [searchQuery, setSearchQuery] = useState('');

    // useEffect(() => {
    // 	const getMsg = async () => {p
    // 		const res = await fetchEndpoint('/');
    // 		setData(res.message);
    // 	}
    //
    // 	getMsg();
    // }, []);

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setSearchQuery(e.target.value);
    }

    const handleSelectChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
        setCampus(e.target.value);
    }

    return (
        <>
            <h1 className='logo'>Project Name</h1>
            <form className='search-form'>
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

                    <button>Search</button>
                </div>
            </form>
        </>
    )
}

export default App
