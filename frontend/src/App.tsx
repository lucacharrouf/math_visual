import Videos from './components/videos'
import './App.css'

function App() {
  // Define the video path relative to the public directory
  const videoPath = '/videos/singular_value_decomposition.mp4'

  return (
    <>
      <Videos />
      <video 
        src={videoPath}
        controls
        className="w-full h-full object-cover"
        preload="metadata"
        onError={(e) => console.error('Video error:', e)}
      >
        Your browser does not support the video tag.
      </video>
    </>
  )
}

export default App