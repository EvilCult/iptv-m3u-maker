import { useState, useEffect } from 'react'

import * as ChannelApi from '@/api/channelApi'
import lang from '@/libs/langs'

const useChannelList = (page = 1, limit = 20) => {

  interface DataTyp {
    code: number;
    data: any;
    msg: string;
    time: number;
  }

  const [msg, setMsg] = useState('')
  const [data, setData] = useState<DataTyp>({code:1, data:null, msg:'', time:0 })
  const [loading, setLoading] = useState(false)

  const req = () => {
    let cancel = false
    setLoading(true)

    const response = ChannelApi.list(page, limit)
    response.then(
      res => {
        if (!cancel) {
          if (parseInt(res.code) === 0) {
            setData(res)
            setMsg('suc')
          } else {
            setMsg(lang(res.msg))
          }
        }
      },
      () => {
        if (!cancel) {
          setMsg(lang('network_error'))
        }
      }
    )
    .finally(() => {
      if (!cancel) {
        setLoading(false)
      }
    })

    return () => {
      cancel = true
    }
  }

  useEffect(() => {
    if (page > 0) {
      const cancelRequest = req()

      return () => {
        cancelRequest()
      }
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [page])

  return {loading, data, msg, setMsg}
}


export default useChannelList
