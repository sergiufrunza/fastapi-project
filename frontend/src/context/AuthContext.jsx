// AuthContext.jsx
import {createContext, useContext, useState} from 'react';
import {apiClient} from "../clients/apiClient.jsx";
import qs from 'qs'

// Tipic, vei stoca aici dacă user-ul e logat, token-ul sau obiectul user, etc.
const AuthContext = createContext(null);

export function AuthProvider({children}) {
    // Poți inițializa starea pe baza unui token deja existent în localStorage
    const [token, setToken] = useState(localStorage.getItem('access_token') || null);

    // Metodă de login
    const login = (newToken) => {
        setToken(newToken);
        localStorage.setItem('access_token', newToken);
    };

    const logout = async () => {
        localStorage.removeItem('access_token');
        setToken(null);
    };

    const value = {
        token,
        isLoggedIn: !!token,
        login,
        logout
    };

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    );
}

// Un hook simplu prin care putem folosi contextul
export function useAuth() {
    return useContext(AuthContext);
}