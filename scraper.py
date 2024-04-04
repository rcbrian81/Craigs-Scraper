from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
import time
from PIL import Image
import pickle
import os
print("Running scraper.py")
#Improvment only load data as needed
#could use dictionary/hashtable to improve search through titles but would cost memory and storage. 
#would require more consideration for a larger project. 

url = 'https://losangeles.craigslist.org/search/zip#search=1~gallery~0~0'

data_file_name = "titles.pkl"

def scroll_down(d):
            d.execute_script("window.scrollTo(0,document.body.scrollHeight);")

def look_for_new_titles():
    #print("running look_for_new_titles() in scraper.py")
    print("looking for new titles")
    titles = get_titles()
    new_titles = {}
    max_listing_to_look_at = 20

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)
    scroll_down(driver)

    listing_containers = driver.find_elements(By.CLASS_NAME, "gallery-card")
    listing_containers = listing_containers[0:max_listing_to_look_at]
    print(f"{len(listing_containers)} listings retrived from website.")

    for container in listing_containers:
        link_element = container.find_element(By.CSS_SELECTOR, "a.cl-app-anchor.text-only.posting-title")
        href = link_element.get_attribute("href")

        title_element = link_element.find_element(By.CLASS_NAME, "label")
        title  = title_element.text 

        if title not in titles:
            titles.append(title)
            new_titles[title] = href
            print(f"    Added new title: {title[:len(title)//3]}...")
    #print(titles[0:5])
    # print(f"Num items found: {len(item_containers)}")


    
    print(f"Have {len(titles)} total titles")
    with open(data_file_name, 'wb') as file:
        startIndex = len(titles)-max_listing_to_look_at
        endIndex = len(titles)-1
        print(f"Start: {startIndex} End: {endIndex}")
        pickle.dump(titles[startIndex:endIndex+1], file)
    print("exiting look_for_new_titles() in scraper.py")
    return new_titles

def get_titles():
    titles = []
    try:
        with open(data_file_name, 'rb') as file:
            titles = pickle.load(file)
    except FileNotFoundError:
        print(f"{data_file_name} doesn't exist. It will be created when saving data.")

    print(f"Previous titles found: {len(titles)}")
    for title in titles:
        print('        ' +title[:len(title)//3] + '...')
    return titles

