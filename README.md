# Python 实用工具合集

## 简介
10个日常必备的 Python 小工具，每个不到 20 行代码，解决实际问题。

---

### 1. 自动整理桌面文件
```python
import os, shutil
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
for f in os.listdir(desktop):
    ext = f.split(".")[-1].lower()
    folder = os.path.join(desktop, ext)
    os.makedirs(folder, exist_ok=True)
    shutil.move(os.path.join(desktop, f), folder)
```

### 2. 批量重命名文件
```python
import os
folder = "photos"
for f in os.listdir(folder):
    if f.endswith(".jpg"):
        os.rename(os.path.join(folder, f), os.path.join(folder, f.replace(" ", "_")))
```

### 3. 监控文件夹变化
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"新文件: {event.src_path}")
observer = Observer()
observer.schedule(Handler(), path="watch", recursive=True)
observer.start()
```

### 4. 抓取网页标题
```python
from bs4 import BeautifulSoup
import requests
r = requests.get("https://example.com")
soup = BeautifulSoup(r.text, "html.parser")
print(soup.title.text)
```

### 5. 批量转换 CSV 到 Excel
```python
import pandas as pd
for csv in ["sales.csv", "orders.csv", "products.csv"]:
    df = pd.read_csv(csv)
    df.to_excel(csv.replace(".csv", ".xlsx"), index=False)
```

### 6. 自动发送邮件
```python
import smtplib
from email.message import EmailMessage
msg = EmailMessage()
msg["From"] = "you@gmail.com"
msg["To"] = "boss@gmail.com"
msg["Subject"] = "每日报告"
msg.set_content("今日销售额：¥1,234")
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
    s.login("you@gmail.com", "password")
    s.send_message(msg)
```

### 7. 定时执行任务
```python
from schedule import every, run_pending
import time
def job():
    print("执行任务...")
every(1).hours.do(job)
while True:
    run_pending()
    time.sleep(60)
```

### 8. 读取 Excel 数据
```python
import pandas as pd
df = pd.read_excel("data.xlsx")
print(df.head())
print(f"总行数: {len(df)}")
print(f"总列数: {len(df.columns)}")
```

### 9. 自动截图
```python
from PIL import ImageGrab
img = ImageGrab.grab()
img.save("screenshot.png")
```

### 10. 批量下载图片
```python
import requests
urls = ["https://img1.jpg", "https://img2.jpg", "https://img3.jpg"]
for url in urls:
    r = requests.get(url)
    with open(url.split("/")[-1], "wb") as f:
        f.write(r.content)
```

---

**用法**：
```bash
git clone https://github.com/yourname/python-tools.git
cd python-tools
python tool1.py
```

**关于作者**：
- GitHub: @wodesha
- 赞助: https://github.com/sponsors/wodesha
