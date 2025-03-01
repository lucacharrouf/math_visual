// routes/input.route.js
import express from 'express'
import Input from '../models/input.model.js' // You'll need to create this model

const router = express.Router()

// Add this route to handle the data from Python
router.post('/save-from-python', async (req, res) => {
  try {
    console.log('Received data from Python:', req.body)
    
    // Create a new document using your model
    const newInput = new Input({
      topic: req.body.topic,
      code: req.body.code,
      status: req.body.status
    })
    
    // Save to MongoDB
    const savedInput = await newInput.save()
    
    res.status(201).json({
      success: true,
      message: 'Data saved successfully',
      data: savedInput
    })
  } catch (error) {
    console.error('Error saving input data:', error)
    res.status(400).json({
      success: false,
      message: 'Failed to save data',
      error: error.message
    })
  }
})

// Handle the feedback
router.get()

export default router