class Lampe:
    def __init__(self, raum):
        self.raum
        self.an = False

    def einschalten(self):
        if self.an == False:
            self.an = True
        else:
            print("Die Lampe war schon an.")

    def ausschalten(self):
        if self.an == True:
            self.an = False
        else:
            print("Die Lampe war schon aus.")

    def status(self):
        self.