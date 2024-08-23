import './SearchResource.css'
import {campuses} from "../Search.tsx";

export type Campus = 'CUNY' | 'HUNT' | 'BRCH' | 'BKLN' | 'CSTI' | 'JJAY' | 'LMAN' | 'MDEV' | 'NYCT' | 'QNSC' | 'CCNY' | 'YORK';

export type Resource = {
    name: string,
    description: string,
    campus: Campus,
    website: string,
}

const SearchResult = ({ resource }: { resource: Resource, quality: number }) => {
    return (
        <div className="resource-container">
            <div>
                <span className="resource-title">{resource.name}</span>
                <span className="resource-campus" style={{color: "dimgrey"}}>{campuses[resource.campus]}</span>
            </div>

            <a href={resource.website}>{resource.website}</a>
            <p className="resource-description">{resource.description}</p>
        </div>
    );
};

export default SearchResult;