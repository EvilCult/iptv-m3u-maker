import React, { Component } from 'react'

import {
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Divider,
  Button,
  IconButton,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Snackbar,
} from '@material-ui/core'
import {
  Inbox as InboxIcon,
  Cached as CachedIcon,
  Close as CloseIcon,
} from '@material-ui/icons'
import './ChannelSider.less'

class ChannelSider extends Component {
  constructor(props) {
    super(props)

    this.state = {
      notice: false,
      noticeMsg: '',
      dialog: false
    }
  }

  render() {
    return (
      <React.Fragment>
        <List dense={true}>
          <Divider />
          <ListItem button>
            <ListItemIcon><InboxIcon /></ListItemIcon>
            <ListItemText primary="List" />
          </ListItem>
          <Divider />
          <ListItem button onClick={this.handleDialogOpen}>
            <ListItemIcon><CachedIcon /></ListItemIcon>
            <ListItemText primary="Initialize" />
          </ListItem>
          <Divider />
        </List>
        {this.renderNotice()}
        {this.renderDialog()}
      </React.Fragment>
    )
  }

  renderNotice() {
    return (
      <Snackbar
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'center',
        }}
        open={this.state.notice}
        autoHideDuration={5000}
        onClose={this.handleNoticeClose}
        message={this.state.noticeMsg}
        action={
          <React.Fragment>
            <IconButton size="small" aria-label="close" color="inherit" onClick={this.handleNoticeClose}>
              <CloseIcon fontSize="small" />
            </IconButton>
          </React.Fragment>
        }
      />
    )
  }

  renderDialog() {
    return (
      <Dialog
        open={this.state.dialog}
        onClose={this.handleDialogClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"确认初始化频道信息?"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            初始化频道信息将会更新国内频道相关名称,logo分类等信息.<br /><br />
            注意:此操作需要大量时间下载logo图片.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={this.handleDialogClose} color="primary">
            取消
          </Button>
          <Button onClick={this.handleInit} color="primary" autoFocus>
            更新
          </Button>
        </DialogActions>
      </Dialog>
    )
  }

  handleNoticeOpen = (msg) => {
    this.setState({
      notice:true,
      noticeMsg:msg
    })
  }

  handleNoticeClose = () => {
    this.setState({
      notice:false
    })
  }

  handleDialogOpen = () => {
    this.setState({
      dialog:true
    })
  }

  handleInit = () => {
    this.setState({
      dialog:false
    },() => {
      this.runInit()
    })
  }

  handleDialogClose = () => {
    this.setState({
      dialog:false
    })
  }

  runInit = () => {
    fetch("/bot/channel/run", {
      method : 'get',
      mode   : 'cors',
    })
    .then(res => res.json())
    .then(resData => {
      if (parseInt(resData.err) === 0) {
        this.handleNoticeOpen('开始更新频道信息...')
      } else {
        this.handleNoticeOpen('数据正在更新中,请稍后...')
      }
    })
  }
}

export default ChannelSider
