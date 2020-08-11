import React, { Component } from 'react'

import { Drawer, List, Divider, ListItem, ListItemIcon, ListItemText } from '@material-ui/core'
import { List as ListIcon, Settings } from '@material-ui/icons'

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
            <ListItemIcon><ListIcon /></ListItemIcon>
            <ListItemText primary='数据管理' />
          </ListItem>
        </List>
        <Divider />
        <List>
          <ListItem button>
            <ListItemIcon><Settings /></ListItemIcon>
            <ListItemText primary='设置' />
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
