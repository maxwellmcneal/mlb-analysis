import pandas as pd
import time
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.onlyhomers.com/database"
path_to_chromedriver = 'C:/Users/cantq/OneDrive/Desktop'

# options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
# options.add_experimental_option(
#     "excludeSwitches", ['enable-automation'])
# options.add_argument(
#     "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
# options.add_argument("--remote-debugging-port=9222")
# driver = webdriver.Chrome(executable_path=path_to_chromedriver, options=options)

driver = webdriver.Chrome(executable_path=path_to_chromedriver)
driver.maximize_window()

driver.get(url)
time.sleep(2 + random.random()*3)

driver.find_element(By.XPATH, "/html/body[@class='has-navbar-fixed-top']/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/nav[@class='navbar navbar_text is-navbar_bg is-fixed-top has-navbar-centered']/div[@class='navbar-menu']/div[@class='navbar-end']/div[@class='navbar-item has-dropdown']/a[@class='navbar-link']").click()
time.sleep(2 + random.random()*3)

driver.find_element(By.XPATH, "/html/body[@class='has-navbar-fixed-top']/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/nav[@class='navbar navbar_text is-navbar_bg is-fixed-top has-navbar-centered']/div[@class='navbar-menu']/div[@class='navbar-end']/div[@class='navbar-item has-dropdown is-active']/div[@class='navbar-dropdown is-hidden-touch']/a[@class='navbar-item'][1]").click()

number = []
team = []
batter = []
hr = []
rob = []
inning = []
outs = []
angle = []
exit_velo = []
distance = []
pitch = []
pitcher = []
ballpark = []
date = []

counter = 0

while counter < 47:
    time.sleep(2 + random.random()*3)

    content = driver.page_source
    soup = BeautifulSoup(content)
    
    for element in soup.findAll(attrs={'data-label': 'Total'}):
        value = element.find('span')
        number.append(value.text)
    
    for element in soup.findAll(attrs={'data-label': 'Team'}):
        value = element.find('span')
        team.append(value.text)
        
    for element in soup.findAll(attrs={'data-label': 'Batter'}):
        value = element.find('span')
        batter.append(value.text)
        
    for element in soup.findAll(attrs={'data-label': 'HR'}):
        value = element.find('span')
        hr.append(value.text)
    
    for element in soup.findAll(attrs={'data-label': 'ROB'}):
        value = element.find('span')
        rob.append(value.text)
    
    for element in soup.findAll(attrs={'data-label': 'Inning'}):
        value = element.find('span')
        inning.append(value.text)

    for element in soup.findAll(attrs={'data-label': 'Outs'}):
        value = element.find('span')
        outs.append(value.text)
        
    for element in soup.findAll(attrs={'data-label': 'Angle'}):
        value = element.find('span')
        angle.append(value.text)
        
    for element in soup.findAll(attrs={'data-label': 'Exit Velo'}):
        value = element.find('span')
        exit_velo.append(value.text)
    
    for element in soup.findAll(attrs={'data-label': 'Distance'}):
        value = element.find('span')
        distance.append(value.text)
    
    for element in soup.findAll(attrs={'data-label': 'Pitch'}):
        value = element.find('span')
        pitch.append(value.text)
    
    for element in soup.findAll(attrs={'data-label': 'Pitcher'}):
        value = element.find('span')
        pitcher.append(value.text)
    
    for element in soup.findAll(attrs={'data-label': 'Ballpark'}):
        value = element.find('span')
        ballpark.append(value.text)
    
    for element in soup.findAll(attrs={'data-label': 'Date'}):
        value = element.find('span')
        date.append(value.text)
    
    
    driver.find_element(By.XPATH, "/html/body[@class='has-navbar-fixed-top']/div[@id='__nuxt']/div[@id='__layout']/div[@id='app']/div[@class='container']/div[@class='advanced']/div[@class='database_table']/div[@class='b-table']/div[@class='top level']/div[@class='level-right']/div[@class='level-item']/nav[@class='pagination']/a[@class='pagination-link pagination-next']/span[@class='icon']/i[@class='mdi mdi-chevron-right mdi-24px']").click()
    counter += 1
    print(f"Progress: Page {counter}/47")
    
 
driver.quit()
print("Progress: Finished")

results = pd.DataFrame({'Number': number,
                        'Team': team,
                        'Batter': batter,
                        'HR': hr,
                        'ROB': rob,
                        'Inning': inning,
                        'Outs': outs,
                        'Angle': angle,
                        'Exit Velo': exit_velo,
                        'Distance': distance,
                        'Pitch': pitch,
                        'Pitcher': pitcher,
                        'Ballpark': ballpark,
                        'Date': date
                        })

results.to_csv('data/2020_2_homers.csv', index=False)