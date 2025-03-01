import os
import subprocess
import re
import shutil
from setup import ManimGenerator

class VideoGenerator:
    def __init__(self, api_key):
        # Create directories in the user's home directory
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.code_dir = os.path.join(curr_dir, "content", "code_dir")
        self.videos_dir = os.path.join(curr_dir, "content", "videos_dir")
        
        # Create necessary directories
        os.makedirs(self.code_dir, exist_ok=True)
        os.makedirs(self.videos_dir, exist_ok=True)
        
        # Initialize generator with API key
        self.generator = ManimGenerator(api_key=api_key)
    
    def _get_safe_filename(self, math_topic):
        """Convert math topic to a safe filename"""
        return math_topic.lower().replace(' ', '_').replace('/', '_').replace('\\', '_').replace(':', '_')
        
    def _extract_class_name(self, code):
        """Extract the class name from the generated code"""
        class_match = re.search(r'class\s+(\w+)\s*\(Scene\)', code)
        if class_match:
            return class_match.group(1)
        return "MathAnimation"  # Default class name
        
    def generate_video(self, math_topic, audience_level="high school"):
        """Generate a Manim animation video for the given math topic"""
        # Generate design
        print("Generating animation design...")
        design_result = self.generator.design_scene(math_topic, audience_level)
        
        if not design_result:
            print("Failed to generate design.")
            return False
            
        # Extract the animation design section
        design = design_result.get("animation_design", design_result.get("full_response", ""))
        print("\nDesign generated successfully!")
        
        # Generate code from design
        print("\nGenerating Manim code...")
        code_result = self.generator.generate_code(design)
        
        if not code_result:
            print("Failed to generate code.")
            return False
            
        # Extract just the code part from the result
        code = code_result.get("code", "")
        if not code:
            print("No code found in generator response.")
            return False
            
        print("\nCode generated successfully!")
        
        # Save code as a file
        safe_topic = self._get_safe_filename(math_topic)
        filename = f"generated_{safe_topic}.py"
        filepath = os.path.join(self.code_dir, filename)
        
        with open(filepath, 'w') as file:
            file.write(code)
        
        # Save code path as instance attribute for easy access later
        self.code_path = filepath
        print(f"Code saved to {filepath}")
        
        # Extract the class name for running Manim
        class_name = self._extract_class_name(code)
        print(f"Detected class name: {class_name}")
        
        # Run Manim on the generated file
        try:
            print(f"Running Manim animation...")
            
            # Create a temp directory for Manim output
            temp_media_dir = os.path.join(self.code_dir, "media")
            os.makedirs(temp_media_dir, exist_ok=True)
            
            # Change to the code directory to run manim
            original_dir = os.getcwd()
            os.chdir(self.code_dir)
            
            # Run Manim with low quality for speed (-ql) and preview (-p)
            result = subprocess.run(
                ['manim', '-ql', filepath, class_name],
                capture_output=True, 
                text=True
            )
            
            if result.returncode != 0:
                print(f"Manim error: {result.stderr}")
                os.chdir(original_dir)
                return False
                
            # Find the generated video file
            video_pattern = r"File ready at '(.*?)'"
            match = re.search(video_pattern, result.stdout)
            
            if not match:
                # Look in the media directory for the most recent mp4 file
                media_videos_dir = os.path.join(temp_media_dir, "videos", os.path.basename(filepath).replace('.py', ''), "480p15")
                if os.path.exists(media_videos_dir):
                    mp4_files = [f for f in os.listdir(media_videos_dir) if f.endswith('.mp4')]
                    if mp4_files:
                        # Sort by creation time, newest first
                        mp4_files.sort(key=lambda x: os.path.getctime(os.path.join(media_videos_dir, x)), reverse=True)
                        source_path = os.path.join(media_videos_dir, mp4_files[0])
                    else:
                        print("No MP4 files found in the media directory.")
                        os.chdir(original_dir)
                        return False
                else:
                    print(f"Media videos directory not found: {media_videos_dir}")
                    os.chdir(original_dir)
                    return False
            else:
                source_path = match.group(1)
            
            # Copy the video to the videos directory with a descriptive name
            target_filename = f"{safe_topic}_animation.mp4"
            target_path = os.path.join(self.videos_dir, target_filename)
            
            shutil.copy2(source_path, target_path)
            print(f"Animation saved to {target_path}")
            
            # Save video path as instance attribute
            self.video_path = target_path
            
            # Change back to original directory
            os.chdir(original_dir)
            
            return target_path
            
        except Exception as e:
            print(f"Error running Manim: {e}")
            # Make sure we return to the original directory
            if 'original_dir' in locals():
                os.chdir(original_dir)
            return False