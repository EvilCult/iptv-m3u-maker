import Types from '@/redux/constants/sources'
import SysConfig from '@/store/Config'

const cacheExpires = 60 * 60 * 2

export const list = (p = 1, ps = 10, rec = 0) => {
  return dispatch => {
    dispatch(loading())
  }
}

export const loading = () => {
  return {
    type: Types.SOURCES_LOADING
  }
}

export const cleanErr = () => {
  return {
    type: Types.SOURCES_CLEANERR,
  }
}

export const err = (code) => {
  return {
    type: Types.SOURCES_ERR,
    errCode: code,
  }
}

