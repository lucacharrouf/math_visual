import express from 'express'
import dotenv from 'dotenv'
import cors from 'cors' // Add CORS support
import path from 'path' // For file paths
import { fileURLToPath } from 'url' // For ES modules __dirname
import { connectDB } from './config/db.js'
import videoRoutes from './routes/video.route.js'
import inputRoutes from './routes/input.route.js'
import feedbackRoutes from './routes/feedback.route.js'
import fs from 'fs' // For file system operations

// Set up __dirname equivalent for ES modules
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

// Load environment variables from .env file
dotenv.config({ path: '../.env' })

// Initialize Express app
const app = express()

// Debugging middleware
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} - ${req.method} ${req.path}`)
  if (req.method !== 'GET') { // Only log bodies for non-GET requests to avoid huge logs
    console.log('Request body type:', typeof req.body)
    // For security, only log a sample or summary of the body if it's large
    const bodySummary = typeof req.body === 'object' 
      ? `Keys: ${Object.keys(req.body).join(', ')}` 
      : 'Body not an object'
    console.log('Request body summary:', bodySummary)
  }
  next()
})

// Middleware
app.use(express.json({ limit: '50mb' })) // Increased limit for video data
app.use(express.urlencoded({ extended: true, limit: '50mb' }))
app.use(cors())

// Define video directories - use both singular and plural directories
const videoDir = path.join(process.cwd(), 'backend', 'manim', 'content', 'video_dir');
const videosDir = path.join(process.cwd(), 'backend', 'manim', 'content', 'videos_dir');

console.log('Video directories to check:');
console.log('- Singular path:', videoDir);
console.log('- Plural path:', videosDir);

// Check if video directories exist and log their contents
try {
  if (fs.existsSync(videoDir)) {
    console.log('Singular video_dir exists');
    const files = fs.readdirSync(videoDir);
    console.log('Files in video_dir:', files);
  } else {
    console.log('Singular video_dir does not exist');
  }
  
  if (fs.existsSync(videosDir)) {
    console.log('Plural videos_dir exists');
    const files = fs.readdirSync(videosDir);
    console.log('Files in videos_dir:', files);
  } else {
    console.log('Plural videos_dir does not exist');
  }
} catch (err) {
  console.error('Error checking video directories:', err);
}

// Serve videos from BOTH directories to be safe
app.use('/videos-content', express.static(videoDir));
app.use('/videos-content', express.static(videosDir));

// Add a test endpoint to check file access
app.get('/check-videos', (req, res) => {
  try {
    // Check both possible directories
    const results = {
      singular: { exists: false, files: [] },
      plural: { exists: false, files: [] }
    };
    
    // Check singular directory (video_dir)
    if (fs.existsSync(videoDir)) {
      results.singular.exists = true;
      results.singular.path = videoDir;
      results.singular.files = fs.readdirSync(videoDir);
    }
    
    // Check plural directory (videos_dir)
    if (fs.existsSync(videosDir)) {
      results.plural.exists = true;
      results.plural.path = videosDir;
      results.plural.files = fs.readdirSync(videosDir);
    }
    
    res.json({ 
      success: true,
      results: results
    });
  } catch (err) {
    res.json({ 
      success: false, 
      error: err.message 
    });
  }
});

// Root route - ensure this is BEFORE your other routes
app.get('/', (req, res) => {
  console.log('Root route hit')
  res.status(200).send('Server is ready')
})

// API Routes
app.use("/videos", videoRoutes)
app.use("/input", inputRoutes)
app.use("/feedback", feedbackRoutes)

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
    console.log(`Video files will be served from both directories:`)
    console.log(`- ${videoDir}`)
    console.log(`- ${videosDir}`)
})