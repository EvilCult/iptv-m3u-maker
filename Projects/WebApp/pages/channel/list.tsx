import React, { useState, useEffect } from 'react'
import {
  Box,
  CssBaseline,
  Toolbar,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TablePagination,
  TableHead,
  TableRow,
  Paper,
  Skeleton,
  Chip,
  IconButton,
  Menu,
  MenuItem,
  ListItemIcon,
  ListItemText,
  InputBase,
  Divider,
} from '@mui/material'
import {
  Tune as TuneIcon,
  DeleteForever as DeleteForeverIcon,
  Edit as EditIcon,
  Speed as SpeedIcon,
  Menu as MenuIcon,
  Search as SearchIcon,
  MoreVert as MoreVertIcon,
} from '@mui/icons-material'
import AppHeader from '@/components/appheader'
import Copyright from '@/components/appfooter'
import DataTable from '@/components/datatable'
import useChannelList from '@/hooks/channel/listHook'
import lang from '@/libs/langs'

const DataBox = () => {
  const [page, setPage] = useState(0)
  const [limit, setLimit] = useState(10)
  const [count, setCount] = useState(0)
  const [list, setlist] = useState([])
  const [update, setUpdate] = useState(false)
  const {loading, data, msg, setMsg} = useChannelList(page + 1, limit)

  useEffect(() => {
    if (!loading && msg === 'suc') {
      setlist(data.data.list)
      setCount(data.data.count)
    }
  }, [loading, data, msg])

  useEffect(() => {
    if (update){
      const newPage = page
      setPage(-1)
      setUpdate(false)
      setTimeout(() => {
        setPage(newPage)
      }, 500)
    }
  }, [page, update])

  const header = [
    { id: 'id ', label: 'ID' },
    { id: 'title', align: 'left', label: lang('page_channel_list_title') },
    { id: 'url', align: 'center', label: 'URL' },
    { id: 'alive', align: 'right', label: lang('page_channel_list_stat') },
    { id: 'ping', align: 'right', label: lang('page_channel_list_ping') },
    { id: 'option'},
  ]

  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage)
  }

  const handleChangeRowsPerPage = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setLimit(parseInt(event.target.value, 10))
    setPage(0)
  }


  return (
    <DataTable
      header={header}
      list={list}
      count={count}
      page={page}
      limit={limit}
      loading={loading}
      update={update}
      setUpdate={setUpdate}
      handleChangePage={handleChangePage}
      handleChangeRowsPerPage={handleChangeRowsPerPage}
    />
  )
}


const ChannelList = () => {
  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppHeader />
      <Box component="main" sx={{ flexGrow: 1, p: 3, display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <Toolbar />
        <Box sx={{ mb: 2}}>
          <Typography variant="h6" gutterBottom> {lang('menu_channel_list')} </Typography>
        </Box>
        <CssBaseline />
        <DataBox />
        <Box sx={{ mt: 'auto' , p: 2}}><Copyright /></Box>
      </Box>
    </Box>
  )
}

export default ChannelList
