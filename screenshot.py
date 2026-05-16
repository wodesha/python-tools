import os
from PIL import ImageGrab

def take_screenshot(filename="screenshot.png", duration=3):
    "Take a screenshot after a short delay"
    time.sleep(duration)
    img = ImageGrab.grab()
    img.save(filename)
    print("Screenshot saved: {}".format(os.path.abspath(filename)))
    return filename

if __name__ == "__main__":
    import sys
    duration = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    take_screenshot(duration=duration)
