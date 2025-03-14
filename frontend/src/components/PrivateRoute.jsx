// PrivateRoute.jsx
import {Navigate} from 'react-router-dom';
import {useAuth} from '../context/AuthContext';

export function PrivateRoute({children}) {
    const {isLoggedIn} = useAuth();

    if (!isLoggedIn) {
        // Dacă nu e logat, redirectez la /login
        return <Navigate to="/login" replace/>;
    }

    // Altfel, afișează componenta protejată
    return children;
}