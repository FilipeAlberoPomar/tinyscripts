# WORK IN PROGRESS
# Fetcher of italian city data.

import requests, os
from random import randint
from time import sleep

#url = 'https://finanzalocale.interno.gov.it/apps/floc.php/certificati/index/codice_ente/1010020030/cod/4/anno/2008/md/0/cod_modello/CCOU/tipo_modello/U/cod_quadro/03'
BASE_URL = 'https://finanzalocale.interno.gov.it/apps/floc.php/certificati/index/codice_ente/{city_code}/cod/4/anno/{year}/md/0/cod_modello/CCOU/tipo_modello/U/cod_quadro/03'
HEADERS = {'user-agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'}

cities = {
    "Alessandria": "1010020030" 
}

START_YEAR = 1996
END_YEAR = 2009
BASE_FOLDER = 'scrapper'

def download():
    for name, code in cities.items():
        print("%s's code is %s" % (name, code))
       
        if not os.path.exists(BASE_FOLDER):
            os.mkdir(BASE_FOLDER)

        if not os.path.exists(BASE_FOLDER+'//'+name):
            os.mkdir(BASE_FOLDER+'//'+name)

        for year in range(START_YEAR, END_YEAR+1):
            url = BASE_URL.format(city_code=code, year=year)
            print(url)
            response = requests.get(url, headers=HEADERS)

            file_name = BASE_FOLDER+'//'+name+'//'+str(year)+'.html' 
            f = open(file_name, 'w')
            print(response)
            f.write(response.text)

            sleep(randint(1,3))

def parse():

    for root, dirs, files in os.walk(BASE_FOLDER):
        print('a')
        print(root)
        for file in files:
            print('b')
            print(file)
            #append the file name to the list
                

    print('parse')
    
    
if __name__ == '__main__':
    parse()



#
#
#print(r.text)