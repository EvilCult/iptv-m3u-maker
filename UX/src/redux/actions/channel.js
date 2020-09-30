import Types from '@/redux/constants/channel'

export const list = (p = 1) => {
  return dispatch => {
    dispatch(loading())

    fetch("/channel/list/" + p, {
      method : 'get',
      mode   : 'cors',
    })
    .then(res => res.json())
    .then(resData => {
      if (parseInt(resData.err) === 0) {
        dispatch(getListSuc(resData.data, resData.count, p))
      } else {
        dispatch(err(resData.err))
      }
    })
    .catch(() => {dispatch(err('990101'))})
  }
}

export const getListSuc = (data, count, page) => {
  return {
    type   : Types.CHANNEL_LIST,
    page   : page,
    data   : data,
    count  : count,
    loading: false,
  }
}

export const loading = () => {
  return {
    type: Types.CHANNEL_LOADING
  }
}

export const cleanErr = () => {
  return {
    type: Types.CHANNEL_CLEANERR,
  }
}

export const err = (code) => {
  return {
    type: Types.CHANNEL_ERR,
    errCode: code,
  }
}

