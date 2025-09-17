import React from 'react'
import { useState } from 'react'

export default function Login({ onLogin }) {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    if (username && password) onLogin()
  }

  return (
    <div className="h-screen flex items-center justify-center bg-gray-100">
      <form onSubmit={handleSubmit} className="bg-white shadow p-6 rounded w-80 space-y-4">
        <h1 className="text-xl font-bold text-center">Login</h1>
        <input className="w-full border p-2" placeholder="Username"
               value={username} onChange={(e)=>setUsername(e.target.value)}/>
        <input className="w-full border p-2" type="password" placeholder="Password"
               value={password} onChange={(e)=>setPassword(e.target.value)}/>
        <button type="submit" className="w-full bg-blue-500 text-white py-2 rounded">
          Sign In
        </button>
      </form>
    </div>
  )
}
