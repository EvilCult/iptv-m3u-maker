import React, { useEffect } from 'react'
import Link from 'next/link'
import { useRouter } from 'next/router'

const Index = (props) => {
  const router = useRouter()

  useEffect(() => {
    router.prefetch("/about")
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
