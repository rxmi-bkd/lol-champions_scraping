import os

import pandas as pd

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

if __name__ == '__main__':
    df = pd.read_csv('languages.csv')
    codes = df.code.tolist()

    if not os.path.exists('champions_name'):
        os.makedirs('champions_name')

    driver = webdriver.Chrome()

    for code in codes:
        champions_name = []
        url = f'https://universe.leagueoflegends.com/{code}/champions/'

        driver.get(url)
        sleep(5) # Wait for the page to load

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        champions_ul = soup.find_all('ul', class_='champsListUl_2Lmb')

        for row in champions_ul:
            champions_li = row.find_all('li')

            for champion in champions_li:
                name = champion.find('h1').text
                link_name = champion.find('a').get('href').split('/')[3]

                champions_name.append([name, link_name])

        # Save the data for the current language
        df = pd.DataFrame(champions_name, columns=['name', 'link_name'])
        df.to_csv(f'champions_name/champions_name_{code}.csv', index=False)

    driver.quit()
