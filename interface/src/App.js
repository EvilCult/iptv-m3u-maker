import React, { Component } from 'react'
import { Provider } from 'react-redux'
import { HashRouter as Router, Switch, Route, Redirect } from 'react-router-dom'

import History from '@/store/History'
import Store from '@/store/Store'

import Home from '@/pages/Home/Home'

const storeSetting = Store()

class App extends Component {
  constructor(props) {
    super(props)

    this.state = {}
  }

  render() {
    return (
      <Provider store={storeSetting}>
        <Router BrowserHistory={History} basename="/">
          <Switch>
            <Route exact path="/home" component={Home} />
            <Redirect to="/home" />
          </Switch>
        </Router>
      </Provider>
    )
  }
}

export default App;
