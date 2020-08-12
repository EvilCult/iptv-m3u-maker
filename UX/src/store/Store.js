import { createStore, applyMiddleware } from 'redux'
import thunkMiddleware from 'redux-thunk'
import { createLogger } from 'redux-logger'
import rootReducer from '@/redux/reducers'

const middlewares = [
  thunkMiddleware,
  createLogger({collapsed:true})
]

export default function Store () {
  const store = createStore(rootReducer, applyMiddleware(...middlewares))
  return store
}
