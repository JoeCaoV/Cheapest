import requests

from bs4 import BeautifulSoup
from .platforms import Steam


class Scrapper():

    def __init__(self):
        """Setting the base URL for each website we're gonna scrap"""
        self.search_steam_url = "https://store.steampowered.com/search/"

    def get_steam_result(self, search):
        """get the HTML result page for a specific research"""
        params = {'term' : search}
        get = requests.get(self.search_steam_url, params)
        soup = BeautifulSoup(get.content, 'lxml')
        div = soup.find("div", {"id" : "search_resultsRows"})
        url = div.a['href']
        title = div.a.find('span', {"class" : "title"}).string
        price = div.a.find('div', {"class" : "search_price_discount_combined"})["data-price-final"]
        steam = Steam(title, price, url)
        return steam
