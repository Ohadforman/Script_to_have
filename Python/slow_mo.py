from moviepy.editor import VideoFileClip

# Load the original video file
video_file = "/Users/ohadformanair/Documents/Python/AMAN.mp4"
clip = VideoFileClip(video_file)

# Slow down the video by a factor of 2
slow_clip = clip.speedx(0.2)

# Save the slowed-down video to a new file
slow_clip.write_videofile("/Users/ohadformanair/Documents/Python/AMANslowed_down_video.mp4")
