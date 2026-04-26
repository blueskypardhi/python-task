# Task 3 (Option 2): Move all .jpg Files Automatically

import os
import shutil

source_folder = "images"
destination_folder = "moved_images"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

if os.path.exists(source_folder):
    for file in os.listdir(source_folder):
        if file.endswith(".jpg"):
            shutil.move(source_folder + "/" + file,
                        destination_folder + "/" + file)

    print("All .jpg files moved successfully!")

else:
    print("images folder not found!")