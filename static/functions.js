function post_json(path, payload) {
  console.log(path, payload)
  const endpoint = `http://127.0.0.1:8080/${path}`
  fetch(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
}

console.log('cheese')