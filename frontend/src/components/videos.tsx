import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface Video {
  _id: string;
  name: string;
  videoPath: string;
  status: string;
}

const VideoGallery: React.FC = () => {
  const [videos, setVideos] = useState<Video[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [detailedError, setDetailedError] = useState<any>(null);

  useEffect(() => {
    const fetchVideos = async () => {
      console.clear(); // Clear previous console logs
      console.log('Starting to fetch videos...');
      
      try {
        console.log('Making request to /videos endpoint');
        const response = await axios.get('/videos');
        
        console.log('Response received:', {
          status: response.status,
          statusText: response.statusText,
          data: response.data
        });
        
        if (response.data && response.data.success) {
          console.log('Videos loaded successfully:', response.data.data);
          setVideos(response.data.data);
        } else {
          console.error('API returned unsuccessful response:', response.data);
          setError('API returned unsuccessful response');
          setDetailedError(response.data);
        }
      } catch (err: any) {
        console.error('Error caught while fetching videos:', err);
        
        // Save detailed error information
        setDetailedError({
          message: err.message,
          response: err.response ? {
            status: err.response.status,
            statusText: err.response.statusText,
            data: err.response.data
          } : 'No response data',
          request: err.request ? 'Request was made but no response received' : 'Request setup error'
        });
        
        // Set user-friendly error message
        if (err.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          setError(`Server error: ${err.response.status} ${err.response.statusText}`);
        } else if (err.request) {
          // The request was made but no response was received
          setError('No response received from server. Is your server running?');
        } else {
          // Something happened in setting up the request that triggered an Error
          setError(`Error: ${err.message}`);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchVideos();
  }, []);

  // Manual test function
  const testEndpoint = async () => {
    try {
      const response = await fetch('/videos');
      const data = await response.json();
      console.log('Test response:', data);
      alert('Test successful! Check console for details.');
    } catch (err: any) {
      console.error('Test failed:', err);
      alert(`Test failed: ${err.message}`);
    }
  };

  // Function to fix video path based on the actual directory structure
  const getFixedVideoPath = (originalPath: string) => {
    // The issue is that the database has 'videos_dir' but the actual filesystem has 'video_dir'
    // Also, we need to map this to the correct frontend URL path
    
    // First, correct the 'videos_dir' to 'video_dir' discrepancy
    let correctedPath = originalPath.replace('videos_dir', 'video_dir');
    
    // Now map the backend path to the frontend URL path
    // We want to go from something like:
    // 'backend/backend/manim/content/video_dir/vector_addition_animation.mp4'
    // to:
    // '/videos-content/vector_addition_animation.mp4'
    
    // Extract just the filename from the path
    const parts = correctedPath.split('/');
    const filename = parts[parts.length - 1];
    
    // Construct the new URL with just the filename
    return `/videos-content/${filename}`;
  };

  if (loading) {
    return <div className="p-4 text-center">Loading videos...</div>;
  }

  if (error) {
    return (
      <div className="container mx-auto p-4">
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          <p className="font-bold">Error: {error}</p>
        </div>
        
        <div className="bg-gray-100 p-4 rounded-lg mb-4">
          <h2 className="text-lg font-bold mb-2">Troubleshooting Steps:</h2>
          <ol className="list-decimal pl-5 space-y-2">
            <li>Make sure your server is running on port 4000</li>
            <li>Check that MongoDB is connected properly</li>
            <li>Verify that the '/videos' route is correctly defined in your server</li>
            <li>Check your server console for any error messages</li>
            <li>Ensure your video paths match the actual directory structure</li>
          </ol>
        </div>
        
        <button 
          onClick={testEndpoint}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Test /videos Endpoint
        </button>
        
        {detailedError && (
          <div className="mt-4">
            <h3 className="font-bold mb-2">Detailed Error Information:</h3>
            <pre className="bg-gray-800 text-white p-4 rounded overflow-auto max-h-96">
              {JSON.stringify(detailedError, null, 2)}
            </pre>
          </div>
        )}
      </div>
    );
  }

  if (videos.length === 0) {
    return <div className="p-4 text-center">No videos found in the database.</div>;
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">Visual Math ({videos.length} videos)</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {videos.map((video) => (
          <div key={video._id} className="border rounded-lg overflow-hidden shadow-lg">
            <div className="aspect-w-16 aspect-h-9">
            <div className="p-4 bg-gray-50">
              <h2 className="text-lg font-semibold truncate">{video.name}</h2>
              <p className="text-sm text-gray-600 mt-1 truncate">
                Original: {video.videoPath}
              </p>
            </div>
              <video 
                src={getFixedVideoPath(video.videoPath)} 
                controls
                className="w-full h-full object-cover"
                preload="metadata"
                onError={(e) => console.error(`Video error for ${video.name}:`, e)}
              >
                Your browser does not support the video tag.
              </video>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default VideoGallery;