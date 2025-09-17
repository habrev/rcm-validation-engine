import React from 'react'
import { useEffect, useState } from 'react'
import api from '../api'

export default function ResultsTable() {
  const [claims, setClaims] = useState([])

  useEffect(() => {
    api.get('/claims').then(res => setClaims(res.data))
  }, [])

  return (
    <div className="border p-4 rounded overflow-auto">
      <h2 className="font-semibold mb-2">Validation Results</h2>
      <table className="w-full border">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2 border">Claim ID</th>
            <th className="p-2 border">Status</th>
            <th className="p-2 border">Error Type</th>
            <th className="p-2 border">Explanation</th>
            <th className="p-2 border">Action</th>
          </tr>
        </thead>
        <tbody>
          {claims.map(c => (
            <tr key={c.id} className="text-sm">
              <td className="p-2 border">{c.claim_id}</td>
              <td className="p-2 border">{c.status}</td>
              <td className="p-2 border">{c.error_type}</td>
              <td className="p-2 border">{c.error_explanation}</td>
              <td className="p-2 border">{c.recommended_action}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
