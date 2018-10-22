import re

import requests
from bs4 import BeautifulSoup


class Parser:
    scheme = 'https'
    url = 'play.google.com'
    apps_path = '/store/apps'
    category_path = '/category'

    def __init__(self):
        pass

    @property
    def categories(self) -> list:
        link = f'{self.scheme}://{self.url}{self.apps_path}'
        response = requests.get(link)
        response_content = response.content.decode()  # bytes to unicode

        reg_exp = fr'{self.apps_path}{self.category_path}/([^\s]+|\?)'
        categories_raw = re.findall(reg_exp, response_content)
        categories = {  # filter bad results
            c[:-1] for c in categories_raw if c.find('?') == -1
            and c.find('\\') == -1
            and c.find('/') == -1
            and c.find('>') == -1
            and c.find(';') == -1
        }

        return list(categories)

    def games(self, category: str) -> list:
        link = (
            f'{self.scheme}://{self.url}{self.apps_path}'
            f'{self.category_path}/{category}'
        )
        response = requests.get(link)
        parsed_html = BeautifulSoup(response.content, features="html.parser")
        games = parsed_html.find_all('a', class_='title')

        return [g['title'] for g in games]

    def results(self) -> dict:
        """
        Get all categories and games.

        :return: dict, keys - categories, values - games for specific category
        """
        results = {}
        for c in self.categories:
            results[c] = self.games(c)
        return results

    def print_all_categories_games(self) -> None:
        """
        Mission 1
        """
        results = self.results()
        for category, games in results.items():
            for game in games:
                print(f'/{category}/{game}')
