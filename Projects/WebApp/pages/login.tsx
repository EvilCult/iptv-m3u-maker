import React, { useState, useEffect, useRef } from 'react'
import {
  Avatar,
  CssBaseline,
  TextField,
  Box,
  Typography,
  Container
} from '@mui/material'
import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
import LoadingButton from '@mui/lab/LoadingButton'
import useLogin from '@/hooks/auth/loginHook'
import Copyright from '@/components/appfooter'
import { useRouter } from 'next/router'
import Notify from '@/components/notify'
import * as lang from '@/libs/langs'

const Login = () => {
  const router = useRouter()
  const [uname, setUname] = useState('')
  const [uNameErr, setuNameErr] = useState([false,''])
  const [pwd, setPwd] = useState('')
  const [uPwdErr, setuPwdErr] = useState([false,''])
  const [submit, setSubmit] = useState(false)
  const { loading, msg, setMsg } = useLogin(uname, pwd, submit)
  const notify = useRef<{ handleNoticeOpen: (msg: string, type: string) => void } | null>(null)

  useEffect(() => {
    router.prefetch("/")
  })

  const handleKeyup = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleLogin()
    }
  }

  const handleLogin = () => {
    setuNameErr([false,''])
    setuPwdErr([false,''])
    if (uname !== '' && pwd !== '') {
      setSubmit(true)
    } else {
      if (uname === '') {
        setuNameErr([true, lang.output('user_name_empty')])
      }
      if (pwd === ''){
        setuPwdErr([true, lang.output('user_pwd_empty')])
      }
    }
  }

  useEffect(() => {
    if (msg === 'suc') {
      (notify.current) ? notify.current.handleNoticeOpen(lang.output('login_success'), 'suc') : null
      setTimeout(() => {
        router.push("/")
      }, 1000)
    } else if (msg !== ''){
      (notify.current) ? notify.current.handleNoticeOpen(msg, 'err') : null
    }

    setMsg('')
    setSubmit(false)
  }, [msg, router, setMsg])

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          {lang.output('site_title')}
        </Typography>
        <Box component="form" noValidate sx={{ mt: 1 }}>
          <TextField
            error={!!uNameErr[0]}
            helperText={uNameErr[1]}
            margin="normal"
            required
            fullWidth
            id="username"
            label={lang.output('user_name')}
            name="username"
            autoFocus
            onKeyUp={handleKeyup}
            onChange={(e) => setUname(e.target.value)}
          />
          <TextField
            error={!!uPwdErr[0]}
            helperText={uPwdErr[1]}
            margin="normal"
            required
            fullWidth
            name="password"
            label={lang.output('user_pwd')}
            type="password"
            id="password"
            onKeyUp={handleKeyup}
            onChange={(e) => setPwd(e.target.value)}
          />
          <LoadingButton
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            onClick={handleLogin}
            loading={loading}
          >
            <span>{lang.output('sign_in')}</span>
          </LoadingButton>
        </Box>
      </Box>
      <Copyright sx={{ mt: 8, mb: 4 }} />
      <Notify ref={notify} />
    </Container>
  )
}

export default Login
