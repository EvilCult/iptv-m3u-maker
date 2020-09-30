import { combineReducers } from 'redux'

import sources from './sources'
import channel from './channel'

export default combineReducers({
  sourcesState: sources,
  channelState: channel,
})
