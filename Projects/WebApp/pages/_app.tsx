import type { AppProps } from 'next/app'
import { ThemeProvider, createTheme } from '@mui/material/styles'

export default function App({ Component, pageProps }: AppProps) {
  const darkTheme = createTheme({
    palette: {
      // mode: 'dark',
    },
  })

  return (
    <ThemeProvider theme={darkTheme}>
      <Component {...pageProps} />
    </ThemeProvider>
  )
}
