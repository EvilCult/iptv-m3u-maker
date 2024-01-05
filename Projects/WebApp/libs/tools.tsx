export const jwt = (jwt = '') => {
  const jwtBody = jwt.split('.')
  let jwtHeader, jwtPayload

  const initJwt = {
    uid  : 0,
    uname: '',
    iat  : 0,
    exp  : 0,
    iss  : '',
  }

  if (jwtBody.length === 3) {
    jwtHeader  = _base64url_decode(jwtBody[0])
    jwtPayload = _base64url_decode(jwtBody[1])

    const header = {
      alg: jwtHeader.alg ? jwtHeader.alg : '',
      typ: jwtHeader.typ ? jwtHeader.typ : '',
    }

    if (
      header.alg.toLowerCase() === 'hs256'
      && header.typ.toLowerCase() ==='jwt'
    ) {
      const jwtInfo = {
        uid  : jwtPayload.data.uid ? jwtPayload.data.uid    : '0',
        uname: jwtPayload.data.uname ? jwtPayload.data.uname: '',
        iat: jwtPayload.iat ? jwtPayload.iat: 0,
        exp: jwtPayload.exp ? jwtPayload.exp: 0,
        iss: jwtPayload.iss ? jwtPayload.iss: '',
      }

      return jwtInfo
    } else {
      return initJwt
    }
  } else {
    return initJwt
  }
}

export const _base64url_decode = (safeStr:string) => {
  let originStr = safeStr.replace(/-/g, '+')
  originStr = originStr.replace(/_/g, '/')

  let mod4 = originStr.length % 4

  if (mod4) {
    originStr += '===='.substring(0, mod4)
  }

  let json = Buffer.from(originStr, 'base64').toString()
  let data = JSON.parse(json)

  return data
}

export const tsToDate = (ts:number, typ = 'f') => {
  if (ts !== 0) {
    const beauty = (v:number) => {
      const vs = v.toString()
      return v < 10 ? '0' + vs : vs
    }

    const date = new Date(ts * 1000)
    const Y = date.getFullYear() + '-'
    const M = beauty(date.getMonth() + 1)
    const D = '-' + beauty(date.getDate())
    const h = beauty(date.getHours())
    const m = ':' + beauty(date.getMinutes())
    const s = ':' + beauty(date.getSeconds())

    switch (typ) {
      case 'full':
        return Y + M + D + ' ' + h + m + s

      case 'date':
        return Y + M + D

      case 'time':
        return Y + M + D + ' ' + h + m

            default:
        return Y + M + D + ' ' + h + m + s
    }
  } else {
    return ''
  }
}
