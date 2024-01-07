import React, { useState, useEffect, useRef } from 'react'
import {
  Box,
  CssBaseline,
  Toolbar,
  Typography,
  Button,
} from '@mui/material'
import AppHeader from '@/components/appheader'
import Copyright from '@/components/appfooter'

import Test from '@/components/test'

const DashBoard = () => {
  const test = useRef<any>()

  const handleClick = () => {
    test.current.handleAdd()
  }

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppHeader />
      <Box component="main" sx={{ flexGrow: 1, p: 3, display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <Toolbar />
        <Typography paragraph>
          {process.env.API_URL}
        </Typography>
        <Test ref={test} start={20}/>
        <Button variant="contained" onClick={handleClick}>add num</Button>
        <Box sx={{ mt: 'auto' , p: 2}}><Copyright />T</Box>
      </Box>
    </Box>
  )
}

export default DashBoard
