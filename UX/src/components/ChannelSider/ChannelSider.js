import React, { Component } from 'react'

import {
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Divider,
} from '@material-ui/core'

import {
  Inbox as InboxIcon,
  AddBox as AddBoxIcon,
  Cached as CachedIcon,
} from '@material-ui/icons'
import './ChannelSider.less'

class ChannelSider extends Component {
  constructor(props) {
    super(props)

    this.state = {}
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
          <ListItem button>
            <ListItemIcon><AddBoxIcon /></ListItemIcon>
            <ListItemText primary="Add" />
          </ListItem>
          <Divider />
          <ListItem button>
            <ListItemIcon><CachedIcon /></ListItemIcon>
            <ListItemText primary="Initialize" />
          </ListItem>
          <Divider />
        </List>
      </React.Fragment>
    )
  }
}

export default ChannelSider
