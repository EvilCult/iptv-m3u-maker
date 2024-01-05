import React, { useState, useEffect } from 'react'

import {
  Box,
  Drawer,
  AppBar,
  Toolbar,
  IconButton,
  List,
  Typography,
  Divider,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
} from '@mui/material'

import {
  MoveToInbox as InboxIcon,
  Mail as MailIcon,
  Menu as MenuIcon,
} from '@mui/icons-material'

const AppHeader = () => {
  const [open, setOpen] = useState(true)
  const [drawerWidth, setDrawerWidth] = useState(240)

  useEffect(() => {
    const sidebar = localStorage.getItem('sidebar') || 'true'
    if (sidebar === 'true') {
      setOpen(true)
    } else {
      setOpen(false)
    }
  }, [])

  useEffect(() => {
    if (open) {
      setDrawerWidth(240)
      localStorage.setItem('sidebar', 'true')
    } else {
      setDrawerWidth(65)
      localStorage.setItem('sidebar', 'false')
    }
  }, [open])

  const handleToggle = () => {
    setOpen(!open)
  }

  return (
    <React.Fragment>
        <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
            onClick={handleToggle}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap component="div">
            IPTV Maker
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
        }}
        anchor="left"
        open={open}
      >
        <Toolbar />
        <Box sx={{ overflow: 'auto' }}>
          <List>
            <ListItem key='list_a' disablePadding sx={{ display: 'block' }} >
              <ListItemButton
                sx={{
                  minHeight: 48,
                  justifyContent: open ? 'initial' : 'center',
                  px: 2.5,
                }}
              >
                <ListItemIcon
                  sx={{
                    minWidth: 0,
                    mr: open ? 3 : 'auto',
                    justifyContent: 'center',
                  }}
                >
                 <InboxIcon />
                </ListItemIcon>
                <ListItemText primary={ open ? "List Item A" : '' }  />
              </ListItemButton>
            </ListItem>
          </List>
          <Divider />
          <List>
            <ListItem key='list_b' disablePadding sx={{ display: 'block' }} >
              <ListItemButton
                sx={{
                  minHeight: 48,
                  justifyContent: open ? 'initial' : 'center',
                  px: 2.5,
                }}
              >
                <ListItemIcon
                  sx={{
                    minWidth: 0,
                    mr: open ? 3 : 'auto',
                    justifyContent: 'center',
                  }}
                >
                 <MailIcon />
                </ListItemIcon>
                <ListItemText primary={ open ? "List Item B" : '' }  />
              </ListItemButton>
            </ListItem>

          </List>
        </Box>
      </Drawer>
    </React.Fragment>
  )
}

export default AppHeader
