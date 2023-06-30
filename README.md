# ImmoEliza
Scrape Immo websites + build database + build machine learning model
This is a immoweb scraping project that required to extract all the immo data in belgium and build a clean dataset for future prediction.
https://www.immoweb.be/ is our source website to extract over 17,000 properties from 333 pages.
17 property features have been extracted, including locality, type of property, subtype of property, price, number_rooms etc.
Whole process includes url scraping, features information extracting,dataset building and data cleaning.
There are 9 modules imported for the process, 5 of them- requests, bs4, re, json, pandas-are the main modules and another
modules- concurrent.futures, time, threading and sys- are side modules to improve the efficiency of the progress and keep the output clean.
