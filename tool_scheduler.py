import time

def schedule(job, interval_minutes=60):
    while True:
        print(f"Running job at {time.strftime('%H:%M:%S')}")
        job()
        time.sleep(interval_minutes * 60)

def daily_report():
    print("Generating daily report...")

schedule(daily_report, interval_minutes=60)
