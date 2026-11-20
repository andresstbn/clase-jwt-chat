import { useEffect, useState } from 'react'
import { obtener } from './api.js'

const hora = new Intl.DateTimeFormat('es-CO', { hour: 'numeric', minute: '2-digit' })

export default function Chat() {
  const [canales, setCanales] = useState([])
  const [canal, setCanal] = useState(null)
  const [mensajes, setMensajes] = useState([])
  const [error, setError] = useState('')

  useEffect(() => {
    obtener('/api/canales/')
      .then((datos) => setCanales(datos.results))
      .catch((e) => setError(e.message))
  }, [])

  useEffect(() => {
    if (!canal) return
    let vigente = true // si cambias de canal antes de que llegue la respuesta, se descarta
    // La API pagina de a 20 y manda primero los más recientes: aquí solo se
    // muestra esa primera página, invertida para leerla de arriba hacia abajo.
    obtener(`/api/mensajes/?canal=${canal.id}`)
      .then((datos) => vigente && setMensajes(datos.results.toReversed()))
      .catch((e) => vigente && setError(e.message))
    return () => {
      vigente = false
    }
  }, [canal])

  return (
    <div className="chat">
      <nav className="canales" aria-label="Canales">
        <h2>Canales</h2>
        {canales.map((c) => (
          <button
            key={c.id}
            className={c.id === canal?.id ? 'activo' : ''}
            aria-current={c.id === canal?.id}
            onClick={() => {
              setMensajes([])
              setCanal(c)
            }}
          >
            # {c.nombre}
          </button>
        ))}
      </nav>

      <main className="mensajes">
        {error && <p className="error" role="alert">{error}</p>}
        {!canal ? (
          <p className="vacio">Elige un canal para ver sus mensajes.</p>
        ) : (
          <>
            <header>
              <h1># {canal.nombre}</h1>
              <p>{canal.descripcion}</p>
            </header>
            <ul>
              {mensajes.map((m) => (
                <li key={m.id}>
                  <strong>{m.autor}</strong>
                  <time dateTime={m.creado}>{hora.format(new Date(m.creado))}</time>
                  {m.editado && <small>(editado)</small>}
                  <p>{m.texto}</p>
                </li>
              ))}
            </ul>
            <p className="aviso">Inicia sesión para escribir en este canal.</p>
          </>
        )}
      </main>
    </div>
  )
}
