import React, { Component } from 'react'

import { AppBar, Toolbar, IconButton, Typography } from '@material-ui/core'
import { Menu } from '@material-ui/icons'

import './AppHeader.less'

class AppHeader extends Component {
  constructor(props) {
    super(props)

    this.state = {
      siderToggle: this.props.toggle
    }
  }

  render() {
    return (
      <AppBar position="fixed" className='AppHeader'>
        <Toolbar variant="dense">
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            onClick={this.state.siderToggle}
          >
            <Menu />
          </IconButton>
          <div className='brand'>
            <Typography
              variant="h6"
              color="inherit"
              onClick={this.goBack}
            >
              FoxHound
            </Typography>
          </div>
        </Toolbar>
      </AppBar>
    )
  }

  goBack = () => {
    this.props.history.push('/home')
  }
}

export default AppHeader
