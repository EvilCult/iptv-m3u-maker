import React, { Component } from 'react'

import { Typography, Button } from '@material-ui/core'
import { } from '@material-ui/icons'

import './Err.less'

class E500 extends Component {
  constructor(props) {
    super(props)

    this.state = {}
  }

  render() {
    return (
      <div className='Error'>
        <Typography
          variant="h5"
          color="inherit"
        >
          500
        </Typography>
        <Typography
          variant="subtitle2"
          color="inherit"
          className='font'
        >
          Internal server error.
        </Typography>
        <Typography
          variant="body2"
          color="inherit"
          className='font'
        >
          The server encountered something unexpected that didn't allow it to complete the request.
        </Typography>
        <Button variant="contained" color="primary" className='btn' onClick={this.goHome}>
          Return to Home
        </Button>
      </div>
    )
  }

  goHome = () => {
    this.props.history.push('/home')
  }
}

export default E500
