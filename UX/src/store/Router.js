import React, { Component } from 'react'
import { Route, Redirect, Switch } from 'react-router-dom'
import Loadable from 'react-loadable'

import { CircularProgress } from '@material-ui/core'

import E404 from '@/pages/Err/E404'
import E500 from '@/pages/Err/E500'

class Router extends Component {
  constructor (props) {
    super(props)

    this.state = {}
  }

  loadingComponent ({ isLoading, error }) {
    if (isLoading) {
      return (
        <div style={{marginTop:'250px',textAlign:'center',}}>
          <CircularProgress />
        </div>
      )
    } else if (error) {
      return (<E500 />)
    } else {
      return (<E404 />)
    }
  }

  render () {
    const Index = Loadable({
      loader: () => import( '@/pages/Index/Index'),
      loading: this.loadingComponent
    })

    const SourceList = Loadable({
      loader: () => import( '@/pages/SourceList/SourceList'),
      loading: this.loadingComponent
    })

    const ChannelList = Loadable({
      loader: () => import( '@/pages/ChannelList/ChannelList'),
      loading: this.loadingComponent
    })

    const E404 = Loadable({
      loader: () => import( '@/pages/Err/E404'),
      loading: this.loadingComponent
    })

    const E500 = Loadable({
      loader: () => import( '@/pages/Err/E500'),
      loading: this.loadingComponent
    })

    return (
      <Switch>
        <Route exact path="/home" component={Index}/>
        <Route exact path="/home/sources/list" component={SourceList}/>
        <Route exact path="/home/channel/list" component={ChannelList}/>

        <Route exact path="/home/err/404" component={E404}/>
        <Route exact path="/home/err/500" component={E500}/>
        <Redirect to='/home/err/404'/>
      </Switch>
    )
  }
}

export default Router
