# mlb-analysis
Analysis of MLB data

## Files
* [onlyhomers_scraper.py](onlyhomers_scraper.py)
  * This is a quick and ugly web scraper I made to scrape www.onlyhomers.com/database. 
    I wanted data on all homeruns hit in major league baseball, and I found this website that had a database of all home runs since 2020. 
    So I built this web scraper to download all the data off the website. This was my first time creating a web scraper for dynamically loaded content, so it has a bunch of problems. 
    It throws errors when run in headless mode, you have to manually change the code to scrape different years, and it may fail depending on the ads loaded on the page. 
    However, I made it in an afternoon and it worked just enough for the task I needed it for.
    
    This was made before I learned about the statcast search function at https://baseballsavant.mlb.com/statcast_search. Statcast search is a better source for this information. 
    For the data I am concerned with, specifically exit velocity and launch angle, statcast goes back to 2015, instead of 2020 on onlyhomers. 
    For the rest of the project, I will be using data obtained through statcast search. 
    However, this web scraper still has some value. onlyhomers updates in real time as more homeruns are hit, as opposed to statcast, which I believe updates overnight each day.
    So, this web scraper could be modified to run continuously, detecting changes in the database to add new homers as they occur, instead of waiting until the next day to include new homeruns.
    
