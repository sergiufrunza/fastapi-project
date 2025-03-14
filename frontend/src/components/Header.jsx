import {Link} from 'react-router-dom'
import {useAuth} from '../context/AuthContext';
import {useNavigate} from 'react-router-dom';

export function Header() {
    const {isLoggedIn, logout} = useAuth();
    const navigate = useNavigate();

    const handleLogout = () => {
        logout(); // Șterge token-ul din localStorage și din context
        navigate('/'); // Duce user-ul înapoi la pagina principală
    };
    return (
        <div className="w-full max-w-screen-xl items-center justify-between mx-auto border-b flex py-3 px-4 gap-4">
            <div>
                <Link to="/" className="text-gray-800 text-2xl font-bold">
                    Admin
                </Link>
            </div>
            <div className="items-center flex gap-4">
                {isLoggedIn ? <button
                        className="block px-4 py-2 text-center text-gray-700 duration-150 font-medium rounded-lg border hover:bg-gray-50 active:bg-gray-100 md:text-sm"
                        onClick={handleLogout}>Logout</button> :
                    <Link
                        to={"/login"}
                        className="block px-4 py-2 text-center text-gray-700 duration-150 font-medium rounded-lg border hover:bg-gray-50 active:bg-gray-100 md:text-sm"
                    >
                        Login
                    </Link>}

            </div>
        </div>
    )
}