// apiClient.js
import axios from 'axios';

// Aici setezi adresa de bază a API-ului.
// Poți prelua dintr-o variabilă de mediu (ex. process.env.REACT_APP_API_URL)
// sau să pui direct string-ul hardcodat "http://localhost:8000"
// Exemplu cu variabilă de mediu:
export const apiClient = axios.create({
  baseURL:'http://localhost:8000/api/v1/',
});
