"""Class to create object of a game according to his belonging platform"""

class Platform():
    """Parent class"""
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

class Steam(Platform):
    """Steam class"""
    def __init__(self, name, price, url):
        super().__init__(name, price, url)
        self.img = 'steam.png'

class HumbleBundle(Platform):
    """HumbleBundle class"""
    def __init__(self, name, price, url):
        super().__init__(name, price, url)
        self.img = 'humble.png'

class EpicGames(Platform):
    """I think you got it already"""
    def __init__(self, name, price, url):
        super().__init__(name, price, url)
        self.img = 'epicgames.png'
