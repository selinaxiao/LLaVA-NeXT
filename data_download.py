import os
import requests
import tarfile

# Repository details
repo_url = "https://huggingface.co/datasets/lmms-lab/LLaVA-NeXT-Data/resolve/main/llava_next_raw_format"
output_dir = "./llava_next_data"
os.makedirs(output_dir, exist_ok=True)

# List of known files to process (manually constructed based on the repo structure)
file_list = [
    "llava_next_raw_format_images_1.tar.gz",
    "llava_next_raw_format_images_2.tar.gz",
    "llava_next_raw_format_images_3.tar.gz",
    "llava_next_raw_format_images_4.tar.gz",
    "llava_next_raw_format_images_5.tar.gz",
    "llava_next_raw_format_images_6.tar.gz",
    "llava_next_raw_format_images_7.tar.gz",
    "llava_next_raw_format_images_8.tar.gz",
    "llava_next_raw_format_images_9.tar.gz",
    "llava_next_raw_format_images_10.tar.gz",
    "llava_next_raw_format_images_11.tar.gz",
    "llava_next_raw_format_processed.json"
]

# Function to download a file
def download_file(url, output_path):
    print(f"Downloading {url}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Downloaded to {output_path}")
    else:
        print(f"Failed to download {url}. HTTP Status Code: {response.status_code}")

# Function to extract tar.gz files
def extract_tar_file(file_path, output_path):
    print(f"Extracting {file_path}...")
    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(path=output_path)
    print(f"Extracted to {output_path}")

# Loop through files and process them
for file_name in file_list:
    file_url = f"{repo_url}/{file_name}"
    output_path = os.path.join(output_dir, file_name)

    # Download the file
    download_file(file_url, output_path)

    # Extract if it's a tar.gz file
    if file_name.endswith(".tar.gz"):
        extract_tar_file(output_path, output_dir)

print("All files have been downloaded and processed successfully!")
