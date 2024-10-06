import shutil
from pathlib import Path
import time

downloads_folder = Path(r"C:/Users/Desktop/downloads") #replace the path of the directory here

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".flv"],
    "Presentations":[".pptx"],
    "CSV":[".csv",".xls"],  #make this list of dictionaries as per your requirement
    "JSON":[".json"],
    "Documents": [".pdf", ".docx", ".xlsx", ".txt"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Programs": [".exe", ".msi", ".apk", ".bat", ".sh"],
}

def organize_downloads():
    for file in downloads_folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            for category, extensions in file_categories.items():
                if ext in extensions:
                    category_dir = downloads_folder / category
                    category_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), category_dir / file.name)
                    break

if __name__ == "__main__":
    # time.sleep(5) #to observe the changes in directory
    organize_downloads()
