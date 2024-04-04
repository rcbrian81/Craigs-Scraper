#Improvement: Make Key Phrases matching faster.
import scraper
import time
import messager

print("Running coordinator.py")
matches = {}
key_phrases = ['must take all','sectional','bike','table','chair','free','couch','sofa','bed','mattress','dresser','desk','dining']
def look_for_new_maches():
    
    new_items = scraper.look_for_new_titles()
    matches.clear()

    print(f"{len(new_items)} new items found.")
    if len(new_items) == 0: 
        print("*No new items where added")
    for key in new_items:
        new_title = key
        for phrase in key_phrases:
            if phrase in new_title.lower():
                print(f"    MATCH: {new_title}")
                matches[new_title] = new_items[new_title]
                break
    
    


cycleCount = 0
while(True):
    cycleCount += 1
    print(f"{cycleCount} New cycle === === === === === === === === === === === === === === === === === === === === = {cycleCount}")
    look_for_new_maches()
    if cycleCount > 1:
        messager.send_emails(matches)
    this_many_seconds = 120
    time.sleep(this_many_seconds)
    

print("exiting coordinator.py")
