export async function login(uname: string, pwd: string) {
  return await fetch(
    process.env.API_URL + '/login/',
    {
      method: "POST",
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        uname: uname,
        pwd: pwd,
      })
    }
  )
    .then(res => {
      if (!res.ok) throw Error(res.statusText)
      return res.json()
    })
    .catch(() => { return { 'err': 'network_error' } })
}

export async function renew(jwt: string) {
  return await fetch(
    process.env.API_URL + '/login/renew',
    {
      method: 'GET',
      mode: 'cors',
      headers: { 'Authorization': jwt },
    }
  )
    .then(res => {
      if (!res.ok) throw Error(res.statusText)
      return res.json()
    })
    .catch(() => { return { 'err': 'network_error' } })
}

export async function editPwd(uname: string, pwd: string, newpwd: string) {
  let jwt = localStorage.getItem('jwt') || ''

  return await fetch(
    process.env.API_URL + '/login/pwd',
    {
      method: "POST",
      mode: 'cors',
      headers: { 'Authorization': jwt },
      body: JSON.stringify({
        uname: uname,
        pwd: pwd,
        newpwd: newpwd,
      })
    }
  )
    .then(res => {
      if (!res.ok) throw Error(res.statusText)
      return res.json()
    })
    .catch(() => { return { 'err': 'network_error' } })
}
