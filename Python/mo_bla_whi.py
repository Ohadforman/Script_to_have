
from moviepy.editor import VideoFileClip, vfx

# Load the original video file
video_file = "/Users/ohadformanair/Documents/Python/AMAN.mp4"
clip = VideoFileClip(video_file)

# Convert the video to black and white
bw_clip = clip.fx(vfx.blackwhite)

# Adjust the contrast of the black and white video
contrast_clip = bw_clip.fx(vfx.colorx, 2)

# Save the modified video to a new file
contrast_clip.write_videofile("/Users/ohadformanair/Documents/Python/AMANblack_and_white_video.mp4")
