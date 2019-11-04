import unittest

from bs4 import BeautifulSoup
from cheapest.classes.scrapper import Scrapper
from unittest.mock import patch

class TestScrapperSteam(unittest.TestCase):
    """Class to test the Steam website scrapping"""

    def setUp(self):
        """Setting class and mocks"""
        self.scrapper = Scrapper()
        self.steam_mock = """
                          <div id="search_resultsRows">
                          <a href="url.com"
                          class="search_result_row ds_collapse_flag  app_impression_tracked">
                          <div class="col search_capsule"><img '
                          src="https://steamcdn-a.akamaihd.net/steam/apps/391540/capsule_sm_120.jpg?t=1568414130"
                          srcset="https://steamcdn-a.akamaihd.net/steam/apps/391540/capsule_sm_120.jpg?t=1568414130
                           1x, https://steamcdn-a.akamaihd.net/steam/apps/391540/capsule_231x87.jpg?t=1568414130 2x">
                          </div>
                          <div class="responsive_search_name_combined">
                          <div class="col search_name ellipsis">
                          <span class="title">Undertale</span>
                          <p>
                          <span class="platform_img win"></span><span class="platform_img mac">
                          </span><span class="platform_img linux"></span></p>
                          </div>
                          <div class="col search_released responsive_secondrow">15 sept. 2015</div>
                          <div class="col search_reviewscore responsive_secondrow">
                          <span class="search_review_summary positive" data-tooltip-html="extrêmement positives
                          <br>95 des 91,237 évaluations des utilisateurs pour ce jeu sont positives.">
						  </span></div><div class="col search_price_discount_combined
                           responsive_secondrow" data-price-final="999">
                          <div class="col search_discount responsive_secondrow">
                          </div><div class="col search_price  responsive_secondrow">9,99€</div>
                          </div></div><div style="clear: left;"></div></a>
                          <a href="https://store.steampowered.com/app/391570/UNDERTALE_Soundtrack/?snr=1_7_7_151_150_1"
                           class="search_result_row ds_collapse_flag  app_impression_tracked">
                          <div class="col search_capsule">
                          <img src="https://steamcdn-a.akamaihd.net/steam/apps/391570/capsule_sm_120.jpg?t=1447377370"
                           srcset="https://steamcdn-a.akamaihd.net/steam/apps/391570/capsule_sm_120.jpg?t=1447377370
                           1x, https://steamcdn-a.akamaihd.net/steam/apps/391570/capsule_231x87.jpg?t=1447377370 2x"></div>
                          <div class="responsive_search_name_combined">
                          <div class="col search_name ellipsis">
                          <span class="title">UNDERTALE Soundtrack</span><p>
                          <span class="platform_img win"></span><span class="platform_img mac"></span></p>
                          </div><div class="col search_released responsive_secondrow">15 sept. 2015</div>
                          <div class="col search_reviewscore responsive_secondrow">
                          <span class="search_review_summary positive"
                           data-tooltip-html="extrêmement positives<br>96 des 1,390 évaluations
                           des utilisateurs pour ce jeu sont positives."></span></div>
                          <div class="col search_price_discount_combined responsive_secondrow" data-price-final="999">
                          <div class="col search_discount responsive_secondrow">
                          </div><div class="col search_price  responsive_secondrow">
                          9,99€</div></div></div><div style="clear: left;"></div></a>
                          """
        self.steam_soup = BeautifulSoup(self.steam_mock, 'lxml')

    @patch('cheapest.classes.scrapper.BeautifulSoup')
    def test_steam(self, steam_mock):
        """Checking if the scrapper works well"""
        steam_mock.return_value = self.steam_soup
        steam = self.scrapper.get_steam_result('CSGO')
        response_name, response_price, response_url = 'Undertale', '999', 'url.com'
        self.assertEqual(response_name, steam.name)
        self.assertEqual(response_price, response_price)
        self.assertEqual(response_url, steam.url)


if __name__ == "__main__":
    unittest.main()