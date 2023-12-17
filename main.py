import write_video
import write_audio
import whisper_interpreter

def main():
    whisper_interpreter.generate()
    write_video.generate()
    write_audio.generate()

if __name__ == "__main__":
    main()