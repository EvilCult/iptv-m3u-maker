import React, { useState, useImperativeHandle, forwardRef } from 'react'
import {
  Alert,
  Snackbar,
  AlertColor
} from '@mui/material'

const Notify = (props: any, ref: React.Ref<any>) => {
  const [open, setOpen] = useState(false)
  const [msg, setMsg] = useState('')
  const [color, setColor] = useState<AlertColor>('info')


  const handleNoticeOpen = (msg: string, typ: string = 'info') => {
    let nTyp = ''
    switch (typ) {
      case 'suc':
        setColor('success')
        break
      case 'err':
        setColor('error')
        break
      case 'info':
        setColor('info')
        break
      default:
        setColor('info')
    }
    setOpen(true)
    setMsg(msg)
  }

  const handleNoticeClose = () => {
    setOpen(false)
    setMsg('')
  }

  useImperativeHandle(ref, () => ({
    handleNoticeOpen: handleNoticeOpen,
  }))


  return (
    <Snackbar
      anchorOrigin={{
        vertical: 'top',
        horizontal: 'right'
      }}
      open={open}
      autoHideDuration={6000}
      onClose={handleNoticeClose}
    >
      <Alert variant="filled" onClose={handleNoticeClose} severity={color} sx={{ width: '100%' }}>
      {msg}
      </Alert>
    </Snackbar>
  )
}

export default forwardRef(Notify)

