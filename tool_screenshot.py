from PIL import ImageGrab
import time

def take_screenshot(filename="screenshot.png", duration=5):
    time.sleep(duration)
    img = ImageGrab.grab()
    img.save(filename)
    print(f"Screenshot saved as {filename}")

take_screenshot()
