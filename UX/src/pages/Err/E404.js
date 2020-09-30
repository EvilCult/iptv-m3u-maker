import React, { Component } from 'react'

import { Typography, Button } from '@material-ui/core'
import { } from '@material-ui/icons'

import './Err.less'

class E404 extends Component {
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
          404
        </Typography>
        <Typography
          variant="subtitle2"
          color="inherit"
          className='font'
        >
          Page not found.
        </Typography>
        <Typography
          variant="body2"
          color="inherit"
          className='font'
        >
          The page you are looking for might have been removed.
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

export default E404
