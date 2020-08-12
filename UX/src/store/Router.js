import React, { Component } from 'react'
import { Route, Redirect, Switch } from 'react-router-dom'
import Loadable from 'react-loadable'

import { CircularProgress } from '@material-ui/core'

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
      console.log('500')
    } else {
      console.log('404')
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

    return (
      <Switch>
        <Route exact path="/home" component={Index}/>
        <Route exact path="/home/sources/list" component={SourceList}/>

        {/* <Route exact path="/home/err/404" component={E404}/>
        <Redirect to='/home/err/404'/> */}
      </Switch>
    )
  }
}

export default Router
