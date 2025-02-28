import express from "express";
import Video from '../models/videos.model.js'

const router = express.Router();

// Get and show all the videos
router.get('/', async (req, res) => {
    try {
        const videos = await Video.find({});
        res.status(200).json({ success: true, data: videos })
    } catch (error) {
        console.log("Error in fetching videos: ", error.message)
        res.status(400).json({ success: false, message: "Server error"})
    }
})

export default router;