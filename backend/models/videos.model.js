import mongoose from "mongoose";

const videoSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    video: {
        type: String, 
        required: true
    },
    description: {
        type: String,
        default: ""
    },
    duration: {
        type: Number
    },
    
}, {
    timestamps: true
});

const Video = mongoose.model('Video', videoSchema);

export default Video;