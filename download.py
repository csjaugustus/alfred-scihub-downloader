import sys
import requests
import os
import re

timeout_seconds = int(os.environ["timeout"])

def sanitize_filename(filename):
    # Define a regular expression pattern to match illegal filename characters
    illegal_chars = r'[\\/:\*\?"<>\|]'  # Add more if needed
    # Replace illegal characters with underscores
    sanitized_filename = re.sub(illegal_chars, '_', filename)

    return sanitized_filename

download_url = os.environ["split1"]
save_dir = os.environ["save_dir"]
title = os.environ["split2"]
# print(f"Download link is: {download_url}")

response = requests.get(download_url, timeout=timeout_seconds)

fn = f"{sanitize_filename(title)}.pdf"
save_path = os.path.join(save_dir, fn)

with open(save_path, "wb") as f:
    f.write(response.content)

sys.stdout.write(save_path)
