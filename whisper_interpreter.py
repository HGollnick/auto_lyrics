import whisper
import constants
from whisper.utils import get_writer

def load_model_and_transcribe(model_name, audio_file, task):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_file, task=task, word_timestamps=False)
    return result

def write_transcription(result, output_file, word_options):
    writer = get_writer("srt", constants.TMP_PATH)
    writer(result, output_file, word_options)

def generate():
    audio_file = constants.FILE_PATH
    output_file = constants.FILE_PATH.split(".")[0]
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
    generate()