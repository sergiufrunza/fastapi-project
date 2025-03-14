import {IndexLayout} from './layouts/IndexLayout.jsx'
import {LoginLayout} from "./layouts/LoginLayout.jsx";
import {Header} from "./components/Header.jsx";
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import {QueryClient, QueryClientProvider} from '@tanstack/react-query'
import {AuthProvider} from './context/AuthContext.jsx'
import './main.css'

const queryClient = new QueryClient();

export const App = () => {
    return (
        <BrowserRouter>
            <QueryClientProvider client={queryClient}>
                <AuthProvider>
                    <Header></Header>
                    <div className="max-w-screen-xl mx-auto w-full h-full py-6 px-4 sm:py-4 sm:px-3">
                        <Routes>
                            <Route path="/" element={<IndexLayout/>}/>
                            <Route path="/login" element={<LoginLayout/>}/>
                        </Routes>
                    </div>
                </AuthProvider>
            </QueryClientProvider>
        </BrowserRouter>
    );

}