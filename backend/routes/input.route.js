import express from "express";
import Input from '../models/input.model.js'
import { spawn } from 'child_process'
import mongoose from "mongoose";

const router = express.Router();

// Get the input from the user
router.post('/', async (req, res) => {
    const input = req.body;

    if(!input.name) {
        return res.status(400).json({ success:false, message:"Please fill the input"});
    }
    const newInput = new Input(input)

    try {
        await newInput.save();
        const pythonProcess = spawn('python', ['main.py', JSON.stringify(input)]);
        
        let pythonOutput = '';
        let pythonError = '';
        
        // Collect data from the Python script
        pythonProcess.stdout.on('data', (data) => {
            pythonOutput += data.toString();
        });
        
        pythonProcess.stderr.on('data', (data) => {
            pythonError += data.toString();
        });
        
        // When the Python process exits
        pythonProcess.on('close', (code) => {
            if (code !== 0) {
                console.error(`Python script exited with code ${code}`);
                console.error(`Python error: ${pythonError}`);
                return res.status(500).json({ 
                    success: false, 
                    message: "Error running Python script",
                    error: pythonError
                });
            }
            
            // Return the saved input along with Python script output
            res.status(201).json({ 
                success: true, 
                data: newInput,
                pythonOutput: pythonOutput
            });
        });

    } catch(error) {
        console.error("Error in getting the input: ", error.message);
        res.status(500).json({ success: false, message: "Server error"});
    }
})

export default router;