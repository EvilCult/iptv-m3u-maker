import React, { useState, useEffect, useRef } from 'react'
import Avatar from '@mui/material/Avatar'
import Button from '@mui/material/Button'
import CssBaseline from '@mui/material/CssBaseline'
import TextField from '@mui/material/TextField'
import Box from '@mui/material/Box'
import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'

import Copyright from '@/components/appfooter'

const Login = () => {
  const [uname, setUname] = useState('')
  const [uNameErr, setuNameErr] = useState(false)
  const [pwd, setPwd] = useState('')
  const [uPwdErr, setuPwdErr] = useState(false)
  const [submit, setSubmit] = useState(false)
  // const notify = useRef()

  // const { loading, msg, setMsg } = useLogin(uname, pwd, submit)

  const handleKeyup = (e) => {
    if(e.keyCode === 13) {
      handleLogin()
    }
  }

  const handleLogin = () => {
    setuNameErr(false)
    setuPwdErr(false)
    if (uname !== '' && pwd !== '') {
      setSubmit(true)
      console.log(uname, pwd)
    } else {
      if (uname === '') {
        setuNameErr(true)
      } else {
        setuPwdErr(true)
      }
    }
  }

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
          Sign in
        </Typography>
        <Box component="form" noValidate sx={{ mt: 1 }}>
          <TextField
            error={uNameErr}
            margin="normal"
            required
            fullWidth
            id="username"
            label="Username"
            name="username"
            autoFocus
            onKeyUp={handleKeyup}
            onChange={(e) => setUname(e.target.value)}
          />
          <TextField
            error={uPwdErr}
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            onKeyUp={handleKeyup}
            onChange={(e) => setPwd(e.target.value)}
          />
          <Button
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            onClick={handleLogin}
          >
            Sign In
          </Button>
        </Box>
      </Box>
      <Copyright sx={{ mt: 8, mb: 4 }} author='EvilCult' />
    </Container>
  )
}

export default Login
