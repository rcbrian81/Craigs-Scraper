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
	sleep_minutes = 60 - minute

	ttl_sleep_time_in_secs = (sleep_hours * 60*60) + (sleep_minutes*60)

	return ttl_sleep_time_in_secs
def sleep_until_hour(wake_hour):
	log(f"Going to sleep until {wake_hour} o'clock")
	minute, hour = get_hour_and_minute()
	sleep_time = calculateSleepTime(minute,hour,wake_hour)
	
	log(f"	{sleep_time} seconds")
	time.sleep(sleep_time)


