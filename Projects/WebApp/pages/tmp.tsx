import React, { useEffect } from 'react'
import { useRouter } from 'next/router'

interface Props {
  stars: string;
}

const Index = (props: Props) => {
  const router = useRouter()

  useEffect(() => {
    const jwt = localStorage.getItem('jwt')
    if (jwt === null) {
      router.push('/login')
    }
  })

  return (
    <div className="bg-blue-500 text-white p-4">
      <p>Hello Next.js</p>
      <p>Next stars: {props.stars}</p>
    </div>
  )
}

Index.getInitialProps = async () => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const json = await res.json()

  return { stars: json.stargazers_count }
}

export default Index
