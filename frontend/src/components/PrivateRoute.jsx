// PrivateRoute.jsx
import {Navigate} from 'react-router-dom';
import {useAuth} from '../context/AuthContext';

export function PrivateRoute({children, fallback = null}) {
    const {isLoggedIn} = useAuth();

    if (!isLoggedIn) {
        return fallback || <Navigate to="/login" replace/>;
    }

    return children;
}