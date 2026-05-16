import os
import time

def monitor_folder(folder_path, interval=5):
    "Monitor a folder for changes and print updates"
    last_mod = {}
    print("Monitoring: {}".format(folder_path))
    while True:
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                mod_time = os.path.getmtime(file_path)
                if file in last_mod and last_mod[file] != mod_time:
                    print("Modified: {} at {}".format(file, time.ctime(mod_time)))
                last_mod[file] = mod_time
        time.sleep(interval)

# 示例：监控桌面文件夹
if __name__ == "__main__":
    import sys
    folder = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Desktop")
    monitor_folder(folder)
