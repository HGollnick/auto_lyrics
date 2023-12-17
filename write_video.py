import cv2
import numpy as np
import read_files
from datetime import timedelta

def create_image_with_text(text, image_size=(1080, 1920, 3), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(255, 255, 255), thickness=1):
    # Create a black image
    image = np.zeros(image_size, dtype="uint8")

    # Calculate the size of the text box
    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)

    # Calculate the center of the image
    image_center_x = image.shape[1] // 2
    image_center_y = image.shape[0] // 2

    # Adjust the starting point of the text so that the center of the text box aligns with the center of the image
    location = (image_center_x - text_width // 2, image_center_y + text_height // 2)

    # Put the text on the image
    image = cv2.putText(image, text, location, font, font_scale, color, thickness, cv2.LINE_AA)
    
    return image

def create_video_from_image(video, image, duration, output_file, fileFormat=".mp4", codec='mp4v', fps=30.0):
    if video is None:
        # Create a VideoWriter objects
        fourcc = cv2.VideoWriter_fourcc(*codec)
        video = cv2.VideoWriter(output_file + fileFormat, fourcc, fps, (image.shape[1], image.shape[0]))

    # Write the image into the video file for a certain duration
    for _ in range(int(fps * duration)):
        video.write(image)
    return video

# TODO Test miliseconds implementation
# def create_video_from_image(video, image, duration_in_ms, output_file='output.mp4', codec='mp4v', fps=30.0):
#     if video is None:
#         # Create a VideoWriter objects
#         fourcc = cv2.VideoWriter_fourcc(*codec)
#         video = cv2.VideoWriter(output_file, fourcc, fps, (image.shape[1], image.shape[0]))

#     # Calculate the number of frames to write based on the duration in milliseconds
#     duration_in_sec = duration_in_ms / 1000.0
#     num_frames = int(fps * duration_in_sec)

#     # Write the image into the video file for the calculated number of frames
#     for _ in range(num_frames):
#         video.write(image)
#     return video
        
def release_video(video):        
    # Release the VideoWriter
    video.release()

def calculate_duration(start, end):
    # Assume start and end are SubRipTime instances
    start = start.to_time()
    end = end.to_time()

    # Convert SubRipTime to timedelta
    start_time = timedelta(hours=start.hour, minutes=start.minute, seconds=start.second, milliseconds=start.microsecond//1000)
    end_time = timedelta(hours=end.hour, minutes=end.minute, seconds=end.second, milliseconds=end.microsecond//1000)

    # Calculate the difference
    return end_time - start_time

def generate():
    video = None
    files = read_files.get_files()
    for file in files:
        results = read_files.get_file_content(file)
        if len(results) > 0:  # Check if results is empty
            for i, result in enumerate(results):
                file_name = file.get("name").split(".")[0]
                text = result.get("text")
                start = result.get("start")
                end = result.get("end")
                
                # Wait for instrumental part to end
                if i == 0:
                    video = create_video_from_image(video, create_image_with_text(result.get("")), start.seconds, file_name)
                elif results[i - 1].get("end") < start:
                    video = create_video_from_image(video, create_image_with_text(result.get("")), calculate_duration(results[i - 1].get("end"), start).seconds, file_name)

                image = create_image_with_text(text) 
                video = create_video_from_image(video, image, calculate_duration(start, end).seconds, file_name)
            release_video(video)

if __name__ == "__main__":
    main()