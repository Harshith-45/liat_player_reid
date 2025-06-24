import gdown
import os

# Google Drive file URL and destination
file_id = '1mjs6gvIwRLU2cBR9C_35_CMjQ2WmiR-3'
url = f'https://drive.google.com/uc?id={file_id}'
output = 'models/player_detection.pt'

# Create 'models' directory if it doesn't exist
os.makedirs('models', exist_ok=True)

# Download
print("[INFO] Downloading model from Google Drive...")
gdown.download(url, output, quiet=False)
print("[INFO] Download complete.")
