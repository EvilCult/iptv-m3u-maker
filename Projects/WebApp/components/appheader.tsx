import React, { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
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
  OndemandVideo as VideoIcon
} from '@mui/icons-material'
import lang from '@/libs/langs'


const AppHeader = () => {
  const [open, setOpen] = useState(true)
  const [drawerWidth, setDrawerWidth] = useState(240)
  const router = useRouter()

  useEffect(() => {
    const uInfo = localStorage.getItem('uInfo')
    if (uInfo === null) {
      router.push('/login')
    } else {
      const uInfoJson = JSON.parse(uInfo)
      if (
        uInfoJson.exp < Date.now() / 1000
        || uInfoJson.iat > Date.now() / 1000
        || uInfoJson.iss !== 'EvilCult'
      ) {
        router.push('/login')
      }
    }
  })

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

  const handelGoto = (url: string) => {
    if (url !== '') {
      router.push(url)
    }
  }

  interface ListItemLinkProps {
    icon?: React.ReactElement
    primary: string
    to: string
  }
  const ListItemLink = (props: ListItemLinkProps) => {
    const { icon, primary, to } = props

    return (
      <ListItem key={primary} disablePadding sx={{ display: 'block' }}>
        <ListItemButton
          sx={{
            minHeight: 48,
            justifyContent: open ? 'initial' : 'center',
            px: 2.5,
          }}
          onClick={ () => handelGoto(to) }
        >
          {icon ? <ListItemIcon
            sx={{
              minWidth: 0,
              mr: open ? 3 : 'auto',
              justifyContent: 'center',
            }}
          >
          {icon}
          </ListItemIcon> : null}
          <ListItemText primary={ open ? primary : '' }  />
        </ListItemButton>
      </ListItem>
    )
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
            <ListItemLink icon={<VideoIcon />} primary={lang('menu_channel_list')} to='/channel/list' />
          </List>
          <Divider />
          <List>
            <ListItemLink icon={<InboxIcon />} primary='test message' to='' />
          </List>
        </Box>
      </Drawer>
    </React.Fragment>
  )
}

export default AppHeader
