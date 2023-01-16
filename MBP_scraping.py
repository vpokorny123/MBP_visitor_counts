#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:03:54 2023

@author: pokor076
"""

import requests
import matplotlib.pyplot as plt
import time
#import schedule
from datetime import datetime, timedelta

occupancy_data = []
def job():
    response = requests.get('https://portal.rockgympro.com/portal/public/18a5ea0176c6494befd44f163f15750c/occupancy?&iframeid=occupancyCounter&fId=')
    txt = response.text.split('\n')
    countline = txt[88].split(':')
    visitors = int(countline[-1].split(',')[0])
    raw_time = time.localtime()
    time_real = time.asctime(raw_time)
    occupancy_data.append((raw_time, time_real, visitors))
    print("Running job...")
    #return schedule.CancelJob
    
now = datetime.now()

# Get today's date
today = datetime(now.year, now.month, now.day)

next_run = datetime.now()
week = datetime.now() + timedelta(days=7)

while True:
    now = datetime.now()
    if now.minute % 10 == 0 and now > next_run :
        job()
        next_run = now + timedelta(minutes=10)
    if datetime.now() > week:
        break
    time.sleep(1)


#start_time = time.time()
#week = start_time + (7 * 24 * 60 * 60)

#while time.time() < week:
#    schedule.every(1).minutes.do(job)
#    schedule.run_pending()
#    if time.time() - start_time >= 60:
#        start_time = time.time()
#        schedule.clear()
#    time.sleep(1)
    
    
# Run the job for a week
#for _ in range(5): # 24*7*10 = 10080
#    schedule.run_pending()
#    time.sleep(1)
#start_time = datetime.datetime.now()
#week = start_time + datetime.timedelta(days=7)

#while datetime.datetime.now() < week:
#    schedule.run_pending()
#    time.sleep(1)
    
#while True:
#    schedule.run_pending()
#    time.sleep(1)



#while True:
    
    #time.sleep(300)

raw_times, times, visitors = zip(*occupancy_data)
short_time = [str(x.tm_hour)+':' + str(x.tm_min) for x in raw_times]
days_of_week = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
day_name = [days_of_week[x.tm_wday] for x in raw_times]
x_ax = [i + ' ' + j for i, j in zip(day_name, short_time)]
plt.plot(x_ax, visitors)
plt.xlabel('Time')
plt.ylabel('Visitors')
plt.show()