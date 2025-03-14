import {useMutation} from '@tanstack/react-query';
import {apiClient} from '../clients/apiClient';
import {useState} from 'react';
import qs from 'qs'
import {useNavigate} from 'react-router-dom';
import {useAuth} from '../context/AuthContext';

export const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const {login} = useAuth();
    const navigate = useNavigate();

    const mutation = useMutation({
        mutationFn: async ({username, password}) => {
            const body = qs.stringify({username, password})

            const response = await apiClient.post('/auth/login', body, {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
            });
            return response.data;
        },
        onSuccess: (data) => {
            // Extrag token-ul din data
            if (!data || !data.access_token) {
                return;
            }


            const token = data.access_token;
            login(token);
            navigate('/');
        },
        onError: (error) => {
            console.error('Login failed', error);
        },
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!username || !password) {
            return;
        }
        mutation.mutate({username, password});
    };
    return (

                <form className="p-7 shadow-md rounded-2xl sm:mx-auto sm:w-full sm:max-w-sm space-y-6" onSubmit={handleSubmit}>
                    <h2 className="text-center text-2xl/9 font-bold tracking-tight text-gray-900">Sign in to your
                    account</h2>
                    <div>
                        <label htmlFor="username" className="block text-sm/6 font-medium text-gray-900">Email
                            address</label>
                        <div className="mt-2">
                            <input type="text" name="username" id="username" autoComplete="email" required
                                   value={username}
                                   placeholder="Email"
                                   onChange={(e) => setUsername(e.target.value)}
                                   className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 border border-gray-300"
                            />
                        </div>
                    </div>

                    <div>
                        <div className="flex items-center justify-between">
                            <label htmlFor="password"
                                   className="block text-sm/6 font-medium text-gray-900">Password</label>
                        </div>
                        <div className="mt-2">
                            <input type="password" name="password" id="password" autoComplete="current-password"
                                   required
                                   placeholder="********"
                                   value={password}
                                   onChange={(e) => setPassword(e.target.value)}
                                   className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6 border border-gray-300"
                            />
                        </div>
                    </div>

                    <div>
                        <button type="submit"
                                className="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
                            Sign in
                        </button>
                    </div>
                </form>
    );
}