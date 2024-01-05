import * as React from 'react'
import {
  Box,
  CssBaseline,
  Toolbar,
  Typography,
} from '@mui/material'
import AppHeader from '@/components/appheader'
import Copyright from '@/components/appfooter'

export default function ClippedDrawer() {
  return (
    <Box sx={{ display: 'flex' }}>
      <AppHeader />
      <Box component="main" sx={{ flexGrow: 1, p: 3, display: 'flex', flexDirection: 'column', minHeight: '95vh' }}>
        <Toolbar />
        <Typography paragraph>
          {process.env.API_URL}
        </Typography>
        <Box sx={{ mt: 'auto' , p: 2}}>
          <Copyright />
        </Box>
      </Box>
    </Box>
  )
}
