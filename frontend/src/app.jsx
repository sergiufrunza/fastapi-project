import {IndexPage} from './pages/IndexPage.jsx'
import {UploadPage} from './pages/UploadPage.jsx'
import {LoginPage} from "./pages/LoginPage.jsx";
import {QuizPage} from './pages/QuizPage.jsx'
import {Header} from "./components/Header.jsx";
import {Routes, Route} from 'react-router-dom'
import {QueryClient, QueryClientProvider} from '@tanstack/react-query'
import {setUnauthorizedHandler} from './clients/apiClient';
import {useEffect} from 'react';
import {PrivateRoute} from "./components/PrivateRoute.jsx";
import {useAuth} from './context/AuthContext';
import './main.css'

const queryClient = new QueryClient();

export const App = () => {
    const {logout} = useAuth();
    useEffect(() => {
        setUnauthorizedHandler(() => {
            logout();
        });
    }, [logout]);
    return (

        <QueryClientProvider client={queryClient}>
            <Header></Header>
            <div className="max-w-screen-xl mx-auto w-full h-full py-6 px-4 sm:py-4 sm:px-3">
                <Routes>
                    <Route path="/" element={<IndexPage/>}/>
                    <Route path="/login" element={<LoginPage/>}/>
                    <Route path="/upload" element={
                        <PrivateRoute>
                            <UploadPage/>
                        </PrivateRoute>
                    }/>
                    <Route path="/quiz/:id" element={
                        <PrivateRoute>
                            <QuizPage/>
                        </PrivateRoute>}/>
                </Routes>
            </div>
        </QueryClientProvider>
    );
}