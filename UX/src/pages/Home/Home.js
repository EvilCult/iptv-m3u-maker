import React, { Component } from 'react'

import { } from '@material-ui/core'
import { } from '@material-ui/icons'

import AppHeader from '@/components/AppHeader/AppHeader'
import AppSider from '@/components/AppSider/AppSider'
import RouteCfg from '@/store/Router'

import './Home.less'

class Home extends Component {
  constructor(props) {
    super(props)

    this.state = {
      showSider: false
    }
  }

  render() {
    return (
      <div className='Home'>
        <AppHeader
          toggle={this.toggleSider}
          history={this.props.history}
        />
        <AppSider
          isOpen={this.state.showSider}
          closeSider={this.closeSider}
          history={this.props.history}
        />
        <div className='wrap'>
          <RouteCfg />
        </div>
      </div>
    )
  }

  toggleSider = () => {
    this.setState({
      showSider: !this.state.showSider
    })
  }

  closeSider = () => {
    this.setState({
      showSider: false
    })
  }
}

export default Home
