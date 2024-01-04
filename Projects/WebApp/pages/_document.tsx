import { Html, Head, Main, NextScript } from 'next/document'

import { ThemeProvider, createTheme } from '@mui/material/styles'
import CssBaseline from '@mui/material/CssBaseline'

export default function Document() {
  const darkTheme = createTheme({
    palette: {
      mode: 'dark',
    },
  })

  return (
    <Html>
      <Head />
      <body>
        <ThemeProvider theme={darkTheme}>
        <Main />
        <NextScript />
        </ThemeProvider>
      </body>
    </Html>
  )
}
