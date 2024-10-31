import os
import bs4

import pandas as pd

from time import sleep

from numpy.distutils.lib2def import output_def
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver

def get_champion_data(champion_link_name: str, driver: WebDriver = None, language: str = 'en_GB') -> dict:
    champion = {
        'link_name': champion_link_name,
        'name': None,
        'surname': None,
        'race': None,
        'role': None,
        'region': None,
        'quote': None,
        'image': None,
        'image_spell_1': None,
        'image_spell_2': None,
        'image_spell_3': None,
        'image_spell_4': None,
        'image_passive': None,
    }

    driver.get(f'https://universe.leagueoflegends.com/{language}/champion/{champion_link_name}/')
    sleep(3)

    champion_soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    try:
        name = champion_soup.find('li', attrs={'class': 'quote_2507'}).find('h5').text
    except AttributeError:
        name = None

    try:
        surname = champion_soup.find('h3', attrs={'class': 'subheadline_rlsJ'}).text
    except AttributeError:
        surname = None

    try:
        race = champion_soup.find('div', attrs={'class': 'race_3k58'}).find('h6').text
    except AttributeError:
        race = None

    try:
        role = champion_soup.find('div', attrs={'class': 'typeDescription_ixWu'}).find('div').find('h6').text
    except AttributeError:
        role = None

    try:
        quote = champion_soup.find('li', attrs={'class': 'quote_2507'}).find('p').text
    except AttributeError:
        quote = None

    try:
        region = champion_soup.find('div', attrs={'class': 'factionText_EnRL'}).find_all('span')[1].text
    except AttributeError:
        region = None
    except IndexError:
        region = None

    champion['name'] = name.replace('~ ', '')
    champion['surname'] = surname
    champion['race'] = race
    champion['role'] = role
    champion['quote'] = quote
    champion['region'] = region

    driver.get(f'https://www.leagueoflegends.com/{language.replace("_", "-")}/champions/{champion_link_name}/')
    sleep(3)

    champion_soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    try:
        image = champion_soup.find('div', attrs={'class': 'sc-cf6885cf-0 dfGzkK media-viewport'}).find('img').get('src')
    except AttributeError:
        image = None

    champion['image'] = image

    try:
        spells_li = champion_soup.find('div', attrs={'class': 'icon-tab--tabs'}).find_all('li')
    except AttributeError:
        spells_li = []

    for i, spell in enumerate(spells_li):
        try:
            spell_image = spell.find('img').get('src')
        except AttributeError:
            spell_image = None

        if i == 0:
            champion['image_passive'] = spell_image
        else:
            champion[f'image_spell_{i}'] = spell_image

    return champion


if __name__ == '__main__':
    file_languages = 'languages.csv'
    file_champions_name = 'champions_name/champions_name_en_gb.csv'

    output_dir = 'champions_data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = pd.read_csv(file_languages)
    codes = df.code.tolist()

    df = pd.read_csv(file_champions_name)
    link_names = df.link_name.tolist()

    d = Chrome()

    # for code in codes:
    for code in ['en_gb']:
        champions_data = []
        for link_name in link_names:
            champion_data = get_champion_data(link_name, d, code)
            champions_data.append(champion_data)

        df = pd.DataFrame.from_records(champions_data)
        df.to_csv(f'{output_dir}/champions_data_{code}.csv', index=False)

    d.quit()


    files = os.listdir(output_dir)
    lane_dr_df = pd.read_csv('champions_lane_and_date_release.csv')

    for file in files:
        df = pd.read_csv(f'{output_dir}/{file}')

        merged = pd.merge(df, lane_dr_df, on='link_name', how='left')
        merged.to_csv(f'{output_dir}/{file}', index=False)

        df = pd.read_csv(f'{output_dir}/{file}')

        df = df[['link_name', 'name', 'surname', 'race', 'role', 'region', 'quote', 'lane', 'date_release',
                         'image', 'image_spell_1', 'image_spell_2', 'image_spell_3',
                         'image_spell_4', 'image_passive']]

        df.to_csv(f'{output_dir}/{file}', index=False)