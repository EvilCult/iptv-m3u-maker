import Typography from '@mui/material/Typography'
import MuiLink from '@mui/material/Link'
import NextLink from 'next/link'

const Copyright = (props: any) => {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
        {'Code with ❤️ by '}
        <NextLink href="https://github.com/EvilCult/iptv-m3u-maker" legacyBehavior passHref>
        <MuiLink color="inherit">
          {props.author}
        </MuiLink>
        </NextLink>
      <br />
      {'© '}
        {new Date().getFullYear()}
      {'.'}
    </Typography>
  )
}

export default Copyright
