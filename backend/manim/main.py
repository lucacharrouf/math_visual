from dotenv import load_dotenv
import os
import argparse
from generate_video import VideoGenerator

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate Manim animations for math concepts")
    parser.add_argument("--topic", type=str, required=True, help="Mathematical topic to animate")
    args = parser.parse_args()
    
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.getenv('ANTHROPIC_API_KEY')
    
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables")
        print("Please create a .env file with your API key or set it as an environment variable")
        return
    
    # Initialize the video generator
    video_gen = VideoGenerator(api_key=api_key)
    
    # Generate the video
    success = video_gen.generate_video(args.topic)
    
    if success:
        print(f"\nProcess completed for topic: '{args.topic}'")
        print(f"Code saved to: {video_gen.code_dir}")
        print("Next steps: Run the generated Python file with Manim to create the animation")
    else:
        print(f"\nFailed to complete the process for topic: '{args.topic}'")

if __name__ == "__main__":
    main()