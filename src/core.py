import os
import shutil
from pathlib import Path

# Define file categories and their corresponding extensions
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Video": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".cpp", ".c", ".sh", ".bat"],
}

def organize_folder(target_dir):
    """
    Scans the target directory and moves files into organized subfolders.
    Returns a dictionary summarizing how many files were moved.
    """
    target_path = Path(target_dir)
    if not target_path.exists() or not target_path.is_dir():
        raise ValueError("Invalid directory path provided.")

    summary = {category: 0 for category in EXTENSION_MAP}
    summary["Others"] = 0

    # Iterate through all items in the directory
    for item in target_path.iterdir():
        # Skip directories to avoid organizing organized folders
        if item.is_dir():
            continue

        file_ext = item.suffix.lower()
        moved = False

        # Check which category the file belongs to
        for category, extensions in EXTENSION_MAP.items():
            if file_ext in extensions:
                dest_dir = target_path / category
                dest_dir.mkdir(exist_ok=True) # Create folder if it doesn't exist
                
                shutil.move(str(item), str(dest_dir / item.name))
                summary[category] += 1
                moved = True
                break

        # If extension doesn't match any category, move to 'Others'
        if not moved:
            dest_dir = target_path / "Others"
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(dest_dir / item.name))
            summary["Others"] += 1

    return summary
