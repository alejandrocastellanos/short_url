# coding=utf-8
"""
Install
    brew install --cask chromedriver
open terminal
    which chromedriver
    xattr -d com.apple.quarantine path/
"""
import csv
import time
import uuid

import requests


class Scraper:

    @staticmethod
    async def create_csv(short_url: list):
        header = ['Long URL', 'Short URL']
        with open('short_urls_3.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(short_url)

    def scraping(self, long_url):
        import urllib.parse
        prepare_url = "https://cutt.ly/api/api.php?key=a6de113b169c03ae80dcf81669ce55a63c924&short=" + urllib.parse.quote('https://segurocelular.grupor5.com/?firstname=ERIKA&lastname=DIAZ&identification=52928145&mobilephone=3132345677&email=milengaflorfet@gmail.com&identificationType=ID ')
        response = requests.get(prepare_url)
        json_response = response.json()
        short_url = json_response['url']['shortLink']
        return short_url
#tempplate_1alejo@yopmail.com



import urllib.parse
import requests
scraper = Scraper()
#short urls
header = ['Long URL', 'Short URL']
with open('short_urls.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    with open('urls.csv', 'r') as file:
        reader = csv.reader(file)
        count = 0
        for url in reader:
            count += 1
            api1 = 'b1cd55f3edae4114ec16500085947f849d019'
            api2 = 'a6de113b169c03ae80dcf81669ce55a63c924'
            api3 = 'fe78ca9c96f6e22dac0c70230fdafc8d2e7be'
            try:
                if count == 1:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api1}&short={urllib.parse.quote(url[0])}"
                elif count == 2:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api2}&short={urllib.parse.quote(url[0])}"
                elif count == 3:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api3}&short={urllib.parse.quote(url[0])}"
                elif count == 4:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api1}&short={urllib.parse.quote(url[0])}"
                elif count == 5:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api2}&short={urllib.parse.quote(url[0])}"
                elif count == 6:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api3}&short={urllib.parse.quote(url[0])}"
                elif count == 7:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api1}&short={urllib.parse.quote(url[0])}"
                elif count == 8:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api2}&short={urllib.parse.quote(url[0])}"
                elif count == 9:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api3}&short={urllib.parse.quote(url[0])}"
                elif count == 10:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api1}&short={urllib.parse.quote(url[0])}"
                elif count == 11:
                    prepare_url = f"https://cutt.ly/api/api.php?key={api3}&short={urllib.parse.quote(url[0])}"
                r = requests.get(prepare_url)
                json_response = r.json()
                data_url = json_response.get('url')
                print(url[0], data_url.get('shortLink'), count)
                writer.writerow([url[0], data_url.get('shortLink')])
            except Exception as e:
                print('Error', e)
                writer.writerow([url[0], None])
            if count == 11:
                time.sleep(55)
                count=0
