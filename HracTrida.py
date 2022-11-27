class Hrac:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.zivoty = 5
        self.skore = 0

    def minus_zivot(self):
        self.zivoty -= 1

    def plus_zivot(self):
        self.zivoty += 1

    def skoreplus(self, pocet):
        self.skore += 100 * pocet

    def skoreminus(self):
        self.skore -= 25

    def statistika_hrace(self):
        print( f'{self.jmeno} - skore: {self.skore} zivoty: {self.zivoty})')
