import shutil
import os

# Define the source directories
source_dirs = ['/Users/ohadformanair/Downloads', '/Users/ohadformanair/Desktop']

# Define the destination directories
university_dir = '/Users/ohadformanair/Documents/University'
personal_dir = '/Users/ohadformanair/Documents/Personal'

# Define the subdirectories within the lecture type directory
lecture_subdirectories = {
    'Lec': 'Lectures',
    'Exe': 'Exercises',
    'Ext': 'Extras',
    'Hw': 'HomeWork',
}

# Define the course names and their corresponding directories
course_directories = {
    'ITP': 'Intro_to_particles',
    'RSN': 'Random_Signals_and_Noises',
    'ACL': 'Advanced_C_Lab',
    'AML': 'Advanced_Microwave_Lab',
    'NA': 'Numerical_Analysis',
    'PCS': 'Practical_Control_Systems',
    'SM': 'Spectral_Methods',
    'IOD': 'Intro_to_optoelectric_devices',
    # Add more courses as necessary
}

# Define the personal directories and their corresponding names
personal_directories = {
    'BNK': 'Bank',
    'PHO': 'Photos',
    # Add more personal directories as necessary
}

# Iterate over the source directories
for source_dir in source_dirs:

    # Iterate over the files in the source directory
    for file_name in os.listdir(source_dir):

        # Ignore .DS_Store files
        if file_name == '.DS_Store':
            continue

        # Check if the file has an extension
        if not os.path.isfile(os.path.join(source_dir, file_name)):
            continue

        # Check if the file name follows the expected naming convention
        if not any(file_name.startswith(prefix) for prefix in lecture_subdirectories.keys()) \
                and not file_name.startswith('UNI_') and not file_name.startswith('PER_'):
            print(f"Error: invalid file name format: {file_name}")
            continue

        # Extract the basename of the file
        file_basename = os.path.basename(file_name)
        # Split the file name into the prefix, course/personal name, and possibly a lecture/file name
        file_parts = file_basename.rsplit('_', maxsplit=3)
        if len(file_parts) == 4:
            prefix, course_name, lecture_type, file_basename = file_parts
        elif len(file_parts) == 3:
            prefix, name_1, name_2 = file_parts
            if prefix == 'UNI':
                course_name = name_1
                lecture_type = ''
                file_basename = name_2
            elif prefix == 'PER':
                course_name = name_1
                lecture_type = ''
                file_basename =  name_2
            else:
                print(f"Error: invalid file prefix: {prefix}")
                continue
        else:
            print(f"Error: invalid file name format: {file_name}")
            continue

        # Handle university files
        if prefix == 'UNI':
            if course_name not in course_directories:
                print(f"Error: invalid course name: {course_name}")
                continue
            course_directory = course_directories[course_name]

            # Extract the lecture type from the filename, if it exists
            if '_' in file_basename:
                lecture_type, linux_tutorial = file_basename.split('_', maxsplit=1)
            else:
                linux_tutorial = file_basename

           
            # Construct the destination directory path
            if lecture_type in lecture_subdirectories:
                destination_dir = os.path.join(university_dir, course_directory, lecture_subdirectories[lecture_type])
            else:
                destination_dir = os.path.join(university_dir, course_directory)

            # Create the destination directory if it doesn't exist
            os.makedirs(destination_dir, exist_ok=True)

            # Construct the destination file path
            destination_file = os.path.join(destination_dir, file_basename)

            # Move the file to the destination
            shutil.move(os.path.join(source_dir, file_name), destination_file)

        # Handle personal files
        elif prefix == 'PER':
            if course_name not in personal_directories:
                print (course_name)
                print(f"Error: invalid personal directory name: {course_name}")
                continue
            personal_directory = personal_directories[course_name]

            # Construct the destination directory path
            destination_dir = os.path.join(personal_dir, personal_directory)

            # Create the destination directory if it doesn't exist
            os.makedirs(destination_dir, exist_ok=True)

            # Construct the destination file path
            destination_file = os.path.join(destination_dir, file_basename)

            # Move the file to the destination
            shutil.move(os.path.join(source_dir, file_name), destination_file)
           

# Create the README.txt file
with open('/Users/ohadformanair/Documents/Scripts/My_Apps/README.txt', 'w') as f:

    # Print the format for university files
    f.write('Format for university files:\n')
    f.write('Prefix_Course_LectureType_FileName\n\n')
    f.write('Prefix: UNI\n')
    f.write('Course: ' + ', '.join(course_directories.keys()) + '\n')
    f.write('Lecture Type: ' + ', '.join(lecture_subdirectories.keys()) + '\n')
    f.write('Example: UNI_ITP_Lec_Lecture1.pdf\n\n')

    # Print the list of university directories
    f.write('University Directories:\n')
    for course_directory in course_directories.values():
        f.write(f'{course_directory}: {os.path.join(university_dir, course_directory)}\n')

    # Print the format for personal files
    f.write('\nFormat for personal files:\n')
    f.write('Prefix_FileType_FileName\n\n')
    f.write('Prefix: PER\n')
    f.write('File Type: ' + ', '.join(personal_directories.keys()) + '\n')
    f.write('Example: PER_Photo_ProfilePic.jpg\n\n')

    # Print the list of personal directories
    f.write('Personal Directories:\n')
    for personal_directory in personal_directories.values():
        f.write(f'{personal_directory}: {os.path.join(personal_dir, personal_directory)}\n')

    # Print the source directories
    f.write('\nSources:\n')
    for source_dir in source_dirs:
        f.write(f'{source_dir}\n')

    # Print the destination directories
    f.write('\nDestinations:\n')
    f.write(f'University: {university_dir}\n')
    f.write(f'Personal: {personal_dir}\n')




# Define the source directories
source_dirs_git = ['/Users/ohadformanair/Downloads', 
                   '/Users/ohadformanair/Desktop',
                   '/Users/ohadformanair/Documents/University']

# Define the destination directory for Git files
git_dir = '/Users/ohadformanair/Documents/Git'

# Define a recursive function to iterate over files in a directory and its subdirectories
def iterate_files(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:

            # Ignore .DS_Store files
            if file_name == '.DS_Store':
                continue

            # Check if the file has an extension
            if not os.path.isfile(os.path.join(root, file_name)):
                continue

            # Check if the file name starts with GIT
            if not file_name.startswith('GIT_'):
                continue

            # Construct the destination file path without the 'GIT_' prefix
            destination_file = os.path.join(git_dir, file_name[4:])

            # Move the file to the destination with its original name
            shutil.move(os.path.join(root, file_name), destination_file)

# Iterate over the source directories and their subdirectories
for source_dir in source_dirs_git:
    iterate_files(source_dir)
