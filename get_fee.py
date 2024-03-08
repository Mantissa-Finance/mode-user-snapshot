import csv
import requests

BASE_URL = 'https://api.mantissa.finance/'
url = BASE_URL + 'api/pool/stats/volume/user/34443/'

with open('fee.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['user', 'volume', 'fee rate', 'fees'])
    response = requests.get(url)
    response_dict = response.json()
    for user, amount in response_dict.items():
        csvwriter.writerow([user, amount, '0.01%', amount * 0.0001])
