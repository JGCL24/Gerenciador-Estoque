const API_BASE = 'https://preinstructive-unrhapsodically-odette.ngrok-free.dev'

const headersPadrao = {
  'Content-Type': 'application/json',
  'ngrok-skip-browser-warning': 'true'
}

export async function fetchProducts() {
  const res = await fetch(`${API_BASE}/products`, {
    headers: { 'ngrok-skip-browser-warning': 'true' }
  })
  return res.json()
}

export async function createProduct(payload) {
  const res = await fetch(`${API_BASE}/products`, {
    method: 'POST',
    headers: headersPadrao,
    body: JSON.stringify(payload)
  })
  return res.json()
}

export async function updateProduct(id, payload) {
  const res = await fetch(`${API_BASE}/products/${id}`, {
    method: 'PUT',
    headers: headersPadrao,
    body: JSON.stringify(payload)
  })
  return res.json()
}

export async function deleteProduct(id) {
  return fetch(`${API_BASE}/products/${id}`, {
    method: 'DELETE',
    headers: { 'ngrok-skip-browser-warning': 'true' }
  })
}

export async function fetchMovements() {
  const res = await fetch(`${API_BASE}/movements`, {
    headers: { 'ngrok-skip-browser-warning': 'true' }
  })
  return res.json()
}

export async function createMovement(payload) {
  const res = await fetch(`${API_BASE}/movements`, {
    method: 'POST',
    headers: headersPadrao,
    body: JSON.stringify(payload)
  })
  const data = await res.json()
  return data
}