class Stand:
    def __init__(self, codiceUnivoco, supMetriQuad, padiglione, prezzo):
        self._codiceUnivoco = codiceUnivoco
        self._supMetriQuad = int(supMetriQuad)
        self._padiglione = int(padiglione)
        self._prezzo = int(prezzo)

    @property
    def codiceUnivoco(self):
        return self._codiceUnivoco

    @property
    def prezzoFinale(self):
        return self._prezzo