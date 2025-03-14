import {createRoot} from 'react-dom/client'
import {App} from './app.jsx'
import './main.css'
import {BrowserRouter} from "react-router-dom";
import {AuthProvider} from './context/AuthContext.jsx'

createRoot(document.getElementById('root')).render(
        <AuthProvider>
            <BrowserRouter>
                <App></App>
            </BrowserRouter>
        </AuthProvider>
)
