import Typography from '@mui/material/Typography'
import MuiLink from '@mui/material/Link'
import NextLink from 'next/link'
import FavoriteIcon from '@mui/icons-material/Favorite'

const Copyright = (props) => {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
        {'Code with ❤️ by '}
        <NextLink href="https://mui.com/" legacyBehavior passHref>
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
