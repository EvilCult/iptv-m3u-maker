import React, { useState, useEffect, useImperativeHandle, forwardRef } from 'react'
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

const Test = (props: any, ref: React.Ref<any>) => {
  const [num, setNum] = useState(0)

  const handleAdd = () => {
    setNum(num + 1)
  }

  useEffect(() => {
    if (props.start) {
      setNum(props.start)
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  },[])

  useImperativeHandle(ref, () => ({
    handleAdd: handleAdd,
  }))


  return (
    <Card sx={{ minWidth: 275 }}>
      <CardContent>
        <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
          Click Time
        </Typography>
        <Typography variant="h5" component="div">
          {num}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Learn More</Button>
      </CardActions>
    </Card>
  )
}

export default forwardRef(Test)

