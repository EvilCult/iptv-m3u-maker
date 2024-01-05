import * as React from 'react'
import {
  Box,
  CssBaseline,
  Toolbar,
  Typography,
} from '@mui/material'
import AppHeader from '@/components/appheader'
import Copyright from '@/components/appfooter'

import * as ChannelApi from '@/api/channelApi'

const DashBoard = () => {

  const response = ChannelApi.list(1)
  response.then(
    (res: any) => {
      console.log(res)

    },
    () => {
    }
  )
  .finally(() => {})

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppHeader />
      <Box component="main" sx={{ flexGrow: 1, p: 3, display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <Toolbar />
        <Typography paragraph>
          {process.env.API_URL}
        </Typography>
        <Box sx={{ mt: 'auto' , p: 2}}><Copyright /></Box>
      </Box>
    </Box>
  )
}

export default DashBoard
