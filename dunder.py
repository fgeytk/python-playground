import math
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        delta = stop - start
        print(f"[TIME : {func.__name__} en {delta} s]")
        return result
    return wrapper

class CalculatriceAvancee:
    def __init__(self):
        self.memoire = []
    @timer
    def racine_carree(self, x):
        time.sleep(0.5)
        resultat = math.sqrt(x)
        self.memoire.append(resultat)
        return resultat

    @timer
    def puissance(self, base, exposant):
        time.sleep(0.3)
        resultat = math.pow(base, exposant)
        self.memoire.append(resultat)
        return resultat

    @timer
    def factorielle(self, n):
        time.sleep(0.7)
        resultat = math.factorial(n)
        self.memoire.append(resultat)
        return resultat

    @timer
    def historique(self):
        return self.memoire


test = CalculatriceAvancee()
test.racine_carree(5)

