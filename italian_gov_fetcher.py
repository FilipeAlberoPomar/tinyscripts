# WORK IN PROGRESS
# Brace! Brace! Ugly, unifished code below
# This script downloads and parses financial information from italian cities

import requests
import os
from random import randint
from time import sleep
from bs4 import BeautifulSoup

BASE_URL = 'https://finanzalocale.interno.gov.it/apps/floc.php/certificati/index/codice_ente/{city_code}/cod/4/anno/{year}/md/0/cod_modello/CCOU/tipo_modello/U/cod_quadro/03'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'}

cities = {
    "Alessandria": "1010020030"
}

START_YEAR = 1996
END_YEAR = 2009

OUTPUT_FOLDER = 'scrapper'


def fetch():

    if not os.path.exists(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)

    for city_name, city_code in cities.items():

        for year in range(START_YEAR, END_YEAR+1):

            file_name = f'{OUTPUT_FOLDER}/{city_name}-{year}.html'

            if not os.path.exists(file_name):
                
                url = BASE_URL.format(city_code=city_code, year=year)
                print(f"Fetching {city_name} for {year}")
                response = requests.get(url, headers=HEADERS, timeout=2)

                file = open(file_name, 'w', encoding='iso-8859-1')
                file.write(response.text)

                sleep(randint(1, 2))


def extract():

    files = os.listdir(OUTPUT_FOLDER)

    for file_name in sorted(files):

        if '.html' in file_name:
            canonical_file = f"{OUTPUT_FOLDER}/{file_name}"

            print(f'Processing {file_name}')
            file = open(canonical_file,encoding='iso-8859-1')
            html = file.read()

            if 'Dati assenti' in html:
                print("no data")

            else:
                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find(class_='table table-striped table-bordered table-condensed')
                money = table.tr.next.next.next.next.next.next.next.next.next.next.next.next.contents[0]
                print(money)

            print("\n")


if __name__ == '__main__':
    fetch()
    extract()
