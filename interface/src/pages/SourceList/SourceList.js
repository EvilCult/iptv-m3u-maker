import React, { Component } from 'react'

import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@material-ui/core'
import { } from '@material-ui/icons'

import './SourceList.less'

class SourceList extends Component {
  constructor(props) {
    super(props)

    this.state = {}
  }

  render() {
    const data = [
      this.fmtData('Frozen yoghurt', 159, 6.0, 24, 4.0),
      this.fmtData('Ice cream sandwich', 237, 9.0, 37, 4.3),
      this.fmtData('Eclair', 262, 16.0, 24, 6.0),
      this.fmtData('Cupcake', 305, 3.7, 67, 4.3),
      this.fmtData('Gingerbread', 356, 16.0, 49, 3.9),
    ];

    return (
      <TableContainer component={Paper}>
        <Table aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Dessert (100g serving)</TableCell>
              <TableCell align="right">Calories</TableCell>
              <TableCell align="right">Fat&nbsp;(g)</TableCell>
              <TableCell align="right">Carbs&nbsp;(g)</TableCell>
              <TableCell align="right">Protein&nbsp;(g)</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {data.map((row) => (
              <TableRow key={row.name}>
                <TableCell component="th" scope="row">
                  {row.name}
                </TableCell>
                <TableCell align="right">{row.calories}</TableCell>
                <TableCell align="right">{row.fat}</TableCell>
                <TableCell align="right">{row.carbs}</TableCell>
                <TableCell align="right">{row.protein}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    )
  }

  fmtData = (name, calories, fat, carbs, protein) => {
    return { name, calories, fat, carbs, protein }
  }
}

export default SourceList
