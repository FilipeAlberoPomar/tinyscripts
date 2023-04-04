# WORK IN PROGRESS
# Brace! Brace! Ugly, unifished code below
# This script downloads and parses financial information from italian cities

import requests, os
from random import randint
from time import sleep
from bs4 import BeautifulSoup

#url = 'https://finanzalocale.interno.gov.it/apps/floc.php/certificati/index/codice_ente/1010020030/cod/4/anno/2008/md/0/cod_modello/CCOU/tipo_modello/U/cod_quadro/03'
BASE_URL = 'https://finanzalocale.interno.gov.it/apps/floc.php/certificati/index/codice_ente/{city_code}/cod/4/anno/{year}/md/0/cod_modello/CCOU/tipo_modello/U/cod_quadro/03'
HEADERS = {'user-agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'}

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

            file_name = "{}/{}-{}.html".format(OUTPUT_FOLDER, city_name,year) 

            if not os.path.exists(file_name):
                url = BASE_URL.format(city_code=city_code, year=year)
                response = requests.get(url, headers=HEADERS)
                file = open(file_name, 'w')
                file.write(response.text)
                sleep(randint(1,3))

def extract():

    files = os.listdir(OUTPUT_FOLDER)

    for file_name in sorted(files):

        if '.html' in file_name:
            canonical_file = "{}/{}".format(OUTPUT_FOLDER, file_name)

            print('Processing: '+canonical_file)
            f = open(canonical_file)
            text = f.read()
            
            if 'Dati assenti' in text:
                print("no data")

            else: 
                soup = BeautifulSoup(text, 'html.parser')
                table = soup.find(class_='table table-striped table-bordered table-condensed')
                money = table.tr.next.next.next.next.next.next.next.next.next.next.next.next.contents[0]
                print(money)
            
            print("\n")

    
if __name__ == '__main__':
    extract()