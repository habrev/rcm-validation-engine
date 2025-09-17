import React from 'react'
import FileUpload from '../components/FileUpload'
import ResultsTable from '../components/ResultsTable'
import Charts from '../components/Charts'

export default function Dashboard() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">RCM Validation Dashboard</h1>
      <FileUpload />
      <div className="grid md:grid-cols-2 gap-6">
        <Charts />
        <ResultsTable />
      </div>
    </div>
  )
}
