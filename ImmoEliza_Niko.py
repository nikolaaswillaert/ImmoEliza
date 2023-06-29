import requests
from bs4 import BeautifulSoup
import re
import json
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor, as_completed
import concurrent.futures
import time
import pandas as pd
import traceback
import threading

# Function to scrape URLs
def scrape_urls(page_num):
    base_url = f"https://www.immoweb.be/en/search/house/for-sale?countries=BE&page={page_num}&orderBy=relevance"
    r = requests.get(base_url)
    soup = BeautifulSoup(r.content, "html.parser")
    
    urls = []
    for elem in soup.find_all("a", attrs={"class": "card__title-link"}):
        urls.append(elem.get('href'))
        
    # Save URLs to file - full_list.txt (local storage)
    with open("full_list.txt", "a") as f:
        for url in urls:
            f.write(url + '\n')
    return urls

def thread_scraping():
    full_list_url = []
    num_pages = 333

    # Create a list to store threads
    start_time = time.time()  # Start timer
    
    threads = []
    start_time = time.time()  # Start timer
    
    # Create and start threads
    for i in range(1, num_pages + 1):
        t = threading.Thread(target=lambda: full_list_url.extend(scrape_urls(i)))
        threads.append(t)
        t.start()

    # Wait for all threads to complete and then join
    for t in threads:
        t.join()

    end_time = time.time()  # Stop timer
    execution_time = end_time - start_time

    print("Scraping completed!")
    print("Total URLs scraped:", len(full_list_url))
    print("Total time:", execution_time, "seconds")
    return full_list_url

def scrape_house(url):
    """Scrapes all the info from a house listing"""
    # Get the house listing and make a soup
    failed_urls = []
    try:
        house_page = requests.get(url)
    except Exception:
            print("Error getting the GET request for the house URL")
            print("URL: ", url)
            failed_urls.append(url)
            print("Waiting for 5 seconds until next url request")
            time.sleep(5)
            house_page = requests.get(url)
            
    house_page = BeautifulSoup(house_page.text, 'html.parser')
    final_dictionary = {}

    # Get the hidden info from the java script
    regex = r"window.classified = (\{.*\})"
    script = house_page.find('div',attrs={"id":"main-container"}).script.text
    script = re.findall(regex, script)
    try:
        script = json.loads(script[0])
    except:
        return {}

    final_dictionary = {}
    #Locality
    try:
        final_dictionary['locality'] = script['property']['location']['locality']
    except:
        final_dictionary['locality'] = 'UNKNOWN'
    #type of property
    try:
        final_dictionary['type of property'] = script['property']['type']
    except:
        final_dictionary['type of property'] = 'UNKNOWN'
    #subtype of property
    try:
        final_dictionary['subtype of property'] = script['property']['subtype']
    except:
        final_dictionary['subtype of property'] = 'UNKNOWN'
    #price
    try:
        final_dictionary['price'] = script['price']['mainValue']
    except:
        final_dictionary['price'] = 'UNKNOWN'
    #- Number of rooms
    try:
        final_dictionary['number_rooms'] = script['property']['bedroomCount']
    except:
        final_dictionary['number_rooms'] = 'UNKNOWN'
    # living area
    try:
        final_dictionary['living_area'] = script['property']['netHabitableSurface']
    except:
        final_dictionary['living_area'] = 'UNKNOWN'
    # Fully equipped kitchen (Yes/No)
    try:
        final_dictionary['kitchen'] = script['property']['kitchen']['type']
    except:
        final_dictionary['kitchen'] = 0
    # NOT INSTALLED / INSTALLED 
    # Furnished (Yes/No)
    try:
        final_dictionary['furnished'] = script['transaction']['sale']['isFurnished']
    except:
        final_dictionary['furnished'] = 'UNKNOWN'
    # Open fire (Yes/No)
    try:
        final_dictionary['fireplace'] = script['property']['fireplaceCount']
    except:
        final_dictionary['fireplace'] = 0
    # Terrace (Yes/No)
    try:
        final_dictionary['terrace'] = script['property']['hasTerrace']
    except:
        final_dictionary['terrace'] = 0
    # If yes: Area
    try:
        final_dictionary['terrace_area'] = script['property']['terraceSurface']
    except: 
        final_dictionary['terrace_area'] = 0
    # Garden
    try:
        final_dictionary['garden'] = script['property']['hasGarden']
    except:
        final_dictionary['garden'] = 0
    #- If yes: Area
    try:
        final_dictionary['garden_area'] = script['property']['gardenSurface']
    except:
        final_dictionary['garden_area'] = 0
    # Surface of the land
    try: 
        final_dictionary['surface_land'] = script['property']['land']['surface']
    except:
        final_dictionary['surface_land'] = "UNKNOWN"
    # Surface area of the plot of land - TO ASK
    # Number of facades
    try:
        final_dictionary['number_facades'] = script['property']['building']['facadeCount']
    except:
        final_dictionary['number_facades'] = "UNKNOWN"
    # Swimming pool (Yes/No)
    try:
        final_dictionary['swimming_pool'] =  script['property']['hasSwimmingPool']
    except:
        final_dictionary['swimming_pool'] = 0
    # State of the building (New, to be renovated, ...)
    try:
        final_dictionary['building_state'] = script['property']['building']['condition']
    except:
        final_dictionary['building_state'] = 'UNKNOWN'

    return final_dictionary

# CHANGE  THIS TO LOOP OVER ALL THE URLS IN URL LINKS LIST OR TXT FILE
# CALL THIS FUNCTION IF NOT FULL_LIST_20k.txt available: houses_links = thread_scraping()
def create_dataframe():
    houses_links = thread_scraping()
    print("Scraping of the URL links has finished")
    # houses_links = []    
    # with open("./full_list_20k.txt", "r") as f:
    #       count = 0
    #       for url in f:
    #           if count < 2000:
    #               houses_links.append(url)
    #               count +=1
    #           else:
    #               break

    print("")
    print("Scraping individual pages...")
    start_time = time.time()
    # Start timer
    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit the scraping tasks to the executor
        futures = [executor.submit(scrape_house, url) for url in houses_links]

        # Retrieve the results as they become available
        for future in concurrent.futures.as_completed(futures):
            data = future.result()
            results.append(data)

    df = pd.DataFrame(results)

    end_time = time.time()  # Stop timer
    execution_time = end_time - start_time

    print("Scraping completed!")
    print("Total time spent scraping:", execution_time, "seconds")
    df.to_csv('dataframe.csv', index = True)
      
    
create_dataframe()

