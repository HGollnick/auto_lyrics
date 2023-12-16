import whisper
from whisper.utils import get_writer

PATH = ""

def load_model_and_transcribe(model_name, audio_file, task):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_file, task=task, word_timestamps=True)
    return result

def write_transcription(result, output_file, word_options):
    writer = get_writer("srt", "D:\\TMP")
    writer(result, output_file, word_options)

def main():
    audio_file = PATH
    output_file = PATH
    model_name = "large-v3"
    task = "transcribe"
    word_options = {
        "highlight_words": False,
        "max_line_count": 50,
        "max_line_width": 3
    }

    result = load_model_and_transcribe(model_name, audio_file, task)
    print(result["text"])
    write_transcription(result, output_file, word_options)

if __name__ == "__main__":
    main()