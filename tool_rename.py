import os
import re

def rename_files(folder, pattern, replacement):
    for f in os.listdir(folder):
        new_name = re.sub(pattern, replacement, f)
        if f != new_name:
            old_path = os.path.join(folder, f)
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print(f"{f} → {new_name}")

# 示例：把空格替换为下划线
rename_files("photos", r" ", "_")
