import time

def schedule(job, interval_minutes=60):
    "Run a job every X minutes"
    while True:
        print("Running job at {}".format(time.strftime("%H:%M:%S")))
        job()
        time.sleep(interval_minutes * 60)

def daily_report():
    print("Generating daily report...")

if __name__ == "__main__":
    import sys
    minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    schedule(daily_report, interval_minutes=minutes)
