import { useState, useEffect } from 'react'


import * as LoginApi from '@/api/loginApi'
import * as Tools from '@/libs/tools'
import * as lang from '@/libs/langs'

const useLogin = (uname: string, pwd: string, submit: boolean) => {
  const [msg, setMsg] = useState('')
  const [loading, setLoading] = useState(false)

  const req = () => {
    let cancel = false

    if (
      submit
      && uname !== ''
      && pwd !== ''
    ) {
      setLoading(true)
      const response = LoginApi.login(uname, pwd)
      response.then(
        (res: any) => {
          if (!cancel) {
            if (parseInt(res.code) === 0) {
              const uInfo = Tools.jwt(res.data)

              localStorage.setItem('uInfo', JSON.stringify(uInfo))
              localStorage.setItem('jwt', res.data)

              setMsg('suc')
            } else {
              setMsg(lang.output('uname_pwd_err'))
            }
          }
        },
        () => {
          if (!cancel) {
            setMsg(lang.output('network_error'))
          }
        }
      )
      .finally(() => {
        if (!cancel) {
          setTimeout(() => {
          setLoading(false)
          }, 1000)
        }
      })
    }

    return () => {
      cancel = true
    }
  }

  useEffect(() => {
    const cancelRequest = req()

    return () => {
      cancelRequest()
    }
     // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [submit])

  return {loading, msg, setMsg}
}
export default useLogin
