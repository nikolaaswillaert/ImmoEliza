# ImmoEliza
Scrape Immo websites + build database + build machine learning model

Developed by Team 'The 3 Scrapeteers’ : Nikolaas, Sam, Weiying

Timeline: 4 days (Creation: 2 days,  Modification: 1 day,   Optimization: 1 day)

Goal of the project: A clean dataset for sales prediction

Source website: https://www.immoweb.be/ 

Steps of the process: url scraping, features information extracting, dataset building and data cleaning. 

Output of the project: 

1. Immo data of over 17,000 properties from 333 pages.
2. 17 property features : locality, type of property, subtype of property, price, number_rooms, living_area, kitchen, furnished, fireplace, terrace, terrace_area, garden, garden_area, surface_land, number_facades, swimming_pool, building_state
3. 9 modules imported: Requests, bs4, re, json, pandas-are the main modules.  Concurrent.futures, time, threading and sys are modules for speeding up data collection and simplifying output.  
4. A clean dataset without empty rows and duplicates.
