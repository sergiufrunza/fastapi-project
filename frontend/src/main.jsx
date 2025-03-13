import { createRoot } from 'react-dom/client'
import { MainPage } from './pages/MainPage.jsx'
import { LoginPage } from "./pages/LoginPage.jsx";
import { Header } from "./components/Header.jsx";
import './main.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'


createRoot(document.getElementById('root')).render(
    <BrowserRouter>
        <Header></Header>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </BrowserRouter>
)
