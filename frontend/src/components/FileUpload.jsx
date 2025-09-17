import React from 'react'
import api from '../api'

export default function FileUpload() {
  const upload = async (e) => {
    const formData = new FormData()
    formData.append('file', e.target.files[0])
    await api.post('/upload', formData)
    alert('File uploaded and processed')
  }
  return (
    <div className="border p-4 rounded">
      <h2 className="font-semibold mb-2">Upload Claims/Rules Files</h2>
      <input type="file" onChange={upload} />
    </div>
  )
}
