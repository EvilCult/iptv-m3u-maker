import React, { useState, useEffect, useImperativeHandle, forwardRef } from 'react'
import {
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
  Search as SearchIcon,
  MoreVert as MoreVertIcon,
} from '@mui/icons-material'
import lang from '@/libs/langs'


interface TableRowsProps {
  readonly id: number,
  readonly title: string,
  readonly alive: number,
  readonly ping: number,
  readonly url: string,
  recall?: any
}
const TableRows = (props: TableRowsProps) => {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null)
  const open = Boolean(anchorEl)

  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget)
  }
  const handleClose = () => {
    setAnchorEl(null)
  }

  const handleEdit = () => {
    handleClose()
    props?.recall(true)
  }

  return (
    <React.Fragment>
      <TableRow
        key={props.id}
      >
        <TableCell component="th" scope="row" width={80}>
          {props.id}
        </TableCell>
        <TableCell
          align="left"
          sx={{
            minWidth: 200,
          }}
        >{props.title}</TableCell>
        <TableCell align="center" width={300}>{props.url}</TableCell>
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
        onClick={handleEdit}
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
            '.MuiMenuItem-root':  {
              width: 150,
            }
          },
        }}
        transformOrigin={{ horizontal: 'right', vertical: 'top' }}
        anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
      >
        <MenuItem>
          <ListItemIcon>
            <EditIcon fontSize="small" />
          </ListItemIcon>
          <ListItemText>Edit</ListItemText>
        </MenuItem>
        <MenuItem>
          <ListItemIcon>
            <SpeedIcon fontSize="small" />
          </ListItemIcon>
          <ListItemText>Ping</ListItemText>
        </MenuItem>
        <MenuItem>
          <ListItemIcon>
            <DeleteForeverIcon fontSize="small" />
          </ListItemIcon>
          <ListItemText>Del</ListItemText>
        </MenuItem>
      </Menu>
    </React.Fragment>
  )
}

interface DataTableProps {
  readonly header: any,
  readonly page: number,
  readonly limit: number,
  readonly count: number,
  readonly list: any,
  readonly loading: boolean,
  readonly setUpdate: any,
  readonly handleChangePage: any,
  readonly handleChangeRowsPerPage: any,
}
const DataTable = (props: any, ref: React.Ref<any>) => {
  useImperativeHandle(ref, () => ({
  }))

  return (
    <Paper sx={{ width: '100%', mb: 2 }}>
      <TableContainer>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell colSpan={6} align='right'>
                <Paper
                  component="form"
                  sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: '100%' }}
                >
                  <SearchIcon sx={{ p: '2px' , ml: '4px'}} color="disabled"/>
                  <InputBase
                    sx={{ ml: 1, flex: 1 }}
                    placeholder="Search"
                    inputProps={{
                      'aria-label': 'search',
                      onKeyPress: (event) => {
                        if (event.key === 'Enter') {
                          event.preventDefault()
                        }
                      }
                    }}
                  />
                  <Divider sx={{ height: 28, m: 0.5 }} orientation="vertical" />
                  <IconButton sx={{ p: '10px' }} aria-label="directions">
                    <MoreVertIcon />
                  </IconButton>
                </Paper>
              </TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow>
              {props.header.map((column: any) => (
                <TableCell
                  key={column.id}
                  align={column.align}
                  sx={{ minWidth: column?.minWidth }}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          {
            props.loading && props.list.length === 0 ?
            <TableRow>
              <TableCell colSpan={6}>
                <Skeleton variant="rectangular" height={100} />
              </TableCell>
            </TableRow>
            :
            props.list.map((row: any) => (
              <TableRows
                key={row.id}
                id={row.id}
                title={row.title}
                alive={row.alive}
                ping={row.ping}
                url={row.url}
                recall={props.setUpdate}
              />
            ))
          }
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
          rowsPerPageOptions={[10, 20, 50]}
          component="div"
          count={props.count}
          rowsPerPage={props.limit}
          page={props.page}
          onPageChange={props.handleChangePage}
          onRowsPerPageChange={props.handleChangeRowsPerPage}
      />
    </Paper>
  )
}

export default forwardRef(DataTable)
