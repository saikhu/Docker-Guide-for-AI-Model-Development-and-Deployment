import subprocess

def convert_video_to_gif(input_video_path, output_gif_path):
    try:
        # FFmpeg command to convert webm to gif
        command = [
            'ffmpeg',
            '-i', input_video_path,  # Input file
            '-filter_complex', '[0:v] fps=10,scale=720:-1 [a]',  # Setting fps and scale
            '-map', '[a]',  # Mapping the video stream
            '-y', output_gif_path  # Output file
        ]

        # Execute the command
        subprocess.run(command, check=True)
        print(f"Conversion successful. GIF saved at {output_gif_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
convert_video_to_gif('input.webm', 'output.gif')


video_path = ""  # Replace with the path to your input video
output_gif_path = "output.gif"  # Replace with the desired output GIF path
# Example usage
convert_video_to_gif(video_path, output_gif_path)
