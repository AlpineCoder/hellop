import time
import datetime

while True:
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print date_time + " hello world"
    time.sleep(5)
