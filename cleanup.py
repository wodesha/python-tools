import os
import shutil
from datetime import datetime

def cleanup_desktop(output_dir="Desktop_Cleanup"):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
        "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".md"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv", ".webm"],
        "Audio": [".mp3", ".wav", ".flac", ".ogg", ".aac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".json", ".yaml"],
        "Executables": [".exe", ".dll", ".so", ".dylib", ".app"],
    }

    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(desktop):
        if file.startswith("."):
            continue
        file_path = os.path.join(desktop, file)
        if not os.path.isfile(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()
        placed = False
        for category, extensions in categories.items():
            if ext in extensions:
                target = os.path.join(output_dir, category)
                os.makedirs(target, exist_ok=True)
                shutil.copy(file_path, os.path.join(target, file))
                print("Moved: {} -> {}".format(file, category))
                placed = True
                break

        if not placed:
            target = os.path.join(output_dir, "Others")
            os.makedirs(target, exist_ok=True)
            shutil.copy(file_path, os.path.join(target, file))
            print("Moved: {} -> Others".format(file))

    print("Cleanup complete! Files organized in: {}".format(os.path.abspath(output_dir)))

def main():
    print("Desktop Cleanup - Organize your files automatically!")
    cleanup_desktop()

if __name__ == "__main__":
    main()
