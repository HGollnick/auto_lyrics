# Import Modules
import os
import pysrt

# Folder Path
PATH = "D:\\TMP"

def get_files():
    subtitles = []  # create an empty list to store the subtitles
    # iterate through all files
    for file in os.listdir(PATH):  # use the specified PATH
        if file.endswith(".srt"):  # check if the file is an SRT file
            subs = pysrt.open(os.path.join(PATH, file))  # use the full file path
            for sub in subs:
                subtitle_obj = {
                    "start": sub.start,
                    "end": sub.end,
                    "text": sub.text
                }
                subtitles.append(subtitle_obj)  # append the subtitle object to the list
    return subtitles  # return the list of subtitle objects
