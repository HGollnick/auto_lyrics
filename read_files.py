# Import Modules
import os
import pysrt
import constants

def get_files():
    file_contents = []
    files = os.listdir(constants.TMP_PATH)  # use the specified PATH
    for file in files:
        file_content = get_file_content(file)
        file_info = {
            "name": file,
            "content": file_content
        }
        file_contents.append(file_info)
    return file_contents

def get_file_content(file):
    subtitles = []  # create an empty list to store the subtitles
    # iterate through all files
    f = file if isinstance(file, str) else file["name"]
    if f.endswith(".srt"):  # check if the file is an SRT file
        subs = pysrt.open(os.path.join(constants.TMP_PATH, f))  # use the full file path]
        for sub in subs:
            subtitle_obj = {
                "start": sub.start,
                "end": sub.end,
                "text": sub.text
            }
            subtitles.append(subtitle_obj)  # append the subtitle object to the list
    return subtitles  # return the list of subtitle objects
