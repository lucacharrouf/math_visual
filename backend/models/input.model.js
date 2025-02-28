import mongoose from "mongoose";

const inputSchema = new mongoose.Schema({
    input: {
        type: String,
        required: true,
    },
    pythonScript: {
        type: String,
        required: true,
    },
    rating: {
        type: Number,
        min: 1,
        max: 5,
        default: null,
    },
    feedback: {
        type: String,
        default: "",
    }
}, {
    timestamps: true,
});

const Input = mongoose.model('Input', inputSchema);

export default Input;