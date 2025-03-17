// PrivateRoute.jsx
import {Navigate} from 'react-router-dom';
import {useAuth} from '../context/AuthContext.jsx';

export function PrivateRoute({children}) {
    const {isLoggedIn} = useAuth();

    if (!isLoggedIn) {
        return <Navigate to="/login" replace/>;
    }

    return children;
}