import os
import random
import shutil
import re

tsinghua = '/mnt/c/Users/hpulc/Downloads/tsinghua/low-resolution'  # Replace with your directory path
stanford = 'raw_data/images'

tsinghua_entries = os.listdir(tsinghua)
cleaned_tsinghua = [entry.split("-")[2].lower() for entry in tsinghua_entries if len(entry.split("-")) > 2]

stanford_entries = os.listdir(stanford)
cleaned_stanford = ["_".join(entry.split("-")[1:]).lower() for entry in stanford_entries]

common = [entry for entry in cleaned_tsinghua if entry in cleaned_stanford]

common_with_tsinghua_format = [entry for entry in tsinghua_entries if len(entry.split("-")) > 2 and entry.split("-")[2].lower() in common]
common_with_stanford_format = [entry for entry in stanford_entries if entry.split("-")[1].lower() in common]

print(len(common))

for folder in common_with_tsinghua_format:
    print(folder)
    #sample from this folder
    folder_path = f"{tsinghua}/{folder}"
    files_in_subfolder = [f for f in os.listdir(folder_path)]
    sampled_files = random.sample(files_in_subfolder, 50)

    #create a directory for this folder but with stanford format
    stanford_format = [entry for entry in stanford_entries if folder.split("-")[2].lower() in "_".join(entry.split("-")[1:]).lower()][0]
    destination_subfolder = f"raw_data/test_samples/{stanford_format}"
    os.makedirs(destination_subfolder, exist_ok=True)

    for file_name in sampled_files:
        source_file_path = os.path.join(folder_path, file_name)
        destination_file_path = os.path.join(destination_subfolder, file_name)
        shutil.copy2(source_file_path, destination_file_path)
