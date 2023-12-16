from moviepy.editor import VideoFileClip, AudioFileClip

PATH = ""

def main():    
    # Add audio to the video
    video_clip = VideoFileClip('output.mp4')
    audio_clip = AudioFileClip(PATH)
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile('output_with_audio.mp4')

if __name__ == "__main__":
    main()