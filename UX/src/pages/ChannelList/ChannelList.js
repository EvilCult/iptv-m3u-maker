import React, { Component } from 'react'
import { connect } from 'react-redux'

import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TablePagination,
  Drawer,
  Toolbar,
  Paper,
  Avatar,
  CircularProgress,
} from '@material-ui/core'
import { InsertPhoto as LogoIcon } from '@material-ui/icons'

import Sider from '@/components/ChannelSider/ChannelSider'
import * as ChannelAct from '@/redux/actions/channel'

import './ChannelList.less'

class ChannelList extends Component {
  constructor(props) {
    super(props)

    this.state = {
      cur: 1,
      data: [],
      count: 0,
      loading: false,
    }
  }

  static getDerivedStateFromProps (nextProps, prevState) {
    const state = nextProps.channelState

    if (!prevState.loading && state.loading) {
      return {
        ...prevState,
        loading: true,
      }
    }

    if (prevState.loading && typeof(state.list[prevState.cur]) !== 'undefined') {
      return {
        ...prevState,
        data: state.list[prevState.cur],
        count: state.count,
        loading: false,
      }
    }

    return null
  }

  render() {
    return (
      <div className='ChannelList'>
        <Drawer
          variant="permanent"
          className='menu'
        >
          <Toolbar />
          <Sider />
        </Drawer>
        <div className='content'>
          {this.state.loading
            ? (
              <div className='loading'>
                <CircularProgress />
              </div>
            )
            : this.renderTable()
          }
        </div>
      </div>
    )
  }

  renderTable() {
    return (
      <Paper className='table'>
        <TableContainer>
          <Table aria-label="Channel List">
            <TableHead>
              <TableRow>
                <TableCell align="right">No.</TableCell>
                <TableCell>Icon</TableCell>
                <TableCell>Title</TableCell>
                <TableCell>Alias</TableCell>
                <TableCell>Group</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {this.state.data.map((row) => (
                <TableRow key={row.id}>
                  <TableCell component="th" scope="row" align="right">
                    {row.num}
                  </TableCell>
                  <TableCell>
                    <Avatar src={row.icon} className='logo'>
                      <LogoIcon />
                    </Avatar>
                  </TableCell>
                  <TableCell>{row.title}</TableCell>
                  <TableCell>{row.alias}</TableCell>
                  <TableCell>{row.group}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
        <TablePagination
          rowsPerPageOptions={[]}
          component="div"
          count={this.state.count}
          rowsPerPage={20}
          page={parseInt(this.state.cur) - 1}
          onChangePage={this.handleChangePage}
        />
      </Paper>
    )
  }

  componentDidMount() {
    this.props.list(1)
  }

  handleChangePage = (e, page) => {
    const newPage = parseInt(page) + 1
    this.setState({
      cur: newPage
    })
    this.props.list(newPage)
  }
}

export default connect(
  (state) => ({
    channelState: state.channelState,
  }),
  (dispatch) => ({
    list: (p) => dispatch(ChannelAct.list(p)),
  })
)(ChannelList)
