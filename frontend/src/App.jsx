import { Link, Route, Routes } from 'react-router'
import Chat from './Chat.jsx'
import Login from './Login.jsx'

export default function App() {
  return (
    <>
      <header className="barra">
        <Link to="/" className="marca">Chat de la clase</Link>
        <Link to="/login">Iniciar sesión</Link>
      </header>
      <Routes>
        <Route path="/" element={<Chat />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </>
  )
}
