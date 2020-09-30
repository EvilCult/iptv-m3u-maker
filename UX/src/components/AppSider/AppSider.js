import React, { Component } from 'react'

import { Drawer, List, Divider, ListItem, ListItemIcon, ListItemText } from '@material-ui/core'
import {
  List as ListIcon,
  Settings as SettingIcon,
  AssignmentReturned as AssignmentReturnedIcon,
  Announcement as AnnouncementIcon,
  Subscriptions as SubscriptionsIcon,
} from '@material-ui/icons'

import './AppSider.less'

class AppSider extends Component {
  constructor(props) {
    super(props)

    this.state = {
      close: this.props.closeSider
    }
  }

  render() {
    const list = (
      <div
        className='AppSider'
        onClick={this.state.close}
      >
        <List>
          <ListItem
            button
            onClick={() => this.goTo('/home/sources/list')}
          >
            <ListItemIcon><SubscriptionsIcon /></ListItemIcon>
            <ListItemText primary='Media' />
          </ListItem>
          <ListItem
            button
            onClick={() => this.goTo('/home/channel/list')}
          >
            <ListItemIcon><ListIcon /></ListItemIcon>
            <ListItemText primary='Channels' />
          </ListItem>
        </List>
        <Divider />
        <List>
          <ListItem button>
            <ListItemIcon><AssignmentReturnedIcon /></ListItemIcon>
            <ListItemText primary='Spiders' />
          </ListItem>
          <ListItem button>
            <ListItemIcon><AnnouncementIcon /></ListItemIcon>
            <ListItemText primary='Alerts' />
          </ListItem>
        </List>
        <Divider />
        <List>
          <ListItem button>
            <ListItemIcon><SettingIcon /></ListItemIcon>
            <ListItemText primary='Settings' />
          </ListItem>
        </List>
      </div>
      )
    return (
      <Drawer
        open={this.props.isOpen}
        onClose={this.state.close}
      >
        {list}
      </Drawer>
    )
  }

  goTo = (path) => {
    this.props.history.push(path)
  }
}

export default AppSider
