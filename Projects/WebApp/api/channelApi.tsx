export async function list (page: number = 1, limit: number = 20) {
  const jwt = localStorage.getItem('jwt') || ''

  const params = new URLSearchParams()
  params.append('page', page.toString())
  params.append('limit', limit.toString())

  return await fetch(
    process.env.API_URL + '/channel/list?' + params.toString(),
    {
      method : 'GET',
      mode   : 'cors',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': jwt
      }
    }
  )
  .then(res => {
    if (!res.ok) throw Error(res.statusText)
    return res.json()
  })
  .catch(() => {return {'err': 'network_error'}})
}
