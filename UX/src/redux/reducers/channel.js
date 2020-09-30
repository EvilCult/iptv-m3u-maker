import Types from '@/redux/constants/channel'

const initState = {
  list   : {},
  count  : 0,
  loading: false,
  err    : 0,
  ts     : 0,
}

export default function channel (state = initState, action) {
  switch (action.type) {
    case Types.CHANNEL_LIST:
      return list(state, action)

    case Types.CHANNEL_LOADING:
      return loading(state)

    case Types.CHANNEL_ERR:
      return err(state, action)

    case Types.CHANNEL_CLEANERR:
      return cleanErr(state)

    default:
      return state
  }
}

const list = (state, action) => {
  const now = parseInt((new Date()).valueOf())

  let list = {...state.list}
  list[action.page] = action.data

  return {
    ...state,
    list   : list,
    count  : action.count,
    loading: false,
    ts     : now
  }
}

const loading = (state) => {
  const now = parseInt((new Date()).valueOf())

  return {
    ...state,
    loading: true,
    ts: now,
  }
}

const err = (state, action) => {
  const now = parseInt((new Date()).valueOf())

  return {
    ...state,
    err: action.errCode,
    count : state.list.length,
    loading: false,
    ts: now
  }
}

const cleanErr = (state) => {
  const now = parseInt((new Date()).valueOf())

  return {
    ...state,
    err: 0,
    ts: now,
  }
}
