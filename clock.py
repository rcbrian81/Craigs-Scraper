from datetime import datetime
from log import log
import time


def get_hour_and_minute():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	return now.hour, now.minute
def calculateSleepTime(hour,minute,wake_hour):
	sleep_hours = 0
	sleep_minutes = 0

	if hour < wake_hour:
		sleep_hours = wake_hour - wake_hour -1
	else:
		sleep_hours = (24 - hour) + wake_hour -1
	if sleep_hours < 0:
		sleep_hours = 0
	sleep_minutes = 60 - minute
	log(f"Sleeping for {sleep_hours} hours and {sleep_minutes} minutes")
	ttl_sleep_time_in_secs = (sleep_hours * 60*60) + (sleep_minutes*60)

	return ttl_sleep_time_in_secs
def sleep_until_hour(wake_hour):
	log(f"Going to sleep until {wake_hour} o'clock")
	hour, minute = get_hour_and_minute()
	sleep_time = calculateSleepTime(minute,hour,wake_hour)
	
	log(f"	{sleep_time} seconds")
	time.sleep(sleep_time)
def is_hour_in_range(hour,start_hour, end_hour):
    if start_hour <= end_hour:
        return start_hour <= hour <= end_hour
    else:
        return not (start_hour <= hour <= end_hour)
