import React from 'react'
import { useEffect, useState } from 'react'
import { Bar } from 'react-chartjs-2'
import api from '../api'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement } from 'chart.js'
ChartJS.register(CategoryScale, LinearScale, BarElement)

export default function Charts() {
  const [data, setData] = useState({labels:[], counts:[], amounts:[]})

  useEffect(() => {
    api.get('/metrics').then(res => setData(res.data))
  }, [])

  return (
    <div className="space-y-6">
      <div>
        <h2 className="font-semibold mb-2">Claim Counts by Error Category</h2>
        <Bar data={{
          labels: data.labels,
          datasets: [{ label: 'Count', data: data.counts }]
        }} />
      </div>
      <div>
        <h2 className="font-semibold mb-2">Paid Amount by Error Category</h2>
        <Bar data={{
          labels: data.labels,
          datasets: [{ label: 'Amount', data: data.amounts }]
        }} />
      </div>
    </div>
  )
}
