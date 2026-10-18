class Stand:
    def __init__(self, codiceUnivoco, supMetriQuad, padiglione, prezzo):
        self._codiceUnivoco = codiceUnivoco
        self._supMetriQuad = int(supMetriQuad)
        self._padiglione = int(padiglione)
        self._prezzo = float(prezzo)
        self.espositore = None

    @property
    def codiceUnivoco(self):
        return self._codiceUnivoco

    @property
    def prezzo_finale(self):
        return self._prezzo

    @property
    def disponibile(self):
        return self.espositore is None

    def __lt__(self, other):
        return self.prezzo_finale < other.prezzo_finale

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore.codiceUnivoco}"
        return f"{self._codiceUnivoco}: Standard | {self._supMetriQuad} mq - Padiglione {self._padiglione} - Prezzo {self.prezzo_finale:.2f}€ - {stato}"

    def __repr__(self):
        return self.__str__()