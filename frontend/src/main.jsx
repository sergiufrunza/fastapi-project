import {createRoot} from 'react-dom/client'
import {PrivateRoute} from "./components/PrivateRoute.jsx";
import {MainPage} from './pages/MainPage.jsx'
import {LoginPage} from "./pages/LoginPage.jsx";
import {PersonalPage} from "./pages/PersonalPage.jsx";
import {Header} from "./components/Header.jsx";
import {AuthProvider} from './context/AuthContext.jsx'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import './main.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'

const queryClient = new QueryClient();

createRoot(document.getElementById('root')).render(
    <BrowserRouter>
        <QueryClientProvider client={queryClient}>
        <AuthProvider>
            <Header></Header>
            <div className="max-w-screen-xl mx-auto w-full h-full py-6 px-4 sm:py-4 sm:px-3">
            <Routes>
                <Route path="/" element={<MainPage/>}/>
                <Route path="/login" element={<LoginPage/>}/>
                <Route
                    path="/personal"
                    element={
                        <PrivateRoute>
                            <PersonalPage/>
                        </PrivateRoute>
                    }
                />

            </Routes>
            </div>
        </AuthProvider>
        </QueryClientProvider>
    </BrowserRouter>
)
