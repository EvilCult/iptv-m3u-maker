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
  Avatar,
} from '@mui/material'
import {
  Tune as TuneIcon,
} from '@mui/icons-material'
import AppHeader from '@/components/appheader'
import Copyright from '@/components/appfooter'
import useChannelList from '@/hooks/channel/listHook'
import lang from '@/libs/langs'

const DataTable = () => {
  const [page, setPage] = useState(0)
  const [limit, setLimit] = useState(10)
  const [count, setCount] = useState(0)
  const [list, setlist] = useState([])
  const {loading, data, msg, setMsg} = useChannelList(page + 1, limit)

  useEffect(() => {
    if (!loading && msg === 'suc') {
      setlist(data.data.list)
      setCount(data.data.count)
    }
  }, [loading, data, msg])


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
    <Paper sx={{ width: '100%', mb: 2 }}>
      <TableContainer>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell align="left">{lang('page_channel_list_title')}</TableCell>
              <TableCell align="right">{lang('page_channel_list_stat')}</TableCell>
              <TableCell align="right">{lang('page_channel_list_ping')}</TableCell>
              <TableCell align="right"></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
          {
            loading ?
            <TableRow>
              <TableCell colSpan={4}>
                <Skeleton variant="rectangular" height={100} />
              </TableCell>
            </TableRow>
            :
            list.map((row: any) => (
              <TableRows
                key={row.id}
                id={row.id}
                title={row.title}
                alive={row.alive}
                ping={row.ping}
              />
            ))
          }
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
          rowsPerPageOptions={[10, 20, 50]}
          component="div"
          count={count}
          rowsPerPage={limit}
          page={page}
          onPageChange={handleChangePage}
          onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </Paper>
  )
}

interface TableRowsProps {
  readonly id: number,
  readonly title: string,
  readonly alive: number,
  readonly ping: number,
}
const TableRows = (props: TableRowsProps) => {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl)
  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget)
  };
  const handleClose = () => {
    setAnchorEl(null)
  };

  return (
    <React.Fragment>
      <TableRow
        key={props.id}
      >
        <TableCell component="th" scope="row" width={80}>
          {props.id}
        </TableCell>
        <TableCell align="left" width={300}>{props.title}</TableCell>
        <TableCell align="right">{
          props.alive === 1 && props.ping !== 0
          ? <Chip size="small" label={lang('channel_stat_alive')} color="success" />
          : <Chip size="small" label={lang('channel_stat_dead')} color="error" />
        }</TableCell>
        <TableCell align="right">{props.ping}</TableCell>
        <TableCell align="right">
        <IconButton
          onClick={handleClick}
          size="small"
          sx={{ ml: 2 }}
          aria-controls={open ? 'account-menu' : undefined}
          aria-haspopup="true"
          aria-expanded={open ? 'true' : undefined}
        >
          <TuneIcon sx={{ width: 24, height: 24 }} />
        </IconButton>
        </TableCell>
      </TableRow>
      <Menu
        anchorEl={anchorEl}
        id="account-menu"
        open={open}
        onClose={handleClose}
        onClick={handleClose}
        PaperProps={{
          elevation: 0,
          sx: {
            overflow: 'visible',
            filter: 'drop-shadow(0px 2px 8px rgba(0,0,0,0.32))',
            mt: 1.5,
            '& .MuiAvatar-root': {
              width: 32,
              height: 32,
              ml: -0.5,
              mr: 1,
            },
            '&::before': {
              content: '""',
              display: 'block',
              position: 'absolute',
              top: 0,
              right: 14,
              width: 10,
              height: 10,
              bgcolor: 'background.paper',
              transform: 'translateY(-50%) rotate(45deg)',
              zIndex: 0,
            },
          },
        }}
        transformOrigin={{ horizontal: 'right', vertical: 'top' }}
        anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
      >
        <MenuItem onClick={handleClose}>
            Profile
        </MenuItem>
      </Menu>
    </React.Fragment>
  )
}

const ChannelList = () => {
  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppHeader />
      <Box component="main" sx={{ flexGrow: 1, p: 3, display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <Toolbar />
        <DataTable />
        <Box sx={{ mt: 'auto' , p: 2}}><Copyright /></Box>
      </Box>
    </Box>
  )
}

export default ChannelList
