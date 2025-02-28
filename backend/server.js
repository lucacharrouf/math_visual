import express from 'express'
import dotenv from 'dotenv'
import { connectDB } from './config/db.js'
import videoRoutes from './routes/video.route.js'
import inputRoutes from './routes/input.route.js'

// Load environment variables from .env.db file
dotenv.config({ path: './.env' })

const app = express()

// Middleware for parsing JSON bodies
app.use(express.json())

app.use("/videos", videoRoutes)
app.use("/input", inputRoutes)

// Basic route
app.get('/.', (req, res) => {
  res.send('Server is ready')
})

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack)
  res.status(500).send('Something broke!')
})

// Start server
app.listen(4000, () => {
    connectDB();
    console.log("Server is ready at http://localhost:4000")
})