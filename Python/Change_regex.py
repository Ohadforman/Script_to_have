import os

directory = "/Users/ohadformanair/Documents/Git/AML/LAB_5p6/DATA56/mixer_folder/MIXER_LOOP_RF_FREQ"

for filename in os.listdir(directory):
    if "/" in filename or ":" in filename or " " in filename:
        new_filename = filename.replace("/", "_").replace(":", "_").replace(" ", "_")
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
