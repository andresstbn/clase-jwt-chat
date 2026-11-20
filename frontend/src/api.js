const API_URL = import.meta.env.VITE_API_URL

// GET a la API. Devuelve el JSON o lanza un error si la respuesta no es 2xx.
export async function obtener(ruta) {
  const respuesta = await fetch(`${API_URL}${ruta}`)
  if (!respuesta.ok) throw new Error(`Error ${respuesta.status} en ${ruta}`)
  return respuesta.json()
}
