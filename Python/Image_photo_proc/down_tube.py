from pytube import YouTube

# enter the URL of the video you want to download
url = "https://www.youtube.com/watch?v=LMW0o15fXP0"

# create a YouTube object and get the highest resolution video stream
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()

# download the video
print("Downloading video...")
stream.download()
print("Video downloaded successfully!")
