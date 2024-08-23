import { createRoot } from 'react-dom/client'
import {
    createBrowserRouter,
    RouterProvider,
} from "react-router-dom";

import App from './App.tsx'
import Create from './Create.tsx'
import './index.css'
import Search from "./Search.tsx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
    },
    {
        path: "/create",
        element: <Create />,
    },
    {
        path: "/search",
        element: <Search />,
    }
]);

createRoot(document.getElementById('root')!).render(
    <RouterProvider router={router} />
)
