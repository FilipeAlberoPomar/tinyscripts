# WORK IN PROGRESS
# Brace! Brace! Ugly, unifished code below
# This script downloads and parses financial information from italian cities

import os
from random import randint
from time import sleep
import requests
from bs4 import BeautifulSoup

CITY_URL = "https://finanzalocale.interno.gov.it/apps/floc.php/indicatori/index/codice_ente/{city_code}/anno/{year}/cod/8/md/0/tipo_certificato/C/tipo_ente/CO"
HEADERS = {'user-agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'}

cities = {
    "Lucca": "3090430170"
}

START_YEAR = 1998
END_YEAR = 2011

OUTPUT_FOLDER = 'scrapper'


def fetch():

    if not os.path.exists(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)

    for city_name, city_code in cities.items():

        for year in range(START_YEAR, END_YEAR+1):

            file_name = f'{OUTPUT_FOLDER}/{city_name}-{year}.html'

            if not os.path.exists(file_name):
                url = CITY_URL.format(city_code=city_code, year=year)
                print(f"Fetching {city_name} for {year}")
                response = requests.get(url, headers=HEADERS, timeout=2)

                file = open(file_name, 'w', encoding='iso-8859-1')
                file.write(response.text)

                sleep(randint(1, 2))


def extract():

    files = os.listdir(OUTPUT_FOLDER)

    for file_name in sorted(files):
        file_name_chunks = file_name.replace('.html','').split('-')
        city = file_name_chunks[0]
        year = file_name_chunks[1]

        if '.html' in file_name:
            canonical_file = f"{OUTPUT_FOLDER}/{file_name}"

            #print(f'Processing {file_name}')
            file = open(canonical_file,encoding='iso-8859-1')
            html = file.read()

            csv_line = ""

            if 'Non esistono indicatori finanziari' in html:
                csv_line = f"{file_name};0;0;0;0"

            else:
                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find(class_='table table-striped table-bordered table-condensed')
                row = table.contents[5]
                valore_ente = row.contents[1].text.strip()
                valore_provincia = row.contents[3].text.strip()
                valore_regione = row.contents[5].text.strip()
                valore_nazione = row.contents[7].text.strip()

                csv_line = f"{city};{year};{valore_ente};{valore_provincia};{valore_regione};{valore_nazione}"

            print(csv_line)



if __name__ == '__main__':
    fetch()
    extract()
