from moviepy.editor import VideoFileClip, AudioFileClip
import constants

def generate():    
    # Add audio to the video
    video_clip = VideoFileClip(constants.OUTPUT_PATH)
    audio_clip = AudioFileClip(constants.FILE_PATH)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile('output.mp4')

if __name__ == "__main__":
    generate()