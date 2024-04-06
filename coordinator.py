#Improvement: Make Key Phrases matching faster.
from datetime import datetime
from log import log
import messanger
import scraper
import clock
import time


start_hour = 5
end_hour = 23
interval_time_seconds = 60

log("Running coordinator.py")
matches = {}
key_phrases = ['must take all','sectional','sofa''clothes','cat tree','cat tower','hanger','mirror','planter']
def look_for_new_maches():
    
    new_items = scraper.look_for_new_titles()
    matches.clear()

    log(f"{len(new_items)} new items found.")
    if len(new_items) == 0: 
        log("*No new items where added")
    for key in new_items:
        new_title = key
        for phrase in key_phrases:
            if phrase in new_title.lower():
                log(f"    MATCH: {new_title}")
                matches[new_title] = new_items[new_title]
                break
    
    


cycleCount = 0
while(True):
    current_hour, current_minute = clock.get_hour_and_minute()

    if current_hour > 5 and current_hour < end_hour:
        cycleCount += 1
        log(f"{cycleCount} New cycle === === === === === === === === === === === === === === === === === === === === = {cycleCount}")
        look_for_new_maches()
        if cycleCount > 1:
            messanger.send_emails(matches)
        time.sleep(interval_time_seconds)
    else:
        log(f"It is {current_hour}:{current_minute}")
        clock.sleep_until_hour(start_hour)
    

log("exiting coordinator.py")
