import speedtest
import csv
import time
from datetime import datetime

with open(r"C:\Users\Orel\OneDrive\שולחן העבודה\DevOps\git repositories\learning code\python\speedtest\speedtest.csv", "x", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Timestamp", "Download Speed (Mbps)", "Upload Speed (Mbps)"]) #מדוע בקובץ הCSV אני רואה מרכאות 

def log_speed(): 
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000
    upload_speed = st.upload() / 1000000

    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(r"C:\Users\Orel\OneDrive\שולחן העבודה\DevOps\git repositories\learning code\python\speedtest\speedtest.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([timestamp, round(download_speed, 3), round(upload_speed, 3)])

while True:
    log_speed()
    time.sleep(300)
