export default function Login() {
  function enviar(evento) {
    evento.preventDefault()
    // Pendiente (clase): pedir el token a POST /api/token/ y guardarlo.
  }

  return (
    <main className="login">
      <form onSubmit={enviar}>
        <h1>Iniciar sesión</h1>
        <label>
          Usuario
          <input name="username" autoComplete="username" required />
        </label>
        <label>
          Contraseña
          <input name="password" type="password" autoComplete="current-password" required />
        </label>
        <button type="submit">Entrar</button>
      </form>
    </main>
  )
}
