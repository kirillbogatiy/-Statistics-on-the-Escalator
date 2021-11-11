import random

class WithoutSpeedEscalator:
    L = 1
    p = 1.0
    alpha = 1.0
    places = [0]
    number_out = 0
    time = 0

    def __init__(self, L, p, alpha):
        self.L = L
        self.p = p
        self.alpha = alpha
        self.places = [0] * L

    def evalute(self, time):
        self.time += time
        for t in range(time):
            places_new = self.places.copy()
            for i in range(self.L): # 0 0 -> 1 0 -> 
                if i < self.L - 1 and self.places[i] and not self.places[i + 1] and random.random() < self.p:
                    places_new[i] = 0
                    places_new[i + 1] = 1
                if i == self.L - 1 and self.places[i] and random.random() < self.p:
                    places_new[i] = 0
                    self.number_out += 1
                    
            if not self.places[0]:
                if random.random() < self.alpha:
                    places_new[0] = 1
            self.places = places_new
        return self.number_out / self.time


def __main__():
    esc = WithoutSpeedEscalator(10, 1.0, 0.44)
    print(esc.evalute(10000))

__main__()
