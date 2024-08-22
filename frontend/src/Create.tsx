import React, { useState } from 'react';
import './Create.css';

type FormData = {
    campus: string;
    name: string;
    location: string;
    hours: string;
    phone: string;
    email: string;
    website: string;
    description: string;
}

const Create = () => {
    // Initialize state for form data
    const [formData, setFormData] = useState<FormData>({
        campus: '',
        name: '',
        location: '',
        hours: '',
        phone: '',
        email: '',
        website: '',
        description: '',
    });

    // Handle input changes
    const handleChange = (e: React.ChangeEvent<HTMLSelectElement> | React.ChangeEvent<HTMLInputElement> | React.ChangeEvent<HTMLTextAreaElement>) => {
        const { name, value } = e.target;

        setFormData(prevData => ({
            ...prevData,
            [name]: value
        }));
    };

    // Handle form submission
    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log('Form Data:', formData);
        // You can handle form data here, such as sending it to an API
    };

    return (
        <div style={{ textAlign: 'left' }}>
            <form onSubmit={handleSubmit}>
                <h1>Add a Resource</h1>

                <label>Campus:</label>
                <select
                    name="campus"
                    id="campus-select"
                    value={formData.campus}
                    onChange={handleChange}
                    required
                >
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

                <br /><br />

                <label htmlFor="name">Resource Name:</label>
                <input
                    type="text"
                    id="name"
                    name="name"
                    placeholder='Give this resource a descriptive name.'
                    value={formData.name}
                    onChange={handleChange}
                    required
                /><br /><br />

                <h3>Access Information</h3>

                <label htmlFor="location">Location:</label>
                <input
                    type="text"
                    id="location"
                    name="location"
                    placeholder='Where should people go to find this resource?'
                    value={formData.location}
                    onChange={handleChange}
                    required
                /><br /><br />

                <label htmlFor='hours'>Hours of Operation:</label>
                <input
                    type='text'
                    id='hours'
                    name='hours'
                    placeholder='When is this resource open for students?'
                    value={formData.hours}
                    onChange={handleChange}
                    required
                />

                <br /><br />

                <h3>Contact Information</h3>

                <label htmlFor="phone">Phone:</label>
                <input
                    type="tel"
                    id="phone"
                    name="phone"
                    placeholder='Enter the best number for students to contact.'
                    value={formData.phone}
                    onChange={handleChange}
                    required
                /><br /><br />

                <label htmlFor="email">Email:</label>
                <input
                    type="email"
                    id="email"
                    name="email"
                    placeholder='Enter resource email address.'
                    value={formData.email}
                    onChange={handleChange}
                    required
                /><br /><br />

                <label htmlFor="website">Website:</label>
                <input
                    type="url"
                    id="website"
                    name="website"
                    placeholder='Enter the website for this resource, or other helpful links.'
                    value={formData.website}
                    onChange={handleChange}
                    required
                /><br />

                <h3>Description</h3>

                <textarea id="description" name="description" rows={4} placeholder='Describe your services. Please be descriptive.' value={formData.description} onChange={handleChange} required></textarea><br/><br/>

                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default Create;