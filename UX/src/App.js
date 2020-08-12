import React, { Component } from 'react'
import { Provider } from 'react-redux'
import { HashRouter as Router, Switch, Route, Redirect } from 'react-router-dom'

import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles'
import { blue, pink } from '@material-ui/core/colors'

import History from '@/store/History'
import Store from '@/store/Store'

import Home from '@/pages/Home/Home'

const storeSetting = Store()

const theme = createMuiTheme({
  palette: {
    primary: blue,
    secondary: pink,
  },
})

class App extends Component {
  constructor(props) {
    super(props)

    this.state = {}
  }

  render() {
    return (
      <Provider store={storeSetting}>
        <ThemeProvider theme={theme}>
          <Router BrowserHistory={History} basename="/">
            <Switch>
              <Route path="/home" component={Home} />
              <Redirect to="/home" />
            </Switch>
          </Router>
        </ThemeProvider>
      </Provider>
    )
  }
}

export default App;
