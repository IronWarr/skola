import uuid

class Elev:

    def _init_(self, namn, utbildning, tel):
        self.id = str(uuid.uuid4())
        self.namn = namn
        self.utbildning = utbildning
        self.tel = tel

    def get_elev(self):
        svar = self.namn + " | Program: " + self.utbildning + "| Tel: " + self.tel + " | ID: " + self.id
        return svar