# Player Re-Identification in Sports Broadcasts 🎥⚽

This project detects and tracks players in sports broadcast videos using YOLOv8 and Deep SORT for re-identification.

---

## 🧠 Features

- Player detection using YOLOv8
- Player tracking using Deep SORT
- Works on sports broadcast videos
- Clean, modular code using OpenCV

---

## 🗂️ Project Structure

liat_player_reid/
├── models/
│ └── player_detection.pt # Not pushed to GitHub (too large)
├── videos/
│ └── broadcast.mp4 # Input video
├── src/
│ ├── main.py # Main runner script
│ ├── detector.py # Detection logic
│ └── tracker.py # Tracking logic
├── requirements.txt # Dependencies
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Or:

bash
Copy
Edit
pip install ultralytics deep_sort_realtime opencv-python torch torchvision
📦 Place Required Files
Place your YOLO model in models/player_detection.pt

Place your video file in videos/broadcast.mp4

🚀 Run
bash
Copy
Edit
python src/main.py videos/broadcast.mp4
🛑 Do NOT Upload to GitHub
models/player_detection.pt (over 100MB)

venv/ folder (huge and unnecessary)

videos/ folder (media files)

🧾 Author
Developed by Harshith-45 for Liat.ai

yaml
Copy
Edit

---

### 💻 Git Commands to Upload Cleanly

```bash
# Go to your project
cd %USERPROFILE%\Desktop\liat_player_reid

# Create .gitignore to exclude large files
echo models/ > .gitignore
echo videos/ >> .gitignore
echo venv/ >> .gitignore
echo __pycache__/ >> .gitignore

# Initialize Git if not already done
git init

# Add and commit only necessary files
git add .
git commit -m "Upload player re-identification project without large files"

# Add your GitHub remote (update with your repo URL if needed)
git remote add origin https://github.com/Harshith-45/liat_player_reid.git

# Rename to main branch (if not already)
git branch -M main

# Push to GitHub
git push -u origin main
