import csv
import requests

BASE_URL = 'https://api.mantissa.finance/'
url = BASE_URL + 'api/pool/stats/tvl/user/34443/'

with open('tvl.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['user', 'amount'])
    response = requests.get(url)
    response_dict = response.json()
    for user, amount in response_dict.items():
        csvwriter.writerow([user, amount])
