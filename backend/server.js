import express from 'express'
import dotenv from 'dotenv'
import cors from 'cors' // Add CORS support
import { connectDB } from './config/db.js'
import videoRoutes from './routes/video.route.js'
import inputRoutes from './routes/input.route.js'
import feedbackRoutes from './routes/feedback.route.js'

// Load environment variables from .env file
dotenv.config({ path: '../.env' })

// At the top of your server.js file, add more debugging
const app = express()

// Debugging middleware
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} - ${req.method} ${req.path}`)
  console.log('Request body:', req.body) 
  next()
})

// Make sure this is before the routes
app.use(express.json({ limit: '10mb' }))
app.use(cors())

// Root route - ensure this is BEFORE your other routes
app.get('/', (req, res) => {
  console.log('Root route hit')
  res.status(200).send('Server is ready')
})

// Then your other routes
app.use("/videos", videoRoutes)
app.use("/input", inputRoutes)
app.use("/feedback", feedbackRoutes)

// Basic root route
app.get('/', (req, res) => {
  res.send('Server is ready')
})

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(`Server error: ${err.stack}`)
  res.status(500).json({ 
    success: false, 
    message: 'Something broke!', 
    error: err.message 
  })
})

// Start server
const PORT = process.env.PORT || 4000
app.listen(PORT, () => {
    connectDB()
    console.log(`Server is ready at http://localhost:${PORT}`)
})