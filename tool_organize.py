import os
import shutil

# 自动整理桌面文件
def organize_desktop():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    for f in os.listdir(desktop):
        if f.startswith("."):
            continue
        ext = f.split(".")[-1].lower()
        folder = os.path.join(desktop, ext)
        os.makedirs(folder, exist_ok=True)
        old = os.path.join(desktop, f)
        new = os.path.join(folder, f)
        try:
            shutil.move(old, new)
            print(f"{f} → {ext}/")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("整理桌面文件...")
    organize_desktop()
    print("完成！")
