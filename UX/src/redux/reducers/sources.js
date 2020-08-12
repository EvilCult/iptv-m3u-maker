import Types from '@/redux/constants/sources'

const initState = {
  source : {},
  list   : [],
  count  : 0,
  exp    : 0,
  loading: false,
  err    : 0,
  ts     : 0,
}

export default function sources (state = initState, action) {
  switch (action.type) {
    case Types.SOURCES_LIST:
      return list(state, action)

    case Types.SOURCES_LOADING:
      return loading(state)

    case Types.SOURCES_ERR:
      return err(state, action)

    case Types.SOURCES_CLEANERR:
      return cleanErr(state)

    default:
      return state
  }
}

const list = (state, action) => {
  const now = parseInt((new Date()).valueOf())

  let source = {...state.source}
  let idList = []
  action.data.forEach((item) => {
    const id = item.id
    source[id] = item
    idList.push(id)
  })

  return {
    ...state,
    source : source,
    list   : idList,
    count  : action.count,
    exp    : action.expires,
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
