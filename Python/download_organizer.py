import os
import shutil
from datetime import datetime, timedelta

# Get the path of the Downloads folder
downloads_dir = os.path.expanduser("/Users/ohadformanair/Downloads")
# Get the modification time of the oldest file in the Downloads folder
oldest_file = min((os.path.join(downloads_dir, f), os.path.getmtime(os.path.join(downloads_dir, f))) for f in os.listdir(downloads_dir) if os.path.isfile(os.path.join(downloads_dir, f)))
start_week = datetime.fromtimestamp(oldest_file[1])

# Loop through each file in the Downloads folder
for filename in os.listdir(downloads_dir):
    # Skip the script file itself
    if filename == "downloads_organizer.py":
        continue
    # Get the full path of the file
    file_path = os.path.join(downloads_dir, filename)
    # Check if the file is a regular file (not a folder or a symlink)
    if os.path.isfile(file_path):
        # Get the modification time of the file as a datetime object
        mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
        # Calculate the difference between the file's modification time and the start of the week
        days_since_start_week = (mtime - start_week).days
        # Calculate the week number based on the number of days since the start of the week
        week_number = days_since_start_week // 7
        # Calculate the start and end dates of the week
        week_start = start_week + timedelta(weeks=week_number)
        week_end = week_start + timedelta(days=6)
        # Format the week start and end dates to the desired folder name format
        week_folder_name = f"{week_start.strftime('%Y-%m-%d')} - {week_end.strftime('%Y-%m-%d')}"
        # Create a folder for the current week if it doesn't already exist
        week_folder_path = os.path.join(downloads_dir, week_folder_name)
        if not os.path.exists(week_folder_path):
            os.mkdir(week_folder_path)
            print(f"Created new folder: {week_folder_path}")
        # Move the file to the week folder
        new_file_path = os.path.join(week_folder_path, filename)
        shutil.move(file_path, new_file_path)
        print(f"Moved file {filename} to folder {week_folder_name}")