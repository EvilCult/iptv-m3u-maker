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
      return (<div>404</div>)
    } else {
      return (<div>404</div>)
    }
  }

  render () {
    let Index = Loadable({
      loader: () => import( 'pages/Index/Index'),
      loading: this.loadingComponent
    })

    return (
      <Switch>
        <Route exact path="/home" component={Index}/>
        {/* <Route exact path="/home/err/404" component={E404}/>
        <Redirect to='/home/err/404'/> */}
      </Switch>
    )
  }
}

export default Router
