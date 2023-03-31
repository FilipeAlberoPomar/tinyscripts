# WORK IN PROGRESS
# Fetcher of italian city data.

import requests 

url = 'https://finanzalocale.interno.gov.it/apps/floc.php/certificati/index/codice_ente/1010020030/cod/4/anno/2008/md/0/cod_modello/CCOU/tipo_modello/U/cod_quadro/03'
headers = {'user-agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'}

r = requests.get(url, headers=headers)

print(r.text)