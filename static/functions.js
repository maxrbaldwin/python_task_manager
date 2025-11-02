async function auth_user(path, payload) {
  const endpoint = `http://127.0.0.1:8080/${path}`
  try {
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    const user = await res.json();

    if (!user) {
      alert("Your password is incorrect. Please try again")
    }

    if (user.id) {
      window.location.replace('/profile')
    }
  } catch (err) {
    alert("Error logging in. Refresh and try again")
  }
}

async function handle_task(task) {
  const endpoint = `http://127.0.0.1:8080/handle_task`
  try {
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(task)
    })
    const user = await res.json();

    if (user.id) {
      window.location.href = ('/profile')
    }
  } catch (err) {
    alert("Error logging in. Refresh and try again")
  }
}